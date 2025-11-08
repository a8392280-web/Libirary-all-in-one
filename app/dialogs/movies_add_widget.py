# add_movie_window.py
from PySide6.QtWidgets import QDialog, QMessageBox,QComboBox
from py_ui.movies_add import Ui_add_widget
from app.db.sqlite_manger import insert_movie , list_movies
from app.utils.my_functions import link_to_image , get_selected_section, resize_combo_box_to_contents
from app.utils.info_from_APIs import get_movie_info
from app.models.movie import Movie
from PySide6.QtCore import Signal  # Add this import
class AddMovieWindow(QDialog): # Inherit from QDialog for modal behavior
    movie_added = Signal()  # Signal emitted when a movie is successfully added
    def __init__(self, parent=None): # Optional parent parameter
        super().__init__(parent) # Call the parent constructor
        self.ui = Ui_add_widget() # Create an instance of the UI class
        self.ui.setupUi(self) # Set up the UI
        self.setWindowTitle("Add New Movie")

        # Disable default/autoDefault behavior for buttons
        self.ui.api_button.setAutoDefault(False)
        self.ui.api_button.setDefault(False)
        self.ui.manual_button.setAutoDefault(False)
        self.ui.manual_button.setDefault(False)


        self.ui.image_url.returnPressed.connect(self.image)  # Trigger image loading when Enter is pressed in the URL field

        # Load current movies grouped by section
        self.data = {sec: list_movies(sec) for sec in ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]}

        #-------------------- Setup combobox ------------------------

        # make the long text in the combobox seen
        self.ui.api_section_selector.showPopup = lambda: (resize_combo_box_to_contents(self.ui.api_section_selector),
                                                QComboBox.showPopup(self.ui.api_section_selector))
        self.ui.manual_section_selector.showPopup = lambda: (resize_combo_box_to_contents(self.ui.manual_section_selector),
                                                QComboBox.showPopup(self.ui.manual_section_selector))
        self.comboBox()

        #---------------------- Setup buttons -----------------------
        self.ui.manual_button.clicked.connect(self.toggle_manual_fields)
        self.ui.manual_button.setShortcut("1")
        self.ui.api_button.clicked.connect(self.toggle_api_fields)
        self.ui.api_button.setShortcut("2")

        self.ui.manual_cancel_button.clicked.connect(self.close)
        self.ui.api_cancel_button.clicked.connect(self.close)
        self.ui.manual_apply_button.clicked.connect(self.add_manual)
        self.ui.search_button.clicked.connect(self.search_and_show)
        self.ui.api_apply_button.clicked.connect(self.add_api)

    # Slots:-
    def toggle_api_fields(self):
        "Switch to API widget fields"
        self.ui.stackedWidget.setCurrentIndex(1)
    def toggle_manual_fields(self):
        "Switch to Manual widget fields"
        self.ui.stackedWidget.setCurrentIndex(0)

    def image(self):
        "Load and display image from the entered URL"
        path = self.ui.image_url.text().strip()
        link_to_image(path,self.ui.manual_image_label,180,270)

    def comboBox(self):
        "Populate section selectors with available categories"

        self.ui.manual_section_selector.clear()
        self.ui.api_section_selector.clear()

        list_of_sections=["Watching","Want_to_watch","Continue_later","Dont_want_to_continue","Watched"]
        for section in list_of_sections:
            self.ui.manual_section_selector.addItem(section.replace("_"," ").capitalize())
            self.ui.api_section_selector.addItem(section.replace("_"," ").capitalize())


                            
    def search_and_show(self):
        # Search for a movie by name and display its info
        movie_name = self.ui.search_line.text().strip()
        if not movie_name:
            QMessageBox.warning(self, "Empty Search", "Please enter a movie name.", QMessageBox.Ok)
            return

        movie_info = get_movie_info(movie_name)
        if not movie_info:
            QMessageBox.critical(self, "Connection Error", "Check your internet connection.", QMessageBox.Ok)
            return
        if movie_info == "no":
            QMessageBox.information(self, "Movie Not Found", f"No results for '{movie_name}'.", QMessageBox.Ok)
            return

        # Display movie info
        self.movie_imdb_id = movie_info.get("imdb_id", "N/A")
        
        self.ui.api_name_input.setText(movie_info.get("Name", "N/A"))
        self.ui.api_time_input.setText(movie_info.get("Runtime", "N/A"))
        self.ui.api_date_input.setText(movie_info.get("Released", "N/A"))
        self.ui.api_gener_input.setText("-".join(movie_info.get("Genres", [])))
        self.ui.api_imdb_rate_input.setText(movie_info.get("Rating", "N/A"))
        self.ui.api_plot_input.setText(movie_info.get("Plot", "N/A"))
        self.ui.api_plot_input.setCursorPosition(0)

        # Show image
        self.api_movie_url = movie_info.get("Image", "")
        link_to_image(self.api_movie_url, self.ui.api_image_label, 180, 270)


    
    def add_manual(self):
        # Add a manually entered movie
        self.add_movie_entry("manual")

    def add_api(self):
        # Add a movie fetched via the API
        self.add_movie_entry("api")


    def add_movie_entry(self, source="manual"):
        # Select the correct UI set based on source
        if source == "manual":
            section_selector = self.ui.manual_section_selector
            name_input = self.ui.manual_name_input
            time_input = self.ui.manual_time_input
            date_input = self.ui.manual_date_input
            plot_input = self.ui.manual_plot_input
            imdb_input = self.ui.manual_imdb_rate_input
            user_input = self.ui.manual_user_rate_input
            genre_input = self.ui.manual_gener_input
            image_url = self.ui.image_url.text().strip()
        else:
            section_selector = self.ui.api_section_selector
            name_input = self.ui.api_name_input
            time_input = self.ui.api_time_input
            date_input = self.ui.api_date_input
            plot_input = self.ui.api_plot_input
            imdb_input = self.ui.api_imdb_rate_input
            user_input = self.ui.api_user_rate_input
            genre_input = self.ui.api_gener_input
            image_url = self.api_movie_url

        # Validation
        if section_selector.currentIndex() == -1 or not name_input.text().strip():
            return

        # Extract data
        name = name_input.text().strip()
        runtime = time_input.text().strip()
        released = date_input.text().strip()
        imdb_rate = imdb_input.text().strip()
        plot = plot_input.text().strip()
        user_rate = user_input.text().strip()
        genres = [g.strip() for g in genre_input.text().split("-") if g.strip()]
        section = get_selected_section(section_selector)


        try:
            # Validate and convert fields
            if imdb_rate:
                imdb_rate = float(imdb_rate)  # This will raise ValueError if not convertible
            
            if user_rate:
                user_rate = float(user_rate)  # This will raise ValueError if not convertible
                
            if runtime:
                runtime = int(runtime)  # This will raise ValueError if not convertible
                
            # Validate year (released) - should be 4 digits
            if released and (len(released) != 4 or not released.isdigit()):
                raise ValueError("Year must be 4 digits")
                
        except ValueError as e:
            reply = QMessageBox.critical(
                self, "Field Error",
                f"Invalid value in one or more fields:\n\n{str(e)}",
                QMessageBox.Ok
            )
            return  # Stop the process if validation fails



                

        # Duplicate check
        for key, movies in self.data.items():
            for movie in movies:
                if movie.title.strip().lower() == name.lower():
                    reply = QMessageBox.question(
                        self, "Confirm Adding",
                        f"There is a movie with this name ({movie.title}) in the ({key.replace('_', ' ')}) section.\n"
                        "Are you sure you want to add this movie again?",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    if reply == QMessageBox.No:
                        print("❌ Adding canceled")
                        return
                    break



        # Add movie
        imdb_id = getattr(self, "movie_imdb_id", None)
        new_movie = Movie(
            title=name,
            runtime=runtime,
            year=released,
            rating=float(imdb_rate) if imdb_rate else None,
            user_rating=float(user_rate) if user_rate else None,
            poster_path=image_url,
            plot=plot,
            genres=genres,
            imdb_id=getattr(self, "movie_imdb_id", None),
            section=section
        )
        insert_movie(new_movie)

        # Emit the signal before closing
        self.movie_added.emit()

        self.close()


        
#------------------------------- information------------------------------------



# Use ["key"] → when you are sure the key exists (like internal data).

# Use .get("key", default) → when reading from external data (like APIs, files, or user input).
    # This is the safe access method. If the key doesn’t exist, it returns None (or a default value if you provide one).