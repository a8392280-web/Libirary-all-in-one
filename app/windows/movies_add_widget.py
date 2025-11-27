# add_movie_window.py
from PySide6.QtWidgets import QDialog, QMessageBox, QComboBox
from PySide6.QtCore import Signal, Qt, QThread
from py_ui.movies_add import Ui_add_widget
from app.db.movies_db import insert_movie, list_movies
from app.utils.my_functions import link_to_image, get_selected_section, resize_combo_box_to_contents
from app.fetch.movies_info_fetcher import get_movie_info
from app.models.movie import Movie
from PySide6.QtGui import QPixmap, QColor, QPainter


# ---------------- Worker Thread ----------------
class MovieFetchWorker(QThread):
    """
    Worker thread to fetch movie info without blocking the UI.
    Emits:
      - finished(dict) on success
      - failed(str) on error (uses 'no' or 'not movie' as special tokens)
    """
    finished = Signal(dict)
    failed = Signal(str)

    def __init__(self, movie_name: str):
        super().__init__()
        self.movie_name = movie_name

    def run(self):
        try:
            result = get_movie_info(self.movie_name)
            # Propagate special return values as failures so UI can show messages
            if not result or result == "no":
                self.failed.emit("no")
            elif result == "not movie":
                self.failed.emit("not movie")
            else:
                self.finished.emit(result)
        except Exception as e:
            self.failed.emit(str(e))


