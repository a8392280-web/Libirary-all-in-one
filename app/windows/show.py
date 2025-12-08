# show_media_window.py
"""
Unified ShowMediaWindow:
- Works for movies and series (media_type = "movies" | "series")
- Uses a single merged UI (assumes you merged movies/series UI and didn't rename objects)
- Consolidates duplicated logic and provides clear comments for maintainability
"""

import logging
from typing import Optional, Dict, Any, Tuple, Callable, List

from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtGui import QCursor, QPixmap, QColor, QPainter, QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QDialog, QMessageBox, QComboBox, QLabel, QWidget, QVBoxLayout, QGroupBox, QHBoxLayout
)

# Import DB functions and models for both media types
from app.db.movies_db import get_movie_by_id, update_movie, delete_movie, move_movie_section
from app.db.series_db import get_series_by_id, update_series, delete_series, move_series_section

from app.utils.my_functions import link_to_image, get_selected_section, resize_combo_box_to_contents
from app.fetch.movies_info_fetcher import ArabSeedScraper, AkwamScraper
from app.models.movie import Movie
from app.models.series import Series

from py_ui.show import Ui_show 


logger = logging.getLogger(__name__)


class WatchLinkWorker(QThread):
    """
    Worker that uses scrapers to find watch links.
    Kept mostly for movies use — it's harmless to exist for series but we only call it when media_type == 'movies'.
    """
    finished = Signal(str)  # emits URL or None

    def __init__(self, button: int, movie: Movie):
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
            logger.warning("WatchLinkWorker scraper failed: %s", e)
            url = None
        self.finished.emit(url)


class ClickableLabel(QLabel):
    """Simple clickable QLabel for plot/trailer/episode interactions"""
    clicked = Signal()
    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)


