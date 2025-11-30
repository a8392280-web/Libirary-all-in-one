# show_movie_window.py
import logging
from typing import Optional, Dict, Any, Tuple

from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtGui import QCursor, QPixmap, QColor, QPainter, QKeySequence,QShortcut
from PySide6.QtWidgets import (
    QDialog, QMessageBox, QComboBox, QLabel, QWidget, QVBoxLayout
)
from py_ui.movies_show import Ui_show
from app.db.movies_db import get_movie_by_id, update_movie, delete_movie, move_movie_section
from app.utils.my_functions import link_to_image, get_selected_section, resize_combo_box_to_contents
from app.fetch.movies_info_fetcher import ArabSeedScraper, AkwamScraper
from app.models.movie import Movie


logger = logging.getLogger(__name__)


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
            "imdb_rating": self.ui.show_edit_imdb_rate_line,
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
        self.ui.show_imdb_rate_lable.setText(str(movie.imdb_rating) if movie.imdb_rating else "No rating")
        self.ui.show_user_rate_lable.setText(str(movie.user_rating) if movie.user_rating else "No user rating")
        self.ui.imdb_votes.setText(str(movie.imdb_votes) if movie.imdb_votes else "No votes")
        self.ui.tmdb_rate.setText(str(movie.tmdb_rating) if movie.tmdb_rating else "No rating")
        self.ui.tmdb_votes.setText(str(movie.tmdb_votes) if movie.tmdb_votes else "No votes")
        self.ui.rotten_tomatos_rate.setText(str(movie.rotten_tomatoes) if movie.rotten_tomatoes else "No  rating")
        self.ui.metascore_rate.setText(str(movie.metascore) if movie.metascore else "No score")
        self.display_cast(self.ui.cast_layout,movie.cast,self._load_image_safe)

        
        name, url = movie.director.split(", ", 1)
        self._load_image_safe(url, self.ui.director_label)
        self.ui.director_name.setText(str(name) if name else "Director Name Unknown")


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
        self.edit_widget_map["imdb_rating"].setText(str(m.imdb_rating) if m.imdb_rating is not None else "")
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
            "imdb_rating": self.edit_widget_map["imdb_rating"].text().strip(),
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

        for key in ("imdb_rating", "user_rating"):
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

        if data["imdb_rating"]:
            new_rating = float(data["imdb_rating"])
            if new_rating != (m.imdb_rating or 0.0):
                m.imdb_rating = new_rating; changed = True
        else:
            if m.imdb_rating is not None:
                m.imdb_rating = None; changed = True

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
        """ for find tag links"""
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



    def display_cast(self, cast_layout, cast_list, load_image_safe_func):
        """
        for the cast:-
        Populate a QHBoxLayout with cast members in a visually appealing way.
        """
        # Clear previous widgets
        while cast_layout.count():
            item = cast_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for actor in cast_list:
            actor_widget = QWidget()
            actor_widget.setStyleSheet("""
                QWidget {
                    background-color: #1f2733;
                    border-radius: 8px;
                    padding: 5px;
                }
            """)
            actor_widget.setFixedWidth(140)

            v_layout = QVBoxLayout(actor_widget)
            v_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            v_layout.setContentsMargins(5,5,5,5)
            v_layout.setSpacing(5)

            # Image
            img_label = QLabel()
            img_label.setFixedSize(120, 180)
            img_label.setStyleSheet("border-radius: 6px;")
            load_image_safe_func(actor.get("profile"), img_label, width=120, height=180)

            # Name
            name_label = QLabel(actor.get("name", "Unknown"))
            name_label.setAlignment(Qt.AlignCenter)
            name_label.setWordWrap(True)
            name_label.setStyleSheet("font-weight: bold; font-size: 12px; color: #fff;")

            # Character
            char_label = QLabel(actor.get("character", ""))
            char_label.setAlignment(Qt.AlignCenter)
            char_label.setWordWrap(True)
            char_label.setStyleSheet("font-size: 11px; color: #ccc;")

            v_layout.addWidget(img_label)
            v_layout.addWidget(name_label)
            v_layout.addWidget(char_label)

            cast_layout.addWidget(actor_widget)

        cast_layout.addStretch()