class AddMovieWindow(QDialog):
    movie_added = Signal(Movie)  # Emit the new Movie object

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Add New Movie")

        # Keep a reference to the worker to avoid GC while running
        self._search_worker = None

        # ---------------- Setup UI ----------------
        self.setup_buttons()
        self.setup_combo_boxes()

        # Load current movies
        self.data = {sec: list_movies(sec) for sec in ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]}

        # Widget mapping for manual/API abstraction
        self.widget_map = {
            "manual": {
                "section": self.ui.manual_section_selector,
                "name": self.ui.manual_name_input,
                "time": self.ui.manual_time_input,
                "date": self.ui.manual_date_input,
                "plot": self.ui.manual_plot_input,
                "imdb_rate": self.ui.manual_imdb_rate_input,
                "user_rate": self.ui.manual_user_rate_input,
                "genres": self.ui.manual_gener_input,
                "image_url": self.ui.image_url,
                "trailer": self.ui.manual_trailer_input
            },
            "api": {
                "section": self.ui.api_section_selector,
                "name": self.ui.api_name_input,
                "time": self.ui.api_time_input,
                "date": self.ui.api_date_input,
                "plot": self.ui.api_plot_input,
                "imdb_rate": self.ui.api_imdb_rate_input,
                "user_rate": self.ui.api_user_rate_input,
                "genres": self.ui.api_gener_input,
                "image_url": None,
                "trailer": self.ui.api_trailer_input
            }
        }

        # ---------------- Connect signals ----------------
        self.ui.manual_button.clicked.connect(lambda: self.toggle_fields("manual"))
        self.ui.api_button.clicked.connect(lambda: self.toggle_fields("api"))
        self.ui.manual_cancel_button.clicked.connect(self.close)
        self.ui.api_cancel_button.clicked.connect(self.close)
        self.ui.manual_apply_button.clicked.connect(lambda: self.add_movie_entry("manual"))
        self.ui.api_apply_button.clicked.connect(lambda: self.add_movie_entry("api"))
        self.ui.search_button.clicked.connect(self.search_and_show)
        self.ui.image_url.returnPressed.connect(lambda: self.load_image(self.ui.image_url.text().strip(), self.ui.manual_image_label))

        # Default to manual view
        self.toggle_fields("manual")

    # ---------------- Button & Combo Setup ----------------
    def setup_buttons(self):
        buttons = [
            (self.ui.manual_button, "1"),
            (self.ui.api_button, "2"),
            (self.ui.manual_apply_button, None),
            (self.ui.api_apply_button, None),
            (self.ui.manual_cancel_button, None),
            (self.ui.api_cancel_button, None)
        ]
        for btn, shortcut in buttons:
            btn.setAutoDefault(False)
            btn.setDefault(False)
            if shortcut:
                btn.setShortcut(shortcut)

    def setup_combo_boxes(self):
        # Populate sections
        sections = ["Watching", "Want_to_watch", "Continue_later", "Dont_want_to_continue", "Watched"]
        for section in sections:
            self.ui.manual_section_selector.addItem(section.replace("_", " ").capitalize())
            self.ui.api_section_selector.addItem(section.replace("_", " ").capitalize())

        # Auto-resize long items
        self.setup_combo_box_resizing(self.ui.manual_section_selector)
        self.setup_combo_box_resizing(self.ui.api_section_selector)

    def setup_combo_box_resizing(self, combo: QComboBox):
        original_show_popup = combo.showPopup
        def new_show_popup():
            resize_combo_box_to_contents(combo)
            original_show_popup()
        combo.showPopup = new_show_popup

    # ---------------- Field Toggling ----------------
    def toggle_fields(self, source="manual"):
        self.ui.stackedWidget.setCurrentIndex(0 if source=="manual" else 1)

    # ---------------- Image Handling ----------------
    def load_image(self, url: str, label, width=180, height=270):
        if not url:
            label.setPixmap(self.get_placeholder_pixmap(width, height))
            return
        try:
            link_to_image(url, label, width, height)
        except Exception as e:
            print(f"❌ Failed to load image: {e}")
            label.setPixmap(self.get_placeholder_pixmap(width, height))

    def get_placeholder_pixmap(self, width, height):
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor("#444"))
        painter = QPainter(pixmap)
        painter.setPen(QColor("#ccc"))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "No Image")
        painter.end()
        return pixmap

    # ---------------- Movie Entry ----------------
    def add_movie_entry(self, source="manual"):
        try:
            data = self.extract_movie_data(source)
            self.validate_movie_data(data)

            duplicate_section = self.check_duplicate(data["title"])
            if duplicate_section:
                reply = QMessageBox.question(
                    self, "Confirm Adding",
                    f"There is a movie with this name ({data['title']}) in the ({duplicate_section.replace('_', ' ')}) section.\n"
                    "Are you sure you want to add this movie again?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.No:
                    QMessageBox.information(self, "Add Canceled", "Movie was not added.", QMessageBox.Ok)
                    return

            self.insert_movie_data(data)
            self.close()
            QMessageBox.information(self, "Success", f"'{data['title']}' was added successfully!", QMessageBox.Ok)
            

        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", str(e), QMessageBox.Ok)

    def extract_movie_data(self, source="manual"):
        widgets = self.widget_map[source]
        image_url = widgets["image_url"].text().strip() if source=="manual" else getattr(self, "api_movie_url", "")

        return {
            "section": get_selected_section(widgets["section"]),
            "title": widgets["name"].text().strip(),
            "runtime": widgets["time"].text().replace("min", "").strip(),
            "year": widgets["date"].text().strip(),
            "imdb_rate": widgets["imdb_rate"].text().strip(),
            "user_rate": widgets["user_rate"].text().strip(),
            "plot": widgets["plot"].text().strip(),
            "genres": [g.strip() for g in widgets["genres"].text().split("-") if g.strip()],
            "poster_path": image_url,
            "trailer": widgets["trailer"].text().strip(),
            "imdb_id": getattr(self, "movie_imdb_id", None),
            "tmdb_id": getattr(self, "movie_tmdb_id", None)
        }

    def validate_movie_data(self, data: dict):
        if not data["title"]:
            raise ValueError("Movie name cannot be empty.")
        if not data["section"]:
            raise ValueError("Please select a section for the movie.")

        for key in ["imdb_rate", "user_rate"]:
            if data[key]:
                try:
                    val = float(data[key])
                    if val < 0 or val > 10:
                        raise ValueError(f"{key.replace('_',' ').title()} must be between 0 and 10.")
                except ValueError:
                    raise ValueError(f"{key.replace('_',' ').title()} must be a number (e.g., 7.5)")

        if data["runtime"]:
            try:
                runtime_int = int(data["runtime"])
                if runtime_int <= 0:
                    raise ValueError("Runtime must be a positive number.")
            except ValueError:
                raise ValueError("Runtime must be a whole number (e.g., 120).")

        if data["year"]:
            if len(data["year"]) != 4 or not data["year"].isdigit():
                raise ValueError("Year must be exactly 4 digits (e.g., 2024).")
        return True

    def check_duplicate(self, title: str):
        title_lower = title.strip().lower()
        for section, movies in self.data.items():
            for movie in movies:
                if movie.title.strip().lower() == title_lower:
                    return section
        return None

    def insert_movie_data(self, data: dict):
        new_movie = Movie(
            title=data["title"],
            runtime=int(data["runtime"]) if data["runtime"] else None,
            year=data["year"],
            rating=float(data["imdb_rate"]) if data["imdb_rate"] else None,
            user_rating=float(data["user_rate"]) if data["user_rate"] else None,
            poster_path=data["poster_path"],
            plot=data["plot"],
            genres=data["genres"],
            imdb_id=data.get("imdb_id"),
            tmdb_id=data.get("tmdb_id"),
            section=data["section"],
            trailer=data["trailer"]
        )
        
        insert_movie(new_movie)
        self.movie_added.emit(new_movie)

    # ---------------- Search & Display ----------------
    # keep existing synchronous helper (still usable elsewhere)
    # def search_movie_info(self, movie_name: str):
    #     
    #     if not movie_name:
    #         QMessageBox.warning(self, "Empty Search", "Please enter a movie name.", QMessageBox.Ok)
    #         return None
    #     try:
    #         movie_info = get_movie_info(movie_name)
    #     except Exception as e:
    #         QMessageBox.critical(self, "Connection Error", f"Error fetching movie info:\n{e}", QMessageBox.Ok)
    #         return None

    #     if not movie_info or movie_info == "no":
    #         QMessageBox.information(self, "Movie Not Found", f"No results for '{movie_name}'.", QMessageBox.Ok)
    #         return None

    #     if movie_info == "not movie":
    #         QMessageBox.information(self, "Movie Not Found", f"No Movie results for '{movie_name}', but there is a series.", QMessageBox.Ok)
    #         return None

    #     return movie_info

    def display_movie_info(self, movie_info: dict):
        # Set IDs to None if missing (keeps DB insert consistent)
        self.movie_imdb_id = movie_info.get("imdb_id", None)
        self.movie_tmdb_id = movie_info.get("tmdb_id", None)

        self.ui.api_name_input.setText(movie_info.get("Name", "N/A"))
        self.ui.api_time_input.setText(str(movie_info.get("Runtime", "N/A")))
        self.ui.api_date_input.setText(movie_info.get("Released", "N/A"))
        self.ui.api_gener_input.setText("-".join(movie_info.get("Genres", [])))
        self.ui.api_imdb_rate_input.setText(movie_info.get("Rating", "N/A"))
        self.ui.api_plot_input.setText(movie_info.get("Plot", "N/A"))
        self.ui.api_trailer_input.setText(movie_info.get("trailer", "N/A"))
        self.ui.api_plot_input.setCursorPosition(0)
        self.api_movie_url = movie_info.get("Image", "")
        self.load_image(self.api_movie_url, self.ui.api_image_label, 180, 270)

    def search_and_show(self):
        """
        Start a background worker to fetch movie info so UI doesn't freeze.
        """
        movie_name = self.ui.search_line.text().strip()
        if not movie_name:
            QMessageBox.warning(self, "Empty Search", "Please enter a movie name.", QMessageBox.Ok)
            return

        # Disable search controls while working
        self.ui.search_button.setEnabled(False)
        self.ui.search_button.setText("Searching...")

        # Create and start the worker
        self._search_worker = MovieFetchWorker(movie_name)
        self._search_worker.finished.connect(self._on_search_success)
        self._search_worker.failed.connect(self._on_search_failed)
        self._search_worker.start()

    # ---------------- Worker callbacks ----------------
    def _on_search_success(self, movie_info: dict):
        # Re-enable UI
        self.ui.search_button.setEnabled(True)
        self.ui.search_button.setText("Search")
        # Display the returned info
        self.display_movie_info(movie_info)
        # Clear worker reference
        self._search_worker = None

    def _on_search_failed(self, error: str):
        # Re-enable UI
        self.ui.search_button.setEnabled(True)
        self.ui.search_button.setText("Search")

        if error == "no":
            QMessageBox.information(self, "Movie Not Found", "No results found.", QMessageBox.Ok)
        elif error == "not movie":
            QMessageBox.information(self, "Movie Not Found", "No Movie results found (maybe a series).", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Error Fetching Movie", f"Error: {error}", QMessageBox.Ok)

        # Clear worker reference
        self._search_worker = None











# # add_movie_window.py
# from PySide6.QtWidgets import QDialog, QMessageBox,QComboBox
# from py_ui.movies_add import Ui_add_widget
# from app.db.movies_db import insert_movie , list_movies
# from app.utils.my_functions import link_to_image , get_selected_section, resize_combo_box_to_contents
# from PySide6.QtCore import Signal  
# from app.fetch.movies_info_fetcher import get_movie_info
# from app.models.movie import Movie

# class AddMovieWindow(QDialog): 

#     movie_added = Signal()  # Signal emitted when a movie is successfully added
#     def __init__(self, parent=None): # Optional parent parameter
#         super().__init__(parent) # Call the parent constructor
#         self.ui = Ui_add_widget() # Create an instance of the UI class
#         self.ui.setupUi(self) # Set up the UI
#         self.setWindowTitle("Add New Movie")

#         # Disable default/autoDefault behavior for buttons
#         self.ui.api_button.setAutoDefault(False)
#         self.ui.api_button.setDefault(False)
#         self.ui.manual_button.setAutoDefault(False)
#         self.ui.manual_button.setDefault(False)

#         self.ui.image_url.returnPressed.connect(self.image)  # Trigger image loading when Enter is pressed in the URL field

#         # Load current movies grouped by section
#         self.data = {sec: list_movies(sec) for sec in ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]}

#         #-------------------- Setup combobox ------------------------

#         # make the long text in the combobox seen
#         self.ui.api_section_selector.showPopup = lambda: (resize_combo_box_to_contents(self.ui.api_section_selector),
#                                                 QComboBox.showPopup(self.ui.api_section_selector))
#         self.ui.manual_section_selector.showPopup = lambda: (resize_combo_box_to_contents(self.ui.manual_section_selector),
#                                                 QComboBox.showPopup(self.ui.manual_section_selector))
#         self.comboBox()

#         #---------------------- Setup buttons -----------------------
#         self.ui.manual_button.clicked.connect(self.toggle_manual_fields)
#         self.ui.manual_button.setShortcut("1")
#         self.ui.api_button.clicked.connect(self.toggle_api_fields)
#         self.ui.api_button.setShortcut("2")

#         self.ui.manual_cancel_button.clicked.connect(self.close)
#         self.ui.api_cancel_button.clicked.connect(self.close)
#         self.ui.manual_apply_button.clicked.connect(self.add_manual)
#         self.ui.search_button.clicked.connect(self.search_and_show)
#         self.ui.api_apply_button.clicked.connect(self.add_api)

#     # Slots:-
#     def toggle_api_fields(self):
#         "Switch to API widget fields"
#         self.ui.stackedWidget.setCurrentIndex(1)
#     def toggle_manual_fields(self):
#         "Switch to Manual widget fields"
#         self.ui.stackedWidget.setCurrentIndex(0)

#     def image(self):
#         "Load and display image from the entered URL"
#         path = self.ui.image_url.text().strip()
#         link_to_image(path,self.ui.manual_image_label,180,270)

#     def comboBox(self):
#         "Populate section selectors with available categories"

#         self.ui.manual_section_selector.clear()
#         self.ui.api_section_selector.clear()

#         list_of_sections=["Watching","Want_to_watch","Continue_later","Dont_want_to_continue","Watched"]
#         for section in list_of_sections:
#             self.ui.manual_section_selector.addItem(section.replace("_"," ").capitalize())
#             self.ui.api_section_selector.addItem(section.replace("_"," ").capitalize())

 
#     def search_and_show(self):
#         # Search for a movie by name and display its info
#         movie_name = self.ui.search_line.text().strip()
#         if not movie_name:
#             QMessageBox.warning(self, "Empty Search", "Please enter a movie name.", QMessageBox.Ok)
#             return

#         movie_info = get_movie_info(movie_name)
#         if not movie_info:
#             QMessageBox.critical(self, "Connection Error", "Check your internet connection.", QMessageBox.Ok)
#             return
#         if movie_info == "no":
#             QMessageBox.information(self, "Movie Not Found", f"No results for '{movie_name}'.", QMessageBox.Ok)
#             return
#         if movie_info == "not movie":
#             QMessageBox.information(self, "Movie Not Found", f"No Movie results for '{movie_name}' But there is a series.", QMessageBox.Ok)
#             return

#         # Display movie info
#         self.movie_imdb_id = movie_info.get("imdb_id", "N/A")
        
#         self.ui.api_name_input.setText(movie_info.get("Name", "N/A"))
#         self.ui.api_time_input.setText(str(movie_info.get("Runtime", "N/A")))
#         self.ui.api_date_input.setText(movie_info.get("Released", "N/A"))
#         self.ui.api_gener_input.setText("-".join(movie_info.get("Genres", [])))
#         self.ui.api_imdb_rate_input.setText(movie_info.get("Rating", "N/A"))
#         self.ui.api_plot_input.setText(movie_info.get("Plot", "N/A"))
#         self.ui.api_trailer_input.setText(movie_info.get("trailer", "N/A"))
#         self.ui.api_plot_input.setCursorPosition(0)

#         # Show image
#         self.api_movie_url = movie_info.get("Image", "")
#         link_to_image(self.api_movie_url, self.ui.api_image_label, 180, 270)


#     def add_manual(self):
#         # Add a manually entered movie
#         self.add_movie_entry("manual")

#     def add_api(self):
#         # Add a movie fetched via the API
#         self.add_movie_entry("api")

#     def add_movie_entry(self, source="manual"):
#         # Select the correct UI set based on source
#         if source == "manual":
#             section_selector = self.ui.manual_section_selector
#             name_input = self.ui.manual_name_input
#             time_input = self.ui.manual_time_input
#             date_input = self.ui.manual_date_input
#             plot_input = self.ui.manual_plot_input
#             imdb_input = self.ui.manual_imdb_rate_input
#             user_input = self.ui.manual_user_rate_input
#             genre_input = self.ui.manual_gener_input
#             image_url = self.ui.image_url.text().strip()
#             trailer_input = self.ui.manual_trailer_input
#         else:
#             section_selector = self.ui.api_section_selector
#             name_input = self.ui.api_name_input
#             time_input = self.ui.api_time_input
#             date_input = self.ui.api_date_input
#             plot_input = self.ui.api_plot_input
#             imdb_input = self.ui.api_imdb_rate_input
#             user_input = self.ui.api_user_rate_input
#             genre_input = self.ui.api_gener_input
#             image_url = self.api_movie_url
#             trailer_input = self.ui.api_trailer_input

#         # Validation
#         if section_selector.currentIndex() == -1 or not name_input.text().strip():
#             return

#         # Extract data
#         name = name_input.text().strip()
#         runtime = time_input.text().replace("min"," ").strip()
#         released = date_input.text().strip()
#         imdb_rate = imdb_input.text().strip()
#         plot = plot_input.text().strip()
#         user_rate = user_input.text().strip()
#         genres = [g.strip() for g in genre_input.text().split("-") if g.strip()]
#         section = get_selected_section(section_selector)
#         trailer = trailer_input.text().strip()


#         try:
#             # Validate and convert fields
#             if imdb_rate:
#                 try:
#                     imdb_rate_float = float(imdb_rate)
#                     if imdb_rate_float < 0 or imdb_rate_float > 10:
#                         raise ValueError("IMDB rating must be between 0 and 10")
#                 except ValueError:
#                     raise ValueError("IMDB Rating must be a number (e.g., 7.5 or 8)")
            
#             if user_rate:
#                 try:
#                     user_rate_float = float(user_rate)
#                     if user_rate_float < 0 or user_rate_float > 10:
#                         raise ValueError("User rating must be between 0 and 10")
#                 except ValueError:
#                     raise ValueError("User Rating must be a number (e.g., 7.5 or 8)")
                        
#             if runtime:
#                 try:
#                     runtime_int = int(runtime.replace("min", " ")) 
#                     if runtime_int <= 0:
#                         raise ValueError("Runtime must be a positive number")
#                 except ValueError:
#                     raise ValueError("Runtime must be a whole number (e.g., 120)")
                        
#             # Validate year (released) - should be 4 digits
#             if released:
#                 if len(released) != 4:
#                     raise ValueError("Year must be exactly 4 digits (e.g., 2024)")
#                 if not released.isdigit():
#                     raise ValueError("Year must contain only numbers (e.g., 2024)")
                        
#         except ValueError as e:
#             reply = QMessageBox.critical(
#                 self, "Invalid Input",
#                 f"Please check the following field:\n\n{str(e)}",
#                 QMessageBox.Ok
#             )
#             return  # Stop the process if validation fails



                

#         # Duplicate check
#         for key, movies in self.data.items():
#             for movie in movies:
#                 if movie.title.strip().lower() == name.lower():
#                     reply = QMessageBox.question(
#                         self, "Confirm Adding",
#                         f"There is a movie with this name ({movie.title}) in the ({key.replace('_', ' ')}) section.\n"
#                         "Are you sure you want to add this movie again?",
#                         QMessageBox.Yes | QMessageBox.No
#                     )
#                     if reply == QMessageBox.No:
#                         print("❌ Adding canceled")
#                         return
#                     break

#         # Add movie
#         imdb_id = getattr(self, "movie_imdb_id", None)
#         new_movie = Movie(
#             title=name,
#             runtime=runtime,
#             year=released,
#             rating=float(imdb_rate) if imdb_rate else None,
#             user_rating=float(user_rate) if user_rate else None,
#             poster_path=image_url,
#             plot=plot,
#             genres=genres,
#             imdb_id=getattr(self, "movie_imdb_id", None),
#             section=section,
#             trailer=trailer
#         )
#         insert_movie(new_movie)

#         # Emit the signal before closing
#         self.movie_added.emit()

#         self.close()





