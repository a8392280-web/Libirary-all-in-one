# show_movie_window.py
import logging
from typing import Optional, Dict, Any, Tuple

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QCursor, QPixmap, QColor, QPainter, QKeySequence,QShortcut
from PySide6.QtWidgets import (
    QDialog, QMessageBox, QComboBox, QLabel
)

from py_ui.movies_show import Ui_show
from app.db.movies_db import get_movie_by_id, update_movie, delete_movie, move_movie_section
from app.utils.my_functions import link_to_image, get_selected_section, resize_combo_box_to_contents
from app.fetch.movies_info_fetcher import ArabSeedScraper, AkwamScraper
from app.models.movie import Movie

logger = logging.getLogger(__name__)

from PySide6.QtCore import QThread, Signal

class WatchLinkWorker(QThread):
    finished = Signal(str)  # the URL or None

    def __init__(self, button, movie):
        super().__init__()
        self.button = button
        self.movie = movie

    def run(self):
        url = None
        title_query = f"{self.movie.title} {self.movie.year or ''}".strip()
        try:
            if self.button == 1:
                scraper = AkwamScraper(self.movie.title, self.movie.year)
                url = scraper.watch_url
            elif self.button == 2:
                scraper = ArabSeedScraper(title_query)
                url = scraper.watch_url
            elif self.button == 3:
                url = f"https://www.vidking.net/embed/movie/{self.movie.tmdb_id}"
        except Exception as e:
            print(f"Scraper failed: {e}")
            url = None
        self.finished.emit(url)


class ClickableLabel(QLabel):   # reuse your clickable label for plot/trailer previews
    clicked = Signal()
    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)


