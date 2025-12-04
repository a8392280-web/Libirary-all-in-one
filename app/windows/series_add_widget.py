from PySide6.QtWidgets import QDialog, QMessageBox, QComboBox
from PySide6.QtCore import Signal, Qt, QThread
from PySide6.QtGui import QPixmap, QColor, QPainter
from py_ui.series_add import Ui_add_widget
from app.db.series_db import insert_series, list_series
from app.utils.my_functions import link_to_image, get_selected_section, resize_combo_box_to_contents
from app.fetch.series_info_fetcher import get_series_info
from app.models.series import Series


# ---------------- Worker Thread ----------------
class SeriesFetchWorker(QThread):
    finished = Signal(dict)
    failed = Signal(str)

    def __init__(self, series_name: str):
        super().__init__()
        self.series_name = series_name

    def run(self):
        try:
            result = get_series_info(self.series_name)
            if not result or result == "no":
                self.failed.emit("no")
            elif result == "not series":
                self.failed.emit("not series")
            else:
                self.finished.emit(result)
        except Exception as e:
            self.failed.emit(str(e))


# ---------------- Main Window ----------------
class AddSeriesWindow(QDialog):
    series_added = Signal(Series)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Add New show")

        self.series_info = None  # fetched series data
        self.data = {sec: list_series(sec) for sec in
                     ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]}

        self.setup_ui()
        self.setup_signals()

    # ---------------- UI Setup ----------------
    def setup_ui(self):
        # Section ComboBox
        self.ui.section_selector.clear()
        sections = ["Watching", "Want_to_watch", "Continue_later", "Dont_want_to_continue", "Watched"]
        self.ui.section_selector.addItems([s.replace("_", " ").capitalize() for s in sections])
        self.ui.section_selector.showPopup = lambda: (
            resize_combo_box_to_contents(self.ui.section_selector),
            QComboBox.showPopup(self.ui.section_selector)
        )

        # Disable auto-default for buttons
        for btn_name in ["apply_button", "cancel_button", "search_button"]:
            btn = getattr(self.ui, btn_name, None)
            if btn:
                btn.setAutoDefault(False)
                btn.setDefault(False)

    def setup_signals(self):
        if hasattr(self.ui, "cancel_button"):
            self.ui.cancel_button.clicked.connect(self.close)
        if hasattr(self.ui, "apply_button"):
            self.ui.apply_button.clicked.connect(self.add_series_entry)
        if hasattr(self.ui, "search_button"):
            self.ui.search_button.clicked.connect(self.search_and_show)

    # ---------------- Image Handling ----------------
    def load_image(self, url: str, label, width=180, height=270):
        if not url:
            label.setPixmap(self.get_placeholder_pixmap(width, height))
            return
        try:
            link_to_image(url, label, width, height)
        except Exception:
            label.setPixmap(self.get_placeholder_pixmap(width, height))

    def get_placeholder_pixmap(self, width, height):
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor("#444"))
        painter = QPainter(pixmap)
        painter.setPen(QColor("#ccc"))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "No Image")
        painter.end()
        return pixmap

    # ---------------- Extract & Merge Data ----------------
    def extract_series_data(self):
        """Extract user input from UI fields."""
        return {
            "section": get_selected_section(self.ui.section_selector),
            "title": self.ui.name_input.text().strip(),
            "runtime": self.ui.time_input.text().strip(),
            "year": self.ui.date_input.text().strip(),
            "imdb_rating": self.ui.imdb_rate_input.text().strip(),
            "user_rating": self.ui.user_rate_input.text().strip(),
            "plot": self.ui.plot_input.text().strip(),
            "genres": [g.strip() for g in self.ui.gener_input.text().split("-") if g.strip()],
            "poster_path": self.ui.image_url_input.text().strip() or (self.series_info.get("Image") if self.series_info else None),
            "trailer": self.ui.trailer_input.text().strip(),
            "total_seasons": self.ui.seasons_input.text().strip(),
            "total_episodes": self.ui.episodes_input.text().strip(),
        }

    def merge_series_data(self, extracted: dict) -> dict:
        """Merge extracted user data with fetched series info."""
        if not self.series_info:
            self.series_info = {}

        data = self.series_info.copy()
        data.update({
            "name": extracted.get("title"),
            "year": extracted.get("year"),
            "runtime": extracted.get("runtime"),
            "plot": extracted.get("plot"),
            "genres": extracted.get("genres"),
            "image": extracted.get("poster_path"),
            "trailer": extracted.get("trailer"),
            "user_rating": extracted.get("user_rating"),
            "imdb_rating": extracted.get("imdb_rating"),
            "section": extracted.get("section"),
            "total_seasons": extracted.get("total_seasons"),
            "total_episodes": extracted.get("total_episodes")
        })

        return data

    # ---------------- Add series ----------------
    def add_series_entry(self):
        try:
            extracted = self.extract_series_data()
            data = self.merge_series_data(extracted)
            print(data)

            self.validate_series_data(data)

            duplicate_section = self.check_duplicate(data["name"])
            if duplicate_section:
                reply = QMessageBox.question(
                    self, "Confirm Adding",
                    f"There is a series with this name ({data['name']}) in the ({duplicate_section.replace('_',' ')}) section.\n"
                    "Are you sure you want to add it again?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.No:
                    QMessageBox.information(self, "Add Canceled", "Series was not added.", QMessageBox.Ok)
                    return

            self.insert_series_data(data)
            self.close()
            QMessageBox.information(self, "Success", f"'{data['name']}' was added successfully!", QMessageBox.Ok)

        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", str(e), QMessageBox.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected error: {str(e)}", QMessageBox.Ok)

    # ---------------- Validation ----------------
    def validate_series_data(self, data: dict):
        if not data["name"]:
            raise ValueError("Series name cannot be empty.")
        if not data["section"]:
            raise ValueError("Please select a section for the series.")

        for key in ["imdb_rating", "user_rating"]:
            if data.get(key):
                try:
                    val = float(data[key])
                    if val < 0 or val > 10:
                        raise ValueError(f"{key.replace('_',' ').title()} must be between 0 and 10.")
                except ValueError:
                    raise ValueError(f"{key.replace('_',' ').title()} must be a number (e.g., 7.5)")

        if data.get("runtime"):
            try:
                if int(data["runtime"]) <= 0:
                    raise ValueError("Runtime must be a positive number.")
            except ValueError:
                raise ValueError("Runtime must be a whole number (e.g., 120).")

        if data.get("year") and (len(data["year"]) != 4 or not data["year"].isdigit()):
            raise ValueError("Year must be exactly 4 digits (e.g., 2024).")

    # ---------------- Duplicate Check ----------------
    def check_duplicate(self, title: str):
        title_lower = title.strip().lower()
        for section, series in self.data.items():
            for serie in series:
                if serie.title.strip().lower() == title_lower:
                    return section
        return None

    # ---------------- Insert Series ----------------
    def insert_series_data(self, data: dict):
        series = Series(
            title=data["name"],
            runtime=int(data["runtime"]) if data.get("runtime") else None,
            year=data.get("year"),
            imdb_rating=float(data["imdb_rating"]) if data.get("imdb_rating") else None,
            user_rating=float(data["user_rating"]) if data.get("user_rating") else None,
            poster_path=data.get("image"),
            plot=data.get("plot"),
            genres=data.get("genres"),
            imdb_id=data.get("imdb_id"),
            tmdb_id=data.get("tmdb_id"),
            section=data.get("section"),
            trailer=data.get("trailer"),
            cast= data.get("cast"),
            creator= data.get("creator"),
            tmdb_rating= data.get("tmdb_rating"),
            tmdb_votes= data.get("tmdb_votes"),
            imdb_votes= data.get("imdb_votes"),
            rotten_tomatoes= data.get("rotten_tomatoes"),
            metascore= data.get("metascore"),
            total_seasons=data.get("total_seasons"),
            total_episodes=data.get("total_episodes"),
            seasons=data.get("seasons")
        )

        insert_series(series)
        self.series_added.emit(series)

    # # ---------------- Display series Info ----------------
    def display_series_info(self, series_info: dict):
        self.ui.name_input.setText(series_info.get("name", ""))
        self.ui.time_input.setText(str(series_info.get("runtime", "")))
        self.ui.date_input.setText(series_info.get("year", ""))
        self.ui.gener_input.setText("-".join(series_info.get("genres", [])))
        self.ui.imdb_rate_input.setText(str(series_info.get("imdb_rating", "")))
        self.ui.user_rate_input.setText(str(series_info.get("user_rating", "")))
        self.ui.plot_input.setText(series_info.get("plot", ""))
        self.ui.trailer_input.setText(series_info.get("trailer", ""))
        self.ui.image_url_input.setText(series_info.get("image", ""))
        self.ui.episodes_input.setText(str(series_info.get("total_episodes", "N/A")))
        self.ui.seasons_input.setText(str(series_info.get("total_seasons", "N/A")))
        self.ui.plot_input.setCursorPosition(0)

        if hasattr(self.ui, "image_label"):
            self.load_image(series_info.get("image", ""), self.ui.image_label)

    # # ---------------- Search ----------------
    def search_and_show(self):
        series_name_widget = getattr(self.ui, "search_line", None)
        if not series_name_widget or not series_name_widget.text().strip():
            QMessageBox.warning(self, "Empty Search", "Please enter a series name.", QMessageBox.Ok)
            return

        series_name = series_name_widget.text().strip()
        self.ui.search_button.setEnabled(False)
        self.ui.search_button.setText("Searching...")

        self._search_worker = SeriesFetchWorker(series_name)
        self._search_worker.finished.connect(self._on_search_success)
        self._search_worker.failed.connect(self._on_search_failed)
        self._search_worker.start()

    def _on_search_success(self, series_info: dict):
        self.series_info = series_info
        self.ui.search_button.setEnabled(True)
        self.ui.search_button.setText("Search TMDB+OMDB")
        self.display_series_info(series_info)
        self._search_worker = None

    def _on_search_failed(self, error: str):
        self.ui.search_button.setEnabled(True)
        self.ui.search_button.setText("Search")

        if error == "no":
            QMessageBox.information(self, "series Not Found", "No results found.", QMessageBox.Ok)
        elif error == "not series":
            QMessageBox.information(self, "series Not Found", "No series results found.", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Error Fetching series", f"Error: {error}", QMessageBox.Ok)

        self._search_worker = None