class ShowMediaWindow(QDialog):
    """
    Unified window for Movies and Series.

    Usage:
        ShowMediaWindow(media_type="movies", section="watching", item_id=123)
        ShowMediaWindow(media_type="series", section="watched", item_id=456)

    Notes:
    - Assumes merged UI exists and object names are the same as before (per your message).
    - Emits generic signals so parent UI can update lists without full reload.
    """

    # Generic signals (media_type kept in payload if parent needs it)
    item_deleted = Signal(str, int)        # media_type, id
    item_moved = Signal(str, int, str)     # media_type, id, new_section
    item_updated = Signal(str, object)     # media_type, model_object

    def __init__(self, media_type: str, section: str, item_id: int, parent=None):
        """
        media_type: "movies" or "series"
        section: current section name (e.g., "watching")
        item_id: database id
        """
        super().__init__(parent)

        # Accept only known types for safety; easy to extend
        if media_type not in ("movies", "series"):
            raise ValueError("media_type must be 'movies' or 'series'")

        self.media_type = media_type
        self.section = section
        self.id = item_id

        # Setup UI: choose the correct Ui_show class depending on what was merged.
        # If your merged UI uses one file, replace logic here to import that single Ui_show.
        # We'll attempt to instantiate either Ui_show (movies) or Ui_show (series) — both have same object names.
        # Prefer the movies UI module by default then series as fallback if needed.
  
        self.ui = Ui_show()
        self.ui.setupUi(self)
        #------------------------------

        index_tab2 = self.ui.tabWidget.indexOf(self.ui.tab_2)
        index_tab3 = self.ui.tabWidget.indexOf(self.ui.tab_3)

        if media_type == "movies":
            self.ui.tabWidget.removeTab(index_tab2)
        else:
            self.ui.tabWidget.removeTab(index_tab3)





        #------------------------------


        self.setWindowTitle("Item Details")

        # runtime objects
        self.active_workers: List[QThread] = []
        self.item: Optional[object] = None  # Movie or Series
        self.original_image_url: str = ""

        # map field names to edit widget names (UI uses same names in both UIs)
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

        # DB and update functions per media type
        self._bind_db_functions()

        # Setup UI wiring
        self._setup_buttons_and_shortcuts()
        self._setup_move_combobox()
        self._connect_signals()

        # Load item (movies or series)
        self._load_item()

    # -----------------------------
    # DB binding (choose correct functions per media_type)
    # -----------------------------
    def _bind_db_functions(self):
        if self.media_type == "movies":
            self._get_item_by_id = get_movie_by_id
            self._update_item = update_movie
            self._delete_item = delete_movie
            self._move_section = move_movie_section
            self._model_cls = Movie
        else:
            self._get_item_by_id = get_series_by_id
            self._update_item = update_series
            self._delete_item = delete_series
            self._move_section = move_series_section
            self._model_cls = Series

    # -----------------------------
    # UI setup helpers
    # -----------------------------
    def _setup_buttons_and_shortcuts(self):
        # guard against accidental default activation
        for btn in (
            getattr(self.ui, 'show_delete_button', None),
            getattr(self.ui, 'show_edit_button', None),
            getattr(self.ui, 'show_cancel_button', None),
            getattr(self.ui, 'show_apply_button', None),
            getattr(self.ui, 'show_edit_apply_button', None),
            getattr(self.ui, 'show_edit_cancel_button', None),
            getattr(self.ui, 'watch_button_1', None),
            getattr(self.ui, 'watch_button_2', None),
            getattr(self.ui, 'watch_button_3', None),
        ):
            if btn is None:
                continue
            try:
                btn.setAutoDefault(False)
                btn.setDefault(False)
            except Exception:
                pass

        # shortcuts
        try:
            self.ui.show_delete_button.setShortcut("Del")
            self.ui.show_edit_button.setShortcut("E")
        except Exception:
            pass

        QShortcut(QKeySequence("Esc"), self, activated=self._exit_edit_mode)
        QShortcut(QKeySequence("Ctrl+S"), self, activated=self.apply_edit)

    def _setup_move_combobox(self):
        # populate move-to combobox excluding current section
        try:
            self.ui.move_to_combobox.clear()
            sections = ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]
            for sec in sections:
                if sec == self.section:
                    continue
                self.ui.move_to_combobox.addItem(sec.replace("_", " ").capitalize())

            # dynamic resize when showing popup
            if hasattr(self.ui.move_to_combobox, "showPopup"):
                self.ui.move_to_combobox.showPopup = lambda: (
                    resize_combo_box_to_contents(self.ui.move_to_combobox),
                    QComboBox.showPopup(self.ui.move_to_combobox)
                )
        except Exception:
            logger.debug("Move combobox not present or failed to setup; skipping.")

    def _connect_signals(self):
        # main actions
        try:
            self.ui.show_delete_button.clicked.connect(self.delete_current_item)
            self.ui.show_edit_button.clicked.connect(self.enter_edit_mode)
            self.ui.show_cancel_button.clicked.connect(self.close)
            self.ui.show_apply_button.clicked.connect(self.move_to)
            self.ui.show_edit_apply_button.clicked.connect(self.apply_edit)
            self.ui.show_edit_cancel_button.clicked.connect(self._exit_edit_mode)
        except Exception:
            logger.debug("Some main UI buttons are missing; continuing setup.")

        # watch buttons (movies only) — they may exist in the merged UI
        try:
            if self.media_type == "movies":
                self.ui.watch_button_1.setText("Watch on Akwam")
                self.ui.watch_button_2.setText("Watch on ArabSeed")
                self.ui.watch_button_3.setText("Watch on Cineby")
                self.ui.watch_button_1.clicked.connect(lambda: self.open_watch_link(1))
                self.ui.watch_button_2.clicked.connect(lambda: self.open_watch_link(2))
                self.ui.watch_button_3.clicked.connect(lambda: self.open_watch_link(3))
            else:
                # hide or disable watch buttons for non-movie types if desired
                try:
                    self.ui.watch_button_1.setVisible(False)
                    self.ui.watch_button_2.setVisible(False)
                    self.ui.watch_button_3.setVisible(False)
                except Exception:
                    pass
        except Exception:
            logger.debug("Watch buttons not present in UI.")

        # clickable plot/trailer
        try:
            self.ui.plot_widget.clicked.connect(self._show_full_plot)
        except Exception:
            try:
                self.ui.plot_widget.mousePressEvent = lambda _: self._show_full_plot()
            except Exception:
                pass

        try:
            self.ui.trailer_widget.clicked.connect(self._open_trailer)
        except Exception:
            try:
                self.ui.trailer_widget.mousePressEvent = lambda _: self._open_trailer()
            except Exception:
                pass

        # preview image on Enter in edit field
        try:
            self.ui.show_edit_image_url.returnPressed.connect(self.preview_or_restore_image)
        except Exception:
            pass

    # -----------------------------
    # Load & refresh
    # -----------------------------
    def _load_item(self):
        """Fetch item from DB and refresh UI. Robust error handling."""
        try:
            self.item = self._get_item_by_id(self.id)
        except Exception as e:
            logger.exception("Failed to fetch %s by id %s: %s", self.media_type, self.id, e)
            QMessageBox.critical(self, "Error", f"Failed to load item: {e}")
            self.close()
            return

        if not self.item:
            QMessageBox.critical(self, "Error", f"{self.media_type.capitalize()} not found.")
            self.close()
            return

        # cache original image url
        self.original_image_url = getattr(self.item, "poster_path", "") or ""

        # refresh UI with loaded data
        self.refresh_display()

    def refresh_display(self):
        """Populate view UI with current item data."""
        item = self.item
        if not item:
            return

        # common fields
        try:
            self.ui.show_name_lable.setText(item.title or "No title")
        except Exception:
            pass

        try:
            self.ui.show_time_lable.setText(f"{item.runtime} min" if getattr(item, "runtime", None) else "Runtime not available")
        except Exception:
            pass

        try:
            self.ui.show_label.setText(str(item.year) if getattr(item, "year", None) else "Year not available")
        except Exception:
            pass

        try:
            self.ui.show_gener_lable.setText(", ".join(item.genres) if getattr(item, "genres", None) else "No genres")
        except Exception:
            pass

        try:
            self.ui.show_imdb_rate_lable.setText(str(item.imdb_rating) if getattr(item, "imdb_rating", None) else "No rating")
            self.ui.show_user_rate_lable.setText(str(item.user_rating) if getattr(item, "user_rating", None) else "No user rating")
            self.ui.imdb_votes.setText(str(getattr(item, "imdb_votes", "")) or "No votes")
            self.ui.tmdb_rate.setText(str(getattr(item, "tmdb_rating", "")) or "No rating")
            self.ui.tmdb_votes.setText(str(getattr(item, "tmdb_votes", "")) or "No votes")
            self.ui.rotten_tomatos_rate.setText(str(getattr(item, "rotten_tomatoes", "")) or "No  rating")
            self.ui.metascore_rate.setText(str(getattr(item, "metascore", "")) or "No score")
        except Exception:
            pass

        # cast
        try:
            self.display_cast(self.ui.cast_layout, getattr(item, "cast", []) or [], self._load_image_safe)
        except Exception:
            logger.debug("Failed to display cast for item %s", self.id)

        # media-specific: director vs creator
        try:
            if self.media_type == "movies":
                # movie.director expected format "Name, image_url"
                if getattr(item, "director", None):
                    try:
                        name, url = item.director.split(", ", 1)
                        self._load_image_safe(url, self.ui.director_label)
                        self.ui.director_name.setText(str(name) if name else "Director Name Unknown")
                    except Exception:
                        self.ui.director_name.setText(str(item.director) or "Director Unknown")
            else:
                if getattr(item, "creator", None):
                    try:
                        name, url = item.creator.split(",", 1)
                        self._load_image_safe(url, self.ui.director_label)
                        self.ui.director_name.setText(str(name) if name else "Creator Name Unknown")
                    except Exception:
                        self.ui.director_name.setText(str(item.creator) or "Creator Unknown")
        except Exception:
            pass

        # series-specific UI: seasons
        try:
            if self.media_type == "series":
                # add seasons widget if present
                self.add_seasons(getattr(item, "seasons", []))
        except Exception:
            pass

        # plot and trailer tooltips
        try:
            self.ui.plot_widget.setToolTip("Click to see full plot")
            self.ui.plot_widget.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.trailer_widget.setToolTip("Click to open trailer")
            self.ui.trailer_widget.setCursor(QCursor(Qt.PointingHandCursor))
        except Exception:
            pass

        # poster image
        try:
            poster = getattr(item, "poster_path", None)
            if poster:
                self._load_image_safe(poster, self.ui.show_image_lable)
            else:
                self._set_label_placeholder(self.ui.show_image_lable, "No Image Available")
        except Exception:
            pass

    # -----------------------------
    # Image helpers
    # -----------------------------
    def _load_image_safe(self, url: str, label: QLabel, width=180, height=270) -> None:
        """Try to load image with link_to_image; fallback to placeholder on failure."""
        if not url:
            self._set_label_placeholder(label, "No Image")
            return
        try:
            link_to_image(path=url, label=label, x=width, y=height)
        except Exception as e:
            logger.warning("Failed to load image %s: %s", url, e)
            self._set_label_placeholder(label, "No Image")

    def _set_label_placeholder(self, label: QLabel, text="No Image", width=180, height=270) -> None:
        try:
            label.setPixmap(self._placeholder_pixmap(width, height))
            label.setAlignment(Qt.AlignCenter)
            label.setToolTip(text)
        except Exception:
            pass

    def _placeholder_pixmap(self, width=180, height=270) -> QPixmap:
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor("#444"))
        painter = QPainter(pixmap)
        painter.setPen(QColor("#ccc"))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "No Image")
        painter.end()
        return pixmap

    # -----------------------------
    # Edit mode
    # -----------------------------
    def enter_edit_mode(self):
        """Fill edit fields and switch to edit page."""
        if not self.item:
            QMessageBox.warning(self, "No item", "Item not loaded.")
            return

        it = self.item
        try:
            self.edit_widget_map["title"].setText(it.title or "")
            self.edit_widget_map["runtime"].setText(str(it.runtime) if getattr(it, "runtime", None) is not None else "")
            self.edit_widget_map["year"].setText(str(it.year) if getattr(it, "year", None) is not None else "")
            self.edit_widget_map["genres"].setText(", ".join(it.genres) if getattr(it, "genres", None) else "")
            self.edit_widget_map["plot"].setText(it.plot or "")
            self.edit_widget_map["imdb_rating"].setText(str(it.imdb_rating) if getattr(it, "imdb_rating", None) is not None else "")
            self.edit_widget_map["user_rating"].setText(str(it.user_rating) if getattr(it, "user_rating", None) is not None else "")
            self.edit_widget_map["image_url"].setText(getattr(it, "poster_path", "") or "")
        except Exception:
            pass

        # preview image in edit label
        try:
            if getattr(it, "poster_path", None):
                self._load_image_safe(it.poster_path, self.ui.show_edit_image_label)
            else:
                self._set_label_placeholder(self.ui.show_edit_image_label, "No Image")
        except Exception:
            pass

        try:
            self.ui.stackedWidget.setCurrentIndex(1)
        except Exception:
            pass

    def _exit_edit_mode(self):
        """Return to view mode (discard unsaved edits) and refresh display."""
        try:
            self.ui.stackedWidget.setCurrentIndex(0)
        except Exception:
            pass
        self.refresh_display()

    # -----------------------------
    # Edit extraction & validation
    # -----------------------------
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
        """Shared validation for both movies and series."""
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

    # -----------------------------
    # Apply edits (persist)
    # -----------------------------
    def apply_edit(self):
        """Apply changes, validate, persist and emit update."""
        if not self.item:
            QMessageBox.critical(self, "Error", "Item not loaded.")
            return

        data = self._extract_edit_data()
        valid, err = self._validate_edit_data(data)
        if not valid:
            QMessageBox.warning(self, "Invalid Input", err)
            return

        obj = self.item
        changed = False

        # Helper to update any attribute cleanly
        def _update_field(attr, new_value, cast=None):
            nonlocal changed
            old_value = getattr(obj, attr, None)

            if cast and new_value not in ("", None):
                try:
                    new_value = cast(new_value)
                except ValueError:
                    return

            # Normalize empty fields into None
            if new_value in ("", None):
                new_value = None

            if new_value != old_value:
                setattr(obj, attr, new_value)
                changed = True

        # mapping of UI → object attr → cast type
        field_map = {
            "title": ("title", str),
            "runtime": ("runtime", int),
            "year": ("year", int),
            "plot": ("plot", str),
            "imdb_rating": ("imdb_rating", float),
            "user_rating": ("user_rating", float),
            "genres": ("genres", None),
            "image_url": ("poster_path", str),
        }

        # Apply updates dynamically
        for key, (attr, cast) in field_map.items():
            _update_field(attr, data.get(key), cast)

        if not changed:
            QMessageBox.information(self, "No Changes", "No changes to save.")
            self._exit_edit_mode()
            return

        # Persist
        try:
            self._update_item(obj)
            self.item = obj
            self.refresh_display()

            self.item_updated.emit(self.media_type, obj)

            QMessageBox.information(
                self,
                "Success",
                f"{self.media_type.capitalize()} updated successfully."
            )

            self._exit_edit_mode()

        except Exception as e:
            logger.exception("Failed to update %s %s: %s", self.media_type, self.id, e)
            QMessageBox.critical(self, "Error", f"Failed to update {self.media_type}: {e}")


    # -----------------------------
    # Delete & Move
    # -----------------------------
    def delete_current_item(self):
        reply = QMessageBox.question(self, "Confirm Delete",
                                     f"Are you sure you want to delete this {self.media_type}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            return

        try:
            success = self._delete_item(self.id)
            if success:
                # emit event for parent
                self.item_deleted.emit(self.media_type, self.id)
                self.close()
                QMessageBox.information(self, "Deleted", f"{self.media_type.capitalize()} deleted successfully.")
            else:
                QMessageBox.warning(self, "Error", f"Failed to delete {self.media_type}.")
        except Exception as e:
            logger.exception("Failed to delete %s %s: %s", self.media_type, self.id, e)
            QMessageBox.critical(self, "Error", f"Failed to delete {self.media_type}: {e}")



    def move_to(self):
        try:
            if self.ui.move_to_combobox.currentIndex() == -1:
                QMessageBox.warning(self, "Select Section", "Please select a section to move to.")
                return
        except Exception:
            QMessageBox.warning(self, "Select Section", "Please select a section to move to.")
            return

        new_section = get_selected_section(self.ui.move_to_combobox)
        try:
            success = self._move_section(self.id, new_section)
            if success:
                self.item_moved.emit(self.media_type, self.id, new_section)
                QMessageBox.information(self, "Moved", f"{self.media_type.capitalize()} moved to {new_section}.")
                self.close()
            else:
                QMessageBox.warning(self, "Error", f"Failed to move {self.media_type}.")
        except Exception as e:
            logger.exception("Failed to move %s %s to %s: %s", self.media_type, self.id, new_section, e)
            QMessageBox.critical(self, "Error", f"Failed to move {self.media_type}: {e}")

    # -----------------------------
    # Plot / Trailer / Watch
    # -----------------------------
    def _show_full_plot(self):
        if not self.item or not getattr(self.item, "plot", None):
            QMessageBox.information(self, "Plot", "No description available.")
            return
        QMessageBox.information(self, f"{self.media_type.capitalize()} Plot", self.item.plot)

    def _open_trailer(self):
        if not self.item or not getattr(self.item, "trailer", None):
            QMessageBox.information(self, "Trailer", "No trailer available.")
            return
        import webbrowser
        webbrowser.open(self.item.trailer)

    def preview_or_restore_image(self):
        """Preview image when editing; restore to original if blank."""
        try:
            url = self.ui.show_edit_image_url.text().strip()
        except Exception:
            url = ""

        if not url:
            if self.original_image_url:
                self._load_image_safe(self.original_image_url, self.ui.show_edit_image_label)
            else:
                self._set_label_placeholder(self.ui.show_edit_image_label, "No Image")
            return

        # Try preview
        try:
            self.ui.show_edit_image_label.setText("Loading preview...")
        except Exception:
            pass
        self._load_image_safe(url, self.ui.show_edit_image_label)

    # Movies-only: open watch link via worker
    def open_watch_link(self, button: int):
        if self.media_type != "movies":
            QMessageBox.information(self, "Watch", "Watch links are available for movies only.")
            return
        if not self.item or not getattr(self.item, "title", None):
            QMessageBox.information(self, "Movie", "Movie title not available.")
            return
        worker = WatchLinkWorker(button, self.item)
        worker.finished.connect(self._open_url_and_cleanup)
        self.active_workers.append(worker)
        worker.start()

    def _open_url_and_cleanup(self, url):
        if url:
            import webbrowser
            webbrowser.open(url)
        else:
            QMessageBox.information(self, "No Match", "No match found or failed to retrieve streaming link.")

        # remove worker
        sender = self.sender()
        if sender in self.active_workers:
            self.active_workers.remove(sender)
            sender.deleteLater()

    # -----------------------------
    # Cast rendering (shared)
    # -----------------------------
    def display_cast(self, cast_layout, cast_list, load_image_safe_func: Callable):
        """
        Populate a cast layout with member cards.
        Reuses same style for movies and series.
        """
        # clear previous
        while cast_layout.count():
            item = cast_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for actor in (cast_list or []):
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

    # -----------------------------
    # Series-specific: seasons (kept close to original)
    # -----------------------------
    def add_seasons(self, seasons: Optional[list]):
        """
        Render seasons and episodes for series.
        Skips season 0 (specials) and seasons with zero episodes.
        """
        if not seasons or self.media_type != "series":
            return

        # Attempt to remove previously added season boxes (if UI is reused)
        try:
            # if you used a dedicated container for seasons (e.g., self.ui.main_layout), clear it first.
            # We'll attempt to remove group boxes with objectName "seasonBox" if present.
            # (This keeps behavior similar to your original code.)
            # NOTE: If your merged UI uses a different container, adjust accordingly.
            # We won't strictly rely on self.ui.main_layout; we'll try both.
            parent_layout = getattr(self.ui, "main_layout", None)
            if parent_layout:
                # remove existing season group boxes (by iterating widgets)
                # naive clear: remove all QGroupBox children added previously
                # caution: don't remove other permanent widgets unintentionally
                # We'll simply proceed to add new boxes; if duplicates occur you can clear in UI before calling.
                pass
        except Exception:
            pass

        # icons (resource paths)
        eye_normal = ":/icons/Icons/eye.png"
        eye_seen = ":/icons/Icons/eye 1.png"

        def create_episode_widget(ep_number: int):
            ep_widget = QWidget()
            ep_layout = QHBoxLayout(ep_widget)
            ep_layout.setContentsMargins(5, 2, 5, 2)

            ep_label = QLabel(f"Episode {ep_number}")
            ep_layout.addWidget(ep_label)
            ep_layout.addStretch()

            eye_label = ClickableLabel()
            eye_label.current_icon = eye_normal
            try:
                eye_label.setPixmap(QPixmap(eye_normal).scaled(18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            except Exception:
                pass

            def toggle(lbl=eye_label):
                lbl.current_icon = eye_seen if lbl.current_icon == eye_normal else eye_normal
                try:
                    lbl.setPixmap(QPixmap(lbl.current_icon).scaled(18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                except Exception:
                    pass

            eye_label.clicked.connect(toggle)
            ep_layout.addWidget(eye_label)

            return ep_widget

        # Add season boxes to a container in the merged UI.
        # We'll attempt to use self.ui.main_layout (as in original series file). If not found, try a sensible fallback.
        container_layout = getattr(self.ui, "main_layout", None)
        if container_layout is None:
            # try another common name
            container_layout = getattr(self.ui, "seasons_layout", None)

        if container_layout is None:
            logger.debug("No seasons container found in UI; skipping adding season boxes.")
            return

        for season in seasons:
            # Skip specials
            if season.get("season_number") == 0:
                continue

            episode_count = season.get("episode_count", 0)
            if episode_count == 0:
                continue

            name = season.get("season_name", f"Season {season.get('season_number')}")
            air_date = season.get("air_date") or ""
            title = f"{name} ({air_date})" if air_date else name

            season_box = QGroupBox(title)
            season_layout = QVBoxLayout()
            season_layout.setSpacing(6)

            for ep in range(1, episode_count + 1):
                season_layout.addWidget(create_episode_widget(ep))

            season_box.setLayout(season_layout)

            # Add to UI container
            try:
                container_layout.addWidget(season_box)
            except Exception:
                logger.debug("Failed to add season box to container; container is not a layout.")