class ShowMovieWindow(QDialog):
    # Emit meaningful payloads so parent can update UI without reloading everything
    movie_deleted = Signal(int)                 # movie id
    movie_moved = Signal(int, str)              # movie id, new_section
    movie_updated = Signal(object)              # Movie object

    def __init__(self, section: str, movie_id: int, parent=None):
        super().__init__(parent)
        self.ui = Ui_show()
        self.ui.setupUi(self)
        self.setWindowTitle("Movie Details")

        self.active_workers = []
        self.section = section
        self.id = movie_id
        self.movie: Optional[Movie] = None
        self.original_image_url: str = ""

        # Field maps to reduce repetition
        self.edit_widget_map = {
            "title": self.ui.show_edit_name_line,
            "runtime": self.ui.show_edit_time_line,
            "year": self.ui.show_edit_date_line,
            "genres": self.ui.show_edit_gener_line,
            "plot": self.ui.show_edit_plot_line,
            "rating": self.ui.show_edit_imdb_rate_line,
            "user_rating": self.ui.show_edit_user_rate_line,
            "image_url": self.ui.show_edit_image_url,
        }

        # Setup UI bits
        self._setup_buttons_and_shortcuts()
        self._setup_move_combobox()
        self._connect_signals()
        self._load_movie()   # populates self.movie and refreshes UI

    # ---------------- Setup helpers ----------------
    def _setup_buttons_and_shortcuts(self):
        # prevent accidental default button activation
        for btn in (
            self.ui.show_delete_button, self.ui.show_edit_button,
            self.ui.show_cancel_button, self.ui.show_apply_button,
            self.ui.show_edit_apply_button, self.ui.show_edit_cancel_button,
            self.ui.watch_button_1, self.ui.watch_button_2, self.ui.watch_button_3
        ):
            try:
                btn.setAutoDefault(False)
                btn.setDefault(False)
            except Exception:
                pass

        # keyboard shortcuts
        self.ui.show_delete_button.setShortcut("Del")
        self.ui.show_edit_button.setShortcut("E")

        # useful global shortcuts
        QShortcut(QKeySequence("Esc"), self, activated=self._exit_edit_mode)
        QShortcut(QKeySequence("Ctrl+S"), self, activated=self.apply_edit)

    def _setup_move_combobox(self):
        # populate move-to combobox excluding current section
        self.ui.move_to_combobox.clear()
        sections = ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]
        for sec in sections:
            if sec == self.section:
                continue
            self.ui.move_to_combobox.addItem(sec.replace("_", " ").capitalize())

        # dynamic resize on show
        self.ui.move_to_combobox.showPopup = lambda: (
            resize_combo_box_to_contents(self.ui.move_to_combobox),
            QComboBox.showPopup(self.ui.move_to_combobox)
        )

    def _connect_signals(self):
        # Main actions
        self.ui.show_delete_button.clicked.connect(self.delete_current_movie)
        self.ui.show_edit_button.clicked.connect(self.enter_edit_mode)
        self.ui.show_cancel_button.clicked.connect(self.close)
        self.ui.show_apply_button.clicked.connect(self.move_to)
        self.ui.show_edit_apply_button.clicked.connect(self.apply_edit)
        self.ui.show_edit_cancel_button.clicked.connect(self._exit_edit_mode)

        # watch buttons
        self.ui.watch_button_1.setText("Watch on Akwam")
        self.ui.watch_button_2.setText("Watch on ArabSeed")
        self.ui.watch_button_3.setText("Watch on Cineby")
        self.ui.watch_button_1.clicked.connect(lambda: self.open_watch_link(1))
        self.ui.watch_button_2.clicked.connect(lambda: self.open_watch_link(2))
        self.ui.watch_button_3.clicked.connect(lambda: self.open_watch_link(3))

        # clickable plot/trailer (use signal if UI provides clickable QLabel; otherwise set event handlers)
        try:
            self.ui.plot_widget.clicked.connect(self._show_full_plot)
        except Exception:
            self.ui.plot_widget.mousePressEvent = lambda _: self._show_full_plot()

        try:
            self.ui.trailer_widget.clicked.connect(self._open_trailer)
        except Exception:
            self.ui.trailer_widget.mousePressEvent = lambda _: self._open_trailer()

        # preview image on Enter in edit image field
        self.ui.show_edit_image_url.returnPressed.connect(self.preview_or_restore_image)

    # ---------------- Loading & Display ----------------
    def _load_movie(self):
        """Load movie from DB and refresh UI. Wrap DB calls with error handling."""
        try:
            self.movie = get_movie_by_id(self.id)
        except Exception as e:
            logger.exception("Failed to fetch movie by id %s: %s", self.id, e)
            QMessageBox.critical(self, "Error", f"Failed to load movie: {e}")
            self.close()
            return

        if not self.movie:
            QMessageBox.critical(self, "Error", "Movie not found.")
            self.close()
            return

        # Cache original image URL for restore
        self.original_image_url = self.movie.poster_path or ""

        self.refresh_display()

    def refresh_display(self):
        """Populate the view UI with current movie data from self.movie"""
        movie = self.movie
        if not movie:
            return

        self.ui.show_name_lable.setText(movie.title or "No title")
        self.ui.show_time_lable.setText(f"{movie.runtime} min" if movie.runtime else "Runtime not available")
        self.ui.show_label.setText(str(movie.year) if movie.year else "Year not available")
        self.ui.show_gener_lable.setText(", ".join(movie.genres) if movie.genres else "No genres")
        self.ui.show_imdb_rate_lable.setText(str(movie.rating) if movie.rating else "No rating")
        self.ui.show_user_rate_lable.setText(str(movie.user_rating) if movie.user_rating else "No user rating")

        # plot and trailer: set tooltip and pointer style
        self.ui.plot_widget.setToolTip("Click to see full plot")
        self.ui.plot_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.trailer_widget.setToolTip("Click to open trailer")
        self.ui.trailer_widget.setCursor(QCursor(Qt.PointingHandCursor))

        # image
        if movie.poster_path:
            self._load_image_safe(movie.poster_path, self.ui.show_image_lable)
        else:
            self._set_label_placeholder(self.ui.show_image_lable, "No Image Available")

    # ---------------- Image helpers ----------------
    def _load_image_safe(self, url: str, label, width=180, height=270) -> None:
        """Try to load an image using link_to_image, fallback to placeholder on error."""
        if not url:
            self._set_label_placeholder(label, "No Image")
            return
        try:
            link_to_image(path=url, label=label, x=width, y=height)
        except Exception as e:
            logger.warning("Failed to load image %s: %s", url, e)
            self._set_label_placeholder(label, "No Image")

    def _set_label_placeholder(self, label, text="No Image", width=180, height=270) -> None:
        label.setPixmap(self._placeholder_pixmap(width, height))
        label.setAlignment(Qt.AlignCenter)
        label.setToolTip(text)

    def _placeholder_pixmap(self, width=180, height=270) -> QPixmap:
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor("#444"))
        painter = QPainter(pixmap)
        painter.setPen(QColor("#ccc"))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "No Image")
        painter.end()
        return pixmap

    # ---------------- Edit mode ----------------
    def enter_edit_mode(self):
        """Populate edit fields and switch to edit page."""
        if not self.movie:
            QMessageBox.warning(self, "No movie", "Movie not loaded.")
            return

        m = self.movie
        self.edit_widget_map["title"].setText(m.title or "")
        self.edit_widget_map["runtime"].setText(str(m.runtime) if m.runtime is not None else "")
        self.edit_widget_map["year"].setText(str(m.year) if m.year is not None else "")
        self.edit_widget_map["genres"].setText(", ".join(m.genres) if m.genres else "")
        self.edit_widget_map["plot"].setText(m.plot or "")
        self.edit_widget_map["rating"].setText(str(m.rating) if m.rating is not None else "")
        self.edit_widget_map["user_rating"].setText(str(m.user_rating) if m.user_rating is not None else "")
        self.edit_widget_map["image_url"].setText(m.poster_path or "")

        # preview current poster in edit label
        if m.poster_path:
            self._load_image_safe(m.poster_path, self.ui.show_edit_image_label)
        else:
            self._set_label_placeholder(self.ui.show_edit_image_label, "No Image")

        self.ui.stackedWidget.setCurrentIndex(1)  # switch to edit page

    def _exit_edit_mode(self):
        """Return to view mode without saving (restores display)."""
        self.ui.stackedWidget.setCurrentIndex(0)
        # restore the displayed info to ensure consistent UI
        self.refresh_display()

    # ---------------- Edit extraction & validation ----------------
    def _extract_edit_data(self) -> Dict[str, Any]:
        """Read values from edit widgets into a dict (strings only)."""
        data = {
            "title": self.edit_widget_map["title"].text().strip(),
            "runtime": self.edit_widget_map["runtime"].text().strip(),
            "year": self.edit_widget_map["year"].text().strip(),
            "genres": [g.strip() for g in self.edit_widget_map["genres"].text().split(",") if g.strip()],
            "plot": self.edit_widget_map["plot"].text().strip(),
            "rating": self.edit_widget_map["rating"].text().strip(),
            "user_rating": self.edit_widget_map["user_rating"].text().strip(),
            "image_url": self.edit_widget_map["image_url"].text().strip(),
        }
        return data

    def _validate_edit_data(self, data: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """Validate extracted data; return (is_valid, error_message)."""
        if not data["title"]:
            return False, "Title cannot be empty."

        if data["runtime"]:
            try:
                r = int(data["runtime"])
                if r <= 0:
                    return False, "Runtime must be a positive integer."
            except ValueError:
                return False, "Runtime must be a whole number."

        if data["year"]:
            if not (data["year"].isdigit() and len(data["year"]) == 4):
                return False, "Year must be a 4-digit number (e.g., 2024)."

        for key in ("rating", "user_rating"):
            if data[key]:
                try:
                    val = float(data[key])
                    if val < 0 or val > 10:
                        return False, f"{key.replace('_',' ').title()} must be between 0 and 10."
                except ValueError:
                    return False, f"{key.replace('_',' ').title()} must be a number."

        return True, None

    # ---------------- Apply edits ----------------
    def apply_edit(self):
        """Apply changes made in edit mode. Validate, update DB, refresh view, emit signal."""
        if not self.movie:
            QMessageBox.critical(self, "Error", "Movie not loaded.")
            return

        data = self._extract_edit_data()
        valid, err = self._validate_edit_data(data)
        if not valid:
            QMessageBox.warning(self, "Invalid Input", err)
            return

        # Build a changed flag and update fields
        changed = False
        m = self.movie

        if data["title"] != (m.title or ""):
            m.title = data["title"]; changed = True

        # runtime/year/rating conversions
        if data["runtime"]:
            new_runtime = int(data["runtime"])
            if new_runtime != (m.runtime or 0):
                m.runtime = new_runtime; changed = True
        else:
            if m.runtime is not None:
                m.runtime = None; changed = True

        if data["year"]:
            new_year = int(data["year"])
            if new_year != (m.year or 0):
                m.year = new_year; changed = True
        else:
            if m.year is not None:
                m.year = None; changed = True

        if data["plot"] != (m.plot or ""):
            m.plot = data["plot"]; changed = True

        if data["rating"]:
            new_rating = float(data["rating"])
            if new_rating != (m.rating or 0.0):
                m.rating = new_rating; changed = True
        else:
            if m.rating is not None:
                m.rating = None; changed = True

        if data["user_rating"]:
            new_user_rating = float(data["user_rating"])
            if new_user_rating != (m.user_rating or 0.0):
                m.user_rating = new_user_rating; changed = True
        else:
            if m.user_rating is not None:
                m.user_rating = None; changed = True

        if data["genres"] != (m.genres or []):
            m.genres = data["genres"]; changed = True

        if data["image_url"] != (m.poster_path or ""):
            m.poster_path = data["image_url"]; changed = True

        if not changed:
            QMessageBox.information(self, "No Changes", "No changes to save.")
            self._exit_edit_mode()
            return

        # Persist changes
        try:
            update_movie(m)
            self.movie = m
            self.refresh_display()
            self.movie_updated.emit(m)
            QMessageBox.information(self, "Success", "Movie updated successfully.")
            self._exit_edit_mode()
        except Exception as e:
            logger.exception("Failed to update movie %s: %s", self.id, e)
            QMessageBox.critical(self, "Error", f"Failed to update movie: {e}")

    # ---------------- Delete & Move ----------------
    def delete_current_movie(self):
        reply = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this movie?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            return

        try:
            success = delete_movie(self.id)
            if success:
                self.movie_deleted.emit(self.id)
                self.close()
                QMessageBox.information(self, "Deleted", "Movie deleted successfully.")
                
            else:
                QMessageBox.warning(self, "Error", "Failed to delete movie.")
        except Exception as e:
            logger.exception("Failed to delete movie %s: %s", self.id, e)
            QMessageBox.critical(self, "Error", f"Failed to delete movie: {e}")

    def move_to(self):
        if self.ui.move_to_combobox.currentIndex() == -1:
            QMessageBox.warning(self, "Select Section", "Please select a section to move to.")
            return

        new_section = get_selected_section(self.ui.move_to_combobox)
        try:
            success = move_movie_section(self.id, new_section)
            if success:
                self.movie_moved.emit(self.id, new_section)
                QMessageBox.information(self, "Moved", f"Movie moved to {new_section}.")
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Failed to move movie.")
        except Exception as e:
            logger.exception("Failed to move movie %s to %s: %s", self.id, new_section, e)
            QMessageBox.critical(self, "Error", f"Failed to move movie: {e}")

    # ---------------- Plot / Trailer / Watch links ----------------
    def _show_full_plot(self):
        if not self.movie or not self.movie.plot:
            QMessageBox.information(self, "Plot", "No description available.")
            return
        QMessageBox.information(self, "Movie Plot", self.movie.plot)

    def _open_trailer(self):
        if not self.movie or not self.movie.trailer:
            QMessageBox.information(self, "Trailer", "No trailer available.")
            return
        import webbrowser
        webbrowser.open(self.movie.trailer)

    def preview_or_restore_image(self):
        """Preview new image on Enter, or restore old one if field empty."""
        url = self.ui.show_edit_image_url.text().strip()
        if not url:
            if self.original_image_url:
                self._load_image_safe(self.original_image_url, self.ui.show_edit_image_label)
            else:
                self._set_label_placeholder(self.ui.show_edit_image_label, "No Image")
            return

        # Try preview
        self.ui.show_edit_image_label.setText("Loading preview...")
        self._load_image_safe(url, self.ui.show_edit_image_label)
        
    def open_watch_link(self, button: int):
        if not self.movie or not self.movie.title:
            QMessageBox.information(self, "Movie", "Movie title not available.")
            return

        worker = WatchLinkWorker(button, self.movie)
        worker.finished.connect(self._open_url_and_cleanup)
        self.active_workers.append(worker)
        worker.start()

    def _open_url_and_cleanup(self, url):
        # Open the browser safely
        if url:
            import webbrowser
            webbrowser.open(url)
        else:
            QMessageBox.information(self, "No Match", "No match found or failed to retrieve streaming link.")

        # Remove finished worker from list
        sender = self.sender()
        if sender in self.active_workers:
            self.active_workers.remove(sender)
            sender.deleteLater()














# from PySide6.QtCore import Qt,Signal
# from PySide6.QtGui import QCursor, QPixmap
# from py_ui.movies_show import Ui_show
# from PySide6.QtWidgets import QDialog , QMessageBox, QComboBox , QScrollArea,QVBoxLayout,QWidget,QLabel,QGroupBox,QHBoxLayout
# from app.db.movies_db import get_movie_by_id, update_movie, delete_movie, move_movie_section
# from app.utils.my_functions import link_to_image , get_selected_section,resize_combo_box_to_contents
# from app.fetch.movies_info_fetcher import update_imdb_info_if_old
# import webbrowser
# from app.fetch.movies_info_fetcher import ArabSeedScraper, AkwamScraper
# class ClickableLabel(QLabel):
#     clicked = Signal()

#     def mousePressEvent(self, event):
#         self.clicked.emit()
#         super().mousePressEvent(event)


# class ShowMovieWindow(QDialog): # Inherit from QDialog for modal behavior
#     movie_deleted = Signal()
#     movie_moved = Signal()


#     def __init__(self,section,id, parent=None): # Optional parent parameter
#         super().__init__(parent) # Call the parent constructor

#         self.ui = Ui_show() # Create an instance of the UI class
#         self.ui.setupUi(self) # Set up the UI
#         self.setWindowTitle("Movie Details")


#         self.section = section 
#         self.id = id
#         self.movie = None

#         self.show_info()

#         self.ui.show_edit_image_url.returnPressed.connect(self.preview_or_restore_image) # Preview or restore image when Enter is pressed

#         #------------------------- Setup widget -----------------------------

#         self.ui.stackedWidget.setCurrentIndex(0) # Show the first page by default
        

#         #------------------------- Setup Buttons -----------------------------

#         self.ui.show_delete_button.clicked.connect(self.delete_current_movie)
#         self.ui.show_delete_button.setShortcut("del")

#         self.ui.show_edit_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
#         self.ui.show_edit_button.clicked.connect(self.edit)
#         self.ui.show_edit_button.setShortcut("e")

#         self.ui.show_cancel_button.clicked.connect(self.close)
#         self.ui.show_apply_button.clicked.connect(self.move_to)     
#         self.ui.show_edit_apply_button.clicked.connect(self.apply_edit)
         
#         self.ui.show_edit_cancel_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0)) 
#         # This would not work, because setCurrentIndex expects an argument, but the clicked signal doesn't provide one.so we use lambda.

#         self.ui.wahtch_button_1.setText("Watch on Akwam")
#         self.ui.wahtch_button_2.setText("Watch on ArabSeed")
#         self.ui.wahtch_button_2.clicked.connect(lambda: self.show_watch_page(2))
#         self.ui.wahtch_button_1.clicked.connect(lambda: self.show_watch_page(1))

#         #----------------------Setup combobox(move_to) ------------------------

#         # make the long text in the combobox seen
#         self.ui.move_to_combobox.showPopup = lambda: (resize_combo_box_to_contents(self.ui.move_to_combobox),
#                                                       QComboBox.showPopup(self.ui.move_to_combobox))
#         self.comboBox(section)


#     # Slotss:-
#     def move_to(self):
#         "Move selected movie to another section"
#         try:
#             if self.ui.move_to_combobox.currentIndex() != -1: 
#                 new_section = get_selected_section(self.ui.move_to_combobox)
#                 success = move_movie_section(self.id, new_section)
#                 if success:
#                     self.movie_moved.emit()  # Emit signal
#                     print(f"✅ Movie moved to {new_section}")
#                 else:
#                     print("❌ Failed to move movie")
#                 self.close()

#         except Exception as e:
#             print("Error while moving movie:", e)
#             QMessageBox.critical(self, "Error", f"Failed to move movie: {str(e)}")



#     def comboBox(self, except_section):
#         "Fill combobox with all sections except the given one"
#         sections = ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]
#         for section in sections:
#             if section == except_section:
#                 continue
#             else:
#                 self.ui.move_to_combobox.addItem(section.replace("_"," ").capitalize())


#     def get_info(self):
#         "Get movie info by its ID"
#         if not self.movie:
#             self.movie = get_movie_by_id(self.id)
#         return self.movie


#     def show_plot(self, event):
#         "Show movie plot in a message box"
#         movie = self.get_info()
#         if movie and movie.plot:
#             QMessageBox.information(self, "Movie Plot", movie.plot)
#         else:
#             QMessageBox.information(self, "Movie Plot", "No description available.")

#     def show_trailer(self, event):
#         "Show movie trailer in the browser"
#         movie = self.get_info()
#         if movie and movie.trailer:

#             webbrowser.open(movie.trailer)
#         else:
#             QMessageBox.information(self, "Movie trailers", "No trailer available.")

#     def show_watch_page(self,button):
#         "Show watch page in the browser"
#         movie = self.get_info()
#         if movie.title:
#             if button == 2:
#                 scraper = ArabSeedScraper(f"{movie.title} {movie.year}")
#                 url = scraper.watch_url

#             elif button == 1:
#                 scraper = AkwamScraper(f"{movie.title}", movie.year)
#                 url = scraper.watch_url

#             else:
#                 url = None
#         if url:
#             webbrowser.open(url)
#         else:
#             QMessageBox.information(self, "Movie", "No Match found.")



#     def show_info(self):
#         "Display movie info and poster in the UI"
#         movie = self.get_info()
#         if not movie:
#             QMessageBox.critical(self, "Error", "Movie not found!")
#             self.close()
#             return

#         print(f"DEBUG: Movie data - Title: {movie.title}, Year: {movie.year}")  # Debug

#         # Set movie data to labels
#         self.ui.show_name_lable.setText(movie.title or "No title")
#         self.ui.show_time_lable.setText(f"{movie.runtime} min" if movie.runtime else "Runtime not available")
#         self.ui.show_label.setText(str(movie.year) if movie.year else "Year not available")
#         self.ui.show_gener_lable.setText(", ".join(movie.genres) if movie.genres else "No genres")
#         self.original_image_url = movie.poster_path or ""

#         self.ui.show_imdb_rate_lable.setText(str(movie.rating) if movie.rating else "No rating")
#         self.ui.show_user_rate_lable.setText(str(movie.user_rating) if movie.user_rating else "No user rating")

#         # Setup plot label
#         self.ui.plot_widget.setToolTip("Click to see full plot")
#         self.ui.plot_widget.setCursor(QCursor(Qt.PointingHandCursor))
#         self.ui.plot_widget.mousePressEvent = self.show_plot
#         # Setup  trailer lable
#         self.ui.trailer_widget.setToolTip("Click to open trailer")
#         self.ui.trailer_widget.setCursor(QCursor(Qt.PointingHandCursor))
#         self.ui.trailer_widget.mousePressEvent = self.show_trailer


#         # Load image
#         if movie.poster_path:
#             link_to_image(path=movie.poster_path, label=self.ui.show_image_lable, x=180, y=270)
#         else:
#             self.ui.show_image_lable.setText("No Image Available")
#             self.ui.show_image_lable.setAlignment(Qt.AlignCenter)
#             self.ui.show_image_lable.setStyleSheet("color: gray;")




#     def delete_current_movie(self):
#         """Ask for confirmation, delete the movie, and close the window."""
#         reply = QMessageBox.question(
#             self,
#             "Confirm Delete",
#             "Are you sure you want to delete this movie?",
#             QMessageBox.Yes | QMessageBox.No
#         )

#         if reply == QMessageBox.Yes:
#             success = delete_movie(self.id)
#             if success:
#                 self.close()
#                 self.movie_deleted.emit()  # Emit signal
#                 QMessageBox.information(self, "Deleted", "Movie deleted successfully.")
                
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to delete movie.")
    
#     def edit(self):
#         "Load movie data into edit fields and display its poster"
#         movie = self.get_info()
#         if not movie:
#             return

#         self.ui.show_edit_name_line.setText(movie.title or "")
#         self.ui.show_edit_time_line.setText(str(movie.runtime) if movie.runtime else "")
#         self.ui.show_edit_date_line.setText(str(movie.year) if movie.year else "")
#         self.ui.show_edit_gener_line.setText(", ".join(movie.genres) if movie.genres else "")

#         self.ui.show_edit_plot_line.setText(movie.plot or "")

#         self.ui.show_edit_imdb_rate_line.setText(str(movie.rating) if movie.rating else "")
#         self.ui.show_edit_user_rate_line.setText(str(movie.user_rating) if movie.user_rating else "")

#         if movie.poster_path:
#             link_to_image(path=movie.poster_path, label=self.ui.show_edit_image_label, x=180, y=270)
#         else:
#             self.ui.show_edit_image_label.setText("No Image")
#             self.ui.show_edit_image_label.setAlignment(Qt.AlignCenter)
             
#     def apply_edit(self):
#         """Apply changes to the movie in database"""
#         movie = self.get_info()
#         if not movie:
#             QMessageBox.critical(self, "Error", "Movie not found!")
#             return

#         # Collect the new data from UI
#         new_title = self.ui.show_edit_name_line.text().strip()
#         new_runtime = self.ui.show_edit_time_line.text().strip()
#         new_year = self.ui.show_edit_date_line.text().strip()
#         new_plot = self.ui.show_edit_plot_line.text().strip()
#         new_rating = self.ui.show_edit_imdb_rate_line.text().strip()
#         new_user_rating = self.ui.show_edit_user_rate_line.text().strip()
#         new_genres = [g.strip() for g in self.ui.show_edit_gener_line.text().split(",") if g.strip()]
#         new_image_path = self.ui.show_edit_image_url.text().strip()

#         # Update movie object
#         changed = False

#         if new_title != movie.title:
#             movie.title = new_title
#             changed = True

#         if new_runtime and new_runtime != str(movie.runtime or ""):
#             try:
#                 movie.runtime = int(new_runtime)
#                 changed = True
#             except ValueError:
#                 QMessageBox.warning(self, "Invalid Runtime", "Runtime must be a number")
#                 return

#         if new_year and new_year != str(movie.year or ""):
#             try:
#                 movie.year = int(new_year)
#                 changed = True
#             except ValueError:
#                 QMessageBox.warning(self, "Invalid Year", "Year must be a number")
#                 return

#         if new_plot != (movie.plot or ""):
#             movie.plot = new_plot
#             changed = True

#         if new_rating and new_rating != str(movie.rating or ""):
#             try:
#                 movie.rating = float(new_rating)
#                 changed = True
#             except ValueError:
#                 QMessageBox.warning(self, "Invalid Rating", "IMDB Rating must be a number")
#                 return

#         if new_user_rating and new_user_rating != str(movie.user_rating or ""):
#             try:
#                 movie.user_rating = float(new_user_rating)
#                 changed = True
#             except ValueError:
#                 QMessageBox.warning(self, "Invalid Rating", "User Rating must be a number")
#                 return

#         if new_genres != (movie.genres or []):
#             movie.genres = new_genres
#             changed = True

#         if new_image_path and new_image_path != (movie.poster_path or ""):
#             movie.poster_path = new_image_path
#             changed = True

#         # Save only if something changed
#         if changed:
#             try:
#                 update_movie(movie)
#                 self.movie = movie  # Update cached movie
#                 self.show_info()  # Refresh display
#                 QMessageBox.information(self, "Success", "Movie updated successfully!")
#             except Exception as e:
#                 QMessageBox.critical(self, "Error", f"Failed to update movie: {str(e)}")
#         else:
#             QMessageBox.information(self, "No Changes", "No changes were made.")

#         self.ui.stackedWidget.setCurrentIndex(0)


#     def preview_or_restore_image(self):
#         """Preview new image on Enter, or restore old one if field empty."""
#         url = self.ui.show_edit_image_url.text().strip()
#         label = self.ui.show_edit_image_label

#         # If the field is empty → restore the old poster
#         if not url:
#             movie = self.get_info()
#             if movie and movie.poster_path:
#                 link_to_image(movie.poster_path, label, 180, 270)
#             else:
#                 label.setText("No Image")
#                 label.setAlignment(Qt.AlignCenter)
#                 label.setStyleSheet("color: gray;")
#             return

#         # Try to load the new image as preview
#         label.setText("Loading preview...")
#         label.setAlignment(Qt.AlignCenter)
#         link_to_image(url, label, 180, 270)

