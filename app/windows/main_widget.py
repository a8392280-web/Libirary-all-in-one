# main_widget.py
from PySide6.QtCore import Qt, QSettings, Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from py_ui.main_ui import Ui_main_widget
from app.windows.movies_show_widget import ShowMovieWindow
from app.windows.movies_add_widget import AddMovieWindow
from app.windows.series_add_widget import AddSeriesWindow
from app.controllers.list_widget import ListLoader
from PySide6.QtGui import QPixmap
import json
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
import requests
# Import the CONTROLLER functions
from app.controllers.movies import (
    pick_random_movie,
    movie_filter_list,
    movie_on_sort_changed,
    movie_on_item_clicked,
)
from app.controllers.series import(
    pick_random_series,
    series_filter_list,
    series_on_sort_changed,
    series_on_item_clicked
)

class Widget(QWidget):

    view_mode_changed = Signal(str, str)  # view_mode, type

    def __init__(self):
        super().__init__()

        self.ui = Ui_main_widget()
        self.ui.setupUi(self)

        self.setWindowTitle("My Library")
        self.settings = QSettings("MyCompany", "MyApp")


        self.movies_loaders = {}
        self.series_loaders = {}


        self.view_mode_changed.connect(self.on_view_mode_changed)
        self.ui.movies_view_1.toggled.connect(lambda checked: self.view_mode_changed.emit("list" if checked else "grid","movies"))
        self.ui.series_view_1.toggled.connect(lambda checked: self.view_mode_changed.emit("list" if checked else "grid","series"))


        # Load log
        with open("log", "r", encoding="utf-8") as f:
            user_info = json.loads(f.read())
            self.set_profile_pic(self.ui.name_lable, user_info.get("profile_pic"))
            self.ui.photo_lable.setText(user_info.get("name", "Guest"))

        # SECTION MAP
        self.movies_sections = {
            "watching": {
                "list": self.ui.movies_list_1,
                "search": self.ui.movies_search_1,
                "combobox": self.ui.movies_sort_by_1,
                "random_button": self.ui.movies_random_button_1,
                "view_button": self.ui.movies_view_1
            },
            "want_to_watch": {
                "list": self.ui.movies_list_2,
                "search": self.ui.movies_search_2,
                "combobox": self.ui.movies_sort_by_2,
                "random_button": self.ui.movies_random_button_2,
                "view_button": self.ui.movies_view_2
            },
            "continue_later": {
                "list": self.ui.movies_list_3,
                "search": self.ui.movies_search_3,
                "combobox": self.ui.movies_sort_by_3,
                "random_button": self.ui.movies_random_button_3,
                "view_button": self.ui.movies_view_3
            },
            "dont_want_to_continue": {
                "list": self.ui.movies_list_4,
                "search": self.ui.movies_search_4,
                "combobox": self.ui.movies_sort_by_4,
                "random_button": self.ui.movies_random_button_4,
                "view_button": self.ui.movies_view_4
            },
            "watched": {
                "list": self.ui.movies_list_5,
                "search": self.ui.movies_search_5,
                "combobox": self.ui.movies_sort_by_5,
                "random_button": self.ui.movies_random_button_5,
                "view_button": self.ui.movies_view_5
            },
        }
        self.series_sections = {
            "watching": {
                "list": self.ui.series_list_1,
                "search": self.ui.series_search_1,
                "combobox": self.ui.series_sort_by_1,
                "random_button": self.ui.series_random_button_1,
                "view_button": self.ui.series_view_1
            },
            "want_to_watch": {
                "list": self.ui.series_list_2,
                "search": self.ui.series_search_2,
                "combobox": self.ui.series_sort_by_2,
                "random_button": self.ui.series_random_button_2,
                "view_button": self.ui.series_view_2
            },
            "continue_later": {
                "list": self.ui.series_list_3,
                "search": self.ui.series_search_3,
                "combobox": self.ui.series_sort_by_3,
                "random_button": self.ui.series_random_button_3,
                "view_button": self.ui.series_view_3
            },
            "dont_want_to_continue": {
                "list": self.ui.series_list_4,
                "search": self.ui.series_search_4,
                "combobox": self.ui.series_sort_by_4,
                "random_button": self.ui.series_random_button_4,
                "view_button": self.ui.series_view_4
            },
            "watched": {
                "list": self.ui.series_list_5,
                "search": self.ui.series_search_5,
                "combobox": self.ui.series_sort_by_5,
                "random_button": self.ui.series_random_button_5,
                "view_button": self.ui.series_view_5
            },
        }







        self.ui.stacked_body_Widget.setCurrentIndex(0)

        # SIDE BUTTONS
        self.ui.show_home.setChecked(True)
        self.ui.show_home.clicked.connect(self.show_home)
        self.ui.show_home.setShortcut("0")

        self.ui.show_movies.clicked.connect(self.show_movies)
        self.ui.show_movies.setShortcut("1")

        self.ui.show_series.clicked.connect(self.show_series)
        self.ui.show_series.setShortcut("2")

        self.ui.show_games.clicked.connect(self.show_games)
        self.ui.show_games.setShortcut("3")

        self.ui.show_books.clicked.connect(self.show_books)
        self.ui.show_books.setShortcut("4")

        self.ui.show_comics.clicked.connect(self.show_comics)
        self.ui.show_comics.setShortcut("5")

        self.ui.show_setting.clicked.connect(self.show_setting)
        self.ui.show_setting.setShortcut("6")

        self.ui.movies_add_botton.clicked.connect(self.open_add_movie_window)
        self.ui.movies_add_botton.setShortcut("+")

        self.ui.series_add_botton.clicked.connect(self.open_add_series_window)
        self.ui.series_add_botton.setShortcut("+")

        # SEARCH FOCUS POLICY

        #movies
        for section_name, section_data in self.movies_sections.items():
            search_widget = section_data["search"]
            search_widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        #series
        for section_name, section_data in self.series_sections.items():
            search_widget = section_data["search"]
            search_widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)


        # LOAD
        
        # movies
        for section_name, section_data in self.movies_sections.items():
            list_widget = section_data["list"]
            loader = ListLoader(list_widget)
            self.movies_loaders[section_name] = loader
            loader.load_from_section(section_name,"movies")

        # series
        for section_name, section_data in self.series_sections.items():
            list_widget = section_data["list"]
            loader = ListLoader(list_widget)
            self.series_loaders[section_name] = loader
            loader.load_from_section(section_name,"series")

        # ITEM CLICK

        # movies
        for section_name, section_data in self.movies_sections.items():
            list_widget = section_data["list"]
            list_widget.itemClicked.connect(
                lambda item, sec=section_name: movie_on_item_clicked(self, item, sec)
            )

        # series
        for section_name, section_data in self.series_sections.items():
            list_widget = section_data["list"]
            list_widget.itemClicked.connect(
                lambda item, sec=section_name: series_on_item_clicked(self, item, sec)
            )

        # HIDE SEARCH BAR INITIALLY

        # movies
        for section_name, section_data in self.movies_sections.items():
            section_data["search"].setHidden(True)

        # series
        for section_name, section_data in self.series_sections.items():
            section_data["search"].setHidden(True)


        # VIEW MODE

        # movies
        if self.settings.value("movies_view_mode", "list") == "list":
            for section in self.movies_sections.values():
                section["view_button"].setChecked(True)
        else:
            for section in self.movies_sections.values():
                section["view_button"].setChecked(False)

        for section in self.movies_sections.values():
            section["view_button"].toggled.connect(self.sync_movies_view_buttons)

        # series
        if self.settings.value("series_view_mode", "list") == "list":
            for section in self.series_sections.values():
                section["view_button"].setChecked(True)
        else:
            for section in self.series_sections.values():
                section["view_button"].setChecked(False)

        for section in self.series_sections.values():
            section["view_button"].toggled.connect(self.sync_series_view_buttons)




        # RANDOM BUTTONS

        # movies
        for section_name, section_data in self.movies_sections.items():
            section_data["random_button"].clicked.connect(
                lambda checked=False, lw=section_data["list"]: pick_random_movie(self, lw)
            )
        # series
        for section_name, section_data in self.series_sections.items():
            section_data["random_button"].clicked.connect(
                lambda checked=False, lw=section_data["list"]: pick_random_series(self, lw)
            )

        # SEARCH FILTER

        # movies
        for section_name, section_data in self.movies_sections.items():
            section_data["search"].textChanged.connect(
                lambda text, lw=section_data["list"]: movie_filter_list(text, lw)
            )
        
        # series
        for section_name, section_data in self.series_sections.items():
            section_data["search"].textChanged.connect(
                lambda text, lw=section_data["list"]: series_filter_list(text, lw)
            )



        # SORT OPTIONS
        options = [
            "Name (A-Z)",
            "Name (Z-A)",
            "Year (Newest-Oldest)",
            "Year (Oldest-Newest)",
            "IMDB Rating (High-Low)",
            "IMDB Rating (Low-High)",
            "User Rating (High-Low)",
            "User Rating (Low-High)"
        ]

        # movies
        for section_name, section_data in self.movies_sections.items():
            combo = section_data["combobox"]
            combo.blockSignals(True)
            combo.clear()
            combo.addItems(options)

            saved_text = self.settings.value(f"movies_{section_name}_sort_by_text")
            if saved_text:
                combo.setCurrentText(saved_text)
            else:
                combo.setCurrentIndex(-1)

            combo.blockSignals(False)
            combo.currentTextChanged.connect(
                lambda text, sec=section_name: movie_on_sort_changed(self, sec, text)
            )

        # series
        for section_name, section_data in self.series_sections.items():
            combo = section_data["combobox"]
            combo.blockSignals(True)
            combo.clear()
            combo.addItems(options)

            saved_text = self.settings.value(f"series_{section_name}_sort_by_text")
            if saved_text:
                combo.setCurrentText(saved_text)
            else:
                combo.setCurrentIndex(-1)

            combo.blockSignals(False)
            combo.currentTextChanged.connect(
                lambda text, sec=section_name: series_on_sort_changed(self, sec, text)
            )

    # --------------------------------------------------------------------------
    # UI PAGE SWITCHING
    # --------------------------------------------------------------------------
    def show_home(self):
        self.ui.stacked_body_Widget.setCurrentIndex(0)

    def show_movies(self):
        self.ui.stacked_body_Widget.setCurrentIndex(1)

    def show_series(self):
        self.ui.stacked_body_Widget.setCurrentIndex(2)

    def show_games(self):
        self.ui.stacked_body_Widget.setCurrentIndex(3)

    def show_books(self):
        self.ui.stacked_body_Widget.setCurrentIndex(4)

    def show_comics(self):
        self.ui.stacked_body_Widget.setCurrentIndex(5)

    def show_setting(self):
        self.ui.stacked_body_Widget.setCurrentIndex(6)

    # --------------------------------------------------------------------------
    # movies
    def open_add_movie_window(self):
        self.add_window = AddMovieWindow()
        self.add_window.movie_added.connect(self.refresh_all_movies_sections)
        self.add_window.exec()

    # series
    def open_add_series_window(self):
        self.add_window = AddSeriesWindow()
        self.add_window.series_added.connect(self.refresh_all_series_sections)
        self.add_window.exec()

    # --------------------------------------------------------------------------

    # movies
    def refresh_all_movies_sections(self):
        print("refres all sections movies")
        for section_name, section_data in self.movies_sections.items():
            loader = ListLoader(section_data["list"])
            loader.load_from_section(section_name,"movies")

    # series
    def refresh_all_series_sections(self):
        print("refres all sections series")
        for section_name, section_data in self.series_sections.items():
            loader = ListLoader(section_data["list"])
            loader.load_from_section(section=section_name,type="series")


    def refresh_one_section(self,section,type, list_widget):

        sort_key = self.settings.value(f"{type}_{section}_sort_by", "title")
        reverse = self.settings.value(f"{type}_{section}_sort_by_reverse", False, type=bool)
        loader = ListLoader(list_widget)
        loader.load_from_section(section=section,type=type)




    # --------------------------------------------------------------------------
    def on_view_mode_changed(self, view_mode, type):
        print("changed to", view_mode, "for", type)

        if type == "movies":
            for loader in self.movies_loaders.values():
                loader.set_view_mode(view_mode, "movies")

        elif type == "series":
            for loader in self.series_loaders.values():
                loader.set_view_mode(view_mode, "series")



    # movies
    def sync_movies_view_buttons(self, checked):
        for section in self.movies_sections.values():
            if section["view_button"].isChecked() != checked:
                section["view_button"].setChecked(checked)

    # series
    def sync_series_view_buttons(self, checked):
        for section in self.series_sections.values():
            if section["view_button"].isChecked() != checked:
                section["view_button"].setChecked(checked)

    def set_profile_pic(label, url, size=50, radius=20):
        if not url:
            return

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

            rounded = QPixmap(size, size)
            rounded.fill(Qt.transparent)

            painter = QPainter(rounded)
            painter.setRenderHint(QPainter.Antialiasing)

            path = QPainterPath()
            path.addRoundedRect(0, 0, size, size, radius, radius)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            label.setPixmap(rounded)
            label.setScaledContents(True)

        except Exception as e:
            print("Could not load profile picture:", e)

