from PySide6.QtWidgets import QDialog, QMessageBox, QComboBox,QListWidget,QListWidgetItem,QLabel,QHBoxLayout,QVBoxLayout,QWidget
from PySide6.QtCore import Signal, Qt, QThread,QSize,QPoint
from PySide6.QtGui import QPixmap, QColor, QPainter
from py_ui.add import Ui_add_widget
from app.utils.my_functions import link_to_image, get_selected_section, resize_combo_box_to_contents

# Import DB and Models dynamically
from app.models.movie import Movie
from app.models.series import Series
from app.db.movies_db import insert_movie, list_movies
from app.db.series_db import insert_series, list_series

from app.fetch.movies_info_fetcher import get_movie_info, search_movies_tmdb,search_anime_movies,get_movies_anime_info
from app.fetch.series_info_fetcher import get_series_info, search_series_tmdb,search_anime_series,get_series_anime_info


class SearchWorker(QThread):
    results_ready = Signal(list)

    def __init__(self, query,media_type,api, parent=None):
        super().__init__(parent)
        self.query = query
        self.media_type = media_type
        self.api=api
    def run(self):
        # YOUR API SEARCH FUNCTION
        if self.media_type == "movies" and self.api == "tmdb+omdb":
            movies = search_movies_tmdb(self.query)
            self.results_ready.emit(movies)

        elif self.media_type == "movies" and self.api == "myanimelist":
            movies = search_anime_movies(self.query)
            self.results_ready.emit(movies)


        elif self.media_type == "series" and self.api == "tmdb+omdb":
            series = search_series_tmdb(self.query)
            self.results_ready.emit(series)

        elif self.media_type == "series" and self.api == "myanimelist":
            series = search_anime_series(self.query)
            self.results_ready.emit(series)

        


class MediaInfoWorker(QThread):
    result_ready = Signal(object)

    def __init__(self, id,media_type,api, parent=None):
        super().__init__(parent)
        self.id = id
        self.media_type = media_type
        self.api = api

    def run(self):
        if self.media_type == "movies" and self.api == "tmdb+omdb":
            media_info = get_movie_info(self.id)
            self.result_ready.emit(media_info)

        if self.media_type == "movies" and self.api == "myanimelist":
            media_info = get_movies_anime_info(self.id)
            self.result_ready.emit(media_info)


        elif self.media_type == "series" and self.api == "tmdb+omdb":
            media_info = get_series_info(self.id)
            self.result_ready.emit(media_info)

        elif self.media_type == "series" and self.api == "myanimelist":
            media_info = get_series_anime_info(self.id)
            self.result_ready.emit(media_info)



# ---------------- Generic Add Media Window ----------------
class AddMediaWindow(QDialog):
    """Unified window for adding Movies or Series."""
    media_added = Signal(object)  # Movie or Series object

    def __init__(self, media_type: str, parent=None):
        """
        :param media_type: 'movie' or 'series'
        """
        super().__init__(parent)
        self.media_type = media_type
        self.ui = Ui_add_widget()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Add New {'Movie' if media_type == 'movie' else 'Series'}")

        # Media info fetched from API
        self.media_info = None

        # Load existing data per section
        self.data = self.get_existing_data()

        self.setup_ui()
        self.setup_signals()

        # new search methode:

        self.search_popup = QListWidget(self)
        self.search_popup.setWindowFlags(Qt.Popup)
        self.search_popup.hide()
        self.ui.result_list_widget.itemClicked.connect(self.on_media_selected)


        self.is_loading_info = False


    # ---------------- Initialize UI ----------------
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

        # ---------------- HIDE specific fields ----------------
        if self.media_type == "movies":
            if hasattr(self.ui, "seasons_input"):
                self.ui.seasons_input.hide()
            if hasattr(self.ui, "episodes_input"):
                self.ui.episodes_input.hide()





        #--------------------- SET UP Search Combobox -----------------------------------------

        apis = ["TMDB+OMDB"]
        self.ui.apis_combobox.addItems(apis)



    def setup_signals(self):
        if hasattr(self.ui, "cancel_button"):
            self.ui.cancel_button.clicked.connect(self.close)
        if hasattr(self.ui, "apply_button"):
            self.ui.apply_button.clicked.connect(self.add_media_entry)
        if hasattr(self.ui, "search_button"):
            self.ui.search_button.clicked.connect(self.on_search_clicked) 

    # ---------------- Load Image ----------------
    def load_image(self, url: str, label, width=180, height=270):
        """Load image from URL or use placeholder."""
        if not url:
            label.setPixmap(self.get_placeholder_pixmap(width, height))
            return
        try:
            link_to_image(url, label, width, height)
        except Exception:
            label.setPixmap(self.get_placeholder_pixmap(width, height))

    def get_placeholder_pixmap(self, width, height):
        """Return a placeholder QPixmap."""
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor("#444"))
        painter = QPainter(pixmap)
        painter.setPen(QColor("#ccc"))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "No Image")
        painter.end()
        return pixmap

    # ---------------- Extract & Merge Data ----------------
    def extract_media_data(self):
        """Extract user input from UI fields."""
        data = {
            "section": get_selected_section(self.ui.section_selector),
            "title": self.ui.name_input.text().strip(),
            "runtime": self.ui.time_input.text().strip(),
            "year": self.ui.date_input.text().strip(),
            "imdb_rating": self.ui.imdb_rate_input.text().strip(),
            "user_rating": self.ui.user_rate_input.text().strip(),
            "plot": self.ui.plot_input.text().strip(),
            "genres": [g.strip() for g in self.ui.gener_input.text().split("-") if g.strip()],
            "poster_path": self.ui.image_url_input.text().strip() or (self.media_info.get("Image") if self.media_info else None),
            "trailer": self.ui.trailer_input.text().strip(),
        }

        # Extra fields for series
        if self.media_type == "series":
            data.update({
                "total_seasons": self.ui.seasons_input.text().strip(),
                "total_episodes": self.ui.episodes_input.text().strip()
            })

        return data

    def merge_media_data(self, extracted: dict) -> dict:
        """Merge extracted user data with fetched info."""
        if not self.media_info:
            self.media_info = {}

        data = self.media_info.copy()
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
            "section": extracted.get("section")
        })

        if self.media_type == "series":
            data.update({
                "total_seasons": extracted.get("total_seasons"),
                "total_episodes": extracted.get("total_episodes")
            })

        return data

    # ---------------- Add Media Entry ----------------
    def add_media_entry(self):
        try:
            extracted = self.extract_media_data()
            data = self.merge_media_data(extracted)
            print(data)

            self.validate_media_data(data)

            duplicate_section = self.check_duplicate(data["name"])
            if duplicate_section:
                reply = QMessageBox.question(
                    self, "Confirm Adding",
                    f"There is a {self.media_type} with this name ({data['name']}) in the ({duplicate_section.replace('_',' ')}) section.\n"
                    "Are you sure you want to add it again?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.No:
                    QMessageBox.information(self, "Add Canceled", f"{self.media_type.title()} was not added.", QMessageBox.Ok)
                    return

            self.insert_media_data(data)
            self.close()
            QMessageBox.information(self, "Success", f"'{data['name']}' was added successfully!", QMessageBox.Ok)

        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", str(e), QMessageBox.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected error: {str(e)}", QMessageBox.Ok)

    # ---------------- Validation ----------------
    def validate_media_data(self, data: dict):
        if not data["name"]:
            raise ValueError(f"{self.media_type.title()} name cannot be empty.")
        if not data["section"]:
            raise ValueError(f"Please select a section for the {self.media_type}.")

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
        for section, items in self.data.items():
            for item in items:
                if item.title.strip().lower() == title_lower:
                    return section
        return None

    # ---------------- Insert Media ----------------
    def insert_media_data(self, data: dict):
        """Insert the media object into the DB."""
        if self.media_type == "movies":
            media_obj = Movie(
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
                mal_id=data.get("mal_id"),
                section=data.get("section"),
                trailer=data.get("trailer"),
                cast=data.get("cast"),
                director=data.get("director"),
                tmdb_rating=data.get("tmdb_rating"),
                mal_rating=data.get("mal_rating"),
                tmdb_votes=data.get("tmdb_votes"),
                imdb_votes=data.get("imdb_votes"),
                rotten_tomatoes=data.get("rotten_tomatoes"),
                metascore=data.get("metascore")
            )
            insert_movie(media_obj)

        elif self.media_type == "series":
            media_obj = Series(
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
                cast=data.get("cast"),
                creator=data.get("creator"),
                tmdb_rating=data.get("tmdb_rating"),
                tmdb_votes=data.get("tmdb_votes"),
                imdb_votes=data.get("imdb_votes"),
                rotten_tomatoes=data.get("rotten_tomatoes"),
                metascore=data.get("metascore"),
                total_seasons=data.get("total_seasons"),
                total_episodes=data.get("total_episodes"),
                seasons=data.get("seasons")
            )
            insert_series(media_obj)

        self.media_added.emit(media_obj)

    # ---------------- Display Info ----------------
    def display_media_info(self, media_info: dict):
        """Populate UI fields with fetched data."""
        self.ui.name_input.setText(media_info.get("name", ""))
        self.ui.time_input.setText(str(media_info.get("runtime", "")))
        self.ui.date_input.setText(media_info.get("year", ""))
        self.ui.gener_input.setText("-".join(media_info.get("genres", [])))
        self.ui.imdb_rate_input.setText(str(media_info.get("imdb_rating", "")))
        self.ui.mal_rate_input.setText(str(media_info.get("mal_rating", "")))
        self.ui.user_rate_input.setText(str(media_info.get("user_rating", "")))
        self.ui.plot_input.setText(media_info.get("plot", ""))
        self.ui.trailer_input.setText(media_info.get("trailer", ""))
        self.ui.image_url_input.setText(media_info.get("image", ""))
        self.ui.plot_input.setCursorPosition(0)

        if self.media_type == "series":
            self.ui.episodes_input.setText(str(media_info.get("total_episodes", "N/A")))
            self.ui.seasons_input.setText(str(media_info.get("total_seasons", "N/A")))

        if hasattr(self.ui, "image_label"):
            self.load_image(media_info.get("image", ""), self.ui.image_label)


    def on_search_clicked(self):


        self.seleted_api= get_selected_section(self.ui.apis_combobox)
        if self.seleted_api == None:
            QMessageBox.warning(self, "API", "Select an API to fetch info from", QMessageBox.Ok)
            return
        print(self.seleted_api)
        query = self.ui.search_line.text().strip()
        if not query:
            return

        self.ui.search_button.setEnabled(False)  # disable while fetching

        # Start worker
        self.worker = SearchWorker(query,self.media_type,self.seleted_api)
        self.worker.results_ready.connect(self.show_search_results)
        self.worker.finished.connect(lambda: self.ui.search_button.setEnabled(True))
        self.worker.start()

    # ---------------- Helper ----------------
    def get_existing_data(self):
        """Return the existing data per section based on media type."""
        if self.media_type == "movie":
            return {sec: list_movies(sec) for sec in ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]}
        elif self.media_type == "series":
            return {sec: list_series(sec) for sec in ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]}
        return {}


    def show_search_results(self, media):
        """
        Build and show the TMDB search results directly in result_list_widget.
        Each item has: poster + title + year.
        """

        self.ui.result_list_widget.clear()  # clear previous results

        if not media:
            return  # nothing to show

        # ---- ADD MOVIE ITEMS ----
        for movie in media:
            title = movie["title"]
            year = movie.get("release_date", "Unknown")
            tmdb_id = movie["id"]
            poster_url = movie["poster_url"]

            # --- Custom item widget ---
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(5, 5, 5, 5)
            layout.setSpacing(10)
            widget.setStyleSheet("""
                    QWidget{
                    background: transparent;
                    border-radius: 6px;
                    
                }

                /* Hover */
                QWidget:hover {
                    background: #2d2d2d;
                }

                /* Pressed (mouse down) */
                QWidget:pressed {
                    background: #1a1a1a;
                }
            """)




            # Poster Label
            poster_label = QLabel()
            poster_label.setFixedSize(70, 100)
            if poster_url:
                link_to_image(poster_url, poster_label, 70, 100)
            layout.addWidget(poster_label)

            # Title + Year section
            text_layout = QVBoxLayout()
            title_label = QLabel(title)
            title_label.setWordWrap(True)
            title_label.setStyleSheet("font-weight: bold; font-size: 14px;")

            year = year.split("-")[0] if year else "Unknown"
            year_label = QLabel(str(year))
            year_label.setStyleSheet("color: gray; font-size: 12px;")
            

            text_layout.addWidget(title_label)
            text_layout.addWidget(year_label)
            layout.addLayout(text_layout)

            # QListWidget item
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 110))
            item.setData(Qt.UserRole, tmdb_id)
            

            self.ui.result_list_widget.addItem(item)
            self.ui.result_list_widget.setItemWidget(item, widget)
            self.ui.result_list_widget.setStyleSheet("""
            QScrollBar:vertical {
                background: #2d3748;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #5a67d8;
                border-radius: 5px;
            }

             
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
                height: 0px;
            }

           
            QScrollBar::sub-page:vertical {
                background: none;
            }
                                
        """)




    def on_media_selected(self, item):

        if self.is_loading_info:
            return  # ignore second click
    
        self.is_loading_info = True

        id = item.data(Qt.UserRole)
        self.search_popup.hide()

        # Create and start the worker
        self.info_thread = MediaInfoWorker(id,self.media_type,self.seleted_api)
        self.info_thread.result_ready.connect(self.display_media_info_from_thread)
        self.info_thread.finished.connect(self._info_thread_finished)
        self.info_thread.start()
        
    def display_media_info_from_thread(self, media_info):
        self.media_info = media_info
        if media_info and media_info != "no":
            self.display_media_info(media_info)
        else:
            QMessageBox.warning(self, "Error", "Movie info could not be loaded.")

    def _info_thread_finished(self):
        self.is_loading_info = False
