# main_widget.py
from PySide6.QtCore import Qt, QSettings, Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from py_ui.main_ui import Ui_main_widget

import json, requests

# CONTROLLERS
from app.controllers.list_widget import ListLoader
from app.windows.add import AddMediaWindow
from app.controllers.media import (
    pick_random_item,
    media_filter_list,
    media_on_item_clicked,
    media_on_sort_changed
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

        # ----------------------------------------------------
        # Load log file and profile picture
        # ----------------------------------------------------
        with open("log", "r", encoding="utf-8") as f:
            user_info = json.loads(f.read())
            self.set_profile_pic(self.ui.name_lable, user_info.get("profile_pic"))
            self.ui.photo_lable.setText(user_info.get("name", "Guest"))

        # ----------------------------------------------------
        # SECTION MAPS
        # ----------------------------------------------------
        self.movies_sections = self._build_section_map("movies")
        self.series_sections = self._build_section_map("series")

        # Default home page
        self.ui.stacked_body_Widget.setCurrentIndex(0)

        # ----------------------------------------------------
        # SIDE MENU EVENTS
        # ----------------------------------------------------
        self._setup_side_buttons()

        # ----------------------------------------------------
        # FOCUS POLICY for search bars
        # ----------------------------------------------------
        self._apply_focus_policy(self.movies_sections)
        self._apply_focus_policy(self.series_sections)

        # ----------------------------------------------------
        # INITIAL DATA LOAD
        # ----------------------------------------------------
        self._load_all_sections("movies")
        self._load_all_sections("series")

        # ----------------------------------------------------
        # ITEM CLICK EVENTS
        # ----------------------------------------------------
        self._connect_item_clicks(self.movies_sections, "movies")
        self._connect_item_clicks(self.series_sections, "series")

        # ----------------------------------------------------
        # SEARCH BAR INITIAL VISIBILITY
        # ----------------------------------------------------
        self._hide_search_bars(self.movies_sections)
        self._hide_search_bars(self.series_sections)

        # ----------------------------------------------------
        # VIEW MODE SETUP
        # ----------------------------------------------------
        self._init_view_mode("movies", self.movies_sections, self.sync_movies_view_buttons)
        self._init_view_mode("series", self.series_sections, self.sync_series_view_buttons)

        # ----------------------------------------------------
        # RANDOM BUTTONS
        # ----------------------------------------------------
        self._connect_random_buttons(self.movies_sections, "movies")
        self._connect_random_buttons(self.series_sections, "series")

        # ----------------------------------------------------
        # SEARCH FILTER SIGNALS
        # ----------------------------------------------------
        self._connect_search_filter(self.movies_sections, "movies")
        self._connect_search_filter(self.series_sections, "series")

        # ----------------------------------------------------
        # SORTING COMBO BOXES
        # ----------------------------------------------------
        self._setup_sorting(self.movies_sections, "movies")
        self._setup_sorting(self.series_sections, "series")

        # View mode signal
        self.view_mode_changed.connect(self.on_view_mode_changed)

    # ==========================================================================
    # HELPER FUNCTIONS
    # ==========================================================================

    def _build_section_map(self, media_type):
        ui = self.ui
        t = media_type

        return {
            "watching": {
                "list": getattr(ui, f"{t}_list_1"),
                "search": getattr(ui, f"{t}_search_1"),
                "combobox": getattr(ui, f"{t}_sort_by_1"),
                "random_button": getattr(ui, f"{t}_random_button_1"),
                "view_button": getattr(ui, f"{t}_view_1")
            },
            "want_to_watch": {
                "list": getattr(ui, f"{t}_list_2"),
                "search": getattr(ui, f"{t}_search_2"),
                "combobox": getattr(ui, f"{t}_sort_by_2"),
                "random_button": getattr(ui, f"{t}_random_button_2"),
                "view_button": getattr(ui, f"{t}_view_2")
            },
            "continue_later": {
                "list": getattr(ui, f"{t}_list_3"),
                "search": getattr(ui, f"{t}_search_3"),
                "combobox": getattr(ui, f"{t}_sort_by_3"),
                "random_button": getattr(ui, f"{t}_random_button_3"),
                "view_button": getattr(ui, f"{t}_view_3")
            },
            "dont_want_to_continue": {
                "list": getattr(ui, f"{t}_list_4"),
                "search": getattr(ui, f"{t}_search_4"),
                "combobox": getattr(ui, f"{t}_sort_by_4"),
                "random_button": getattr(ui, f"{t}_random_button_4"),
                "view_button": getattr(ui, f"{t}_view_4")
            },
            "watched": {
                "list": getattr(ui, f"{t}_list_5"),
                "search": getattr(ui, f"{t}_search_5"),
                "combobox": getattr(ui, f"{t}_sort_by_5"),
                "random_button": getattr(ui, f"{t}_random_button_5"),
                "view_button": getattr(ui, f"{t}_view_5")
            },
        }

    # ----------------------------------------------------
    def _setup_side_buttons(self):
        buttons = [
            ("show_home", self.show_home, "0"),
            ("show_movies", self.show_movies, "1"),
            ("show_series", self.show_series, "2"),
            ("show_games", self.show_games, "3"),
            ("show_books", self.show_books, "4"),
            ("show_comics", self.show_comics, "5"),
            ("show_setting", self.show_setting, "6"),
        ]

        for name, func, shortcut in buttons:
            btn = getattr(self.ui, name)
            btn.clicked.connect(func)
            btn.setShortcut(shortcut)

        # Add buttons
        self.ui.movies_add_botton.clicked.connect(self.open_add_movie_window)
        self.ui.movies_add_botton.setShortcut("+")

        self.ui.series_add_botton.clicked.connect(self.open_add_series_window)
        self.ui.series_add_botton.setShortcut("+")

    # ----------------------------------------------------
    def _apply_focus_policy(self, sections):
        for sec in sections.values():
            sec["search"].setFocusPolicy(Qt.ClickFocus)

    # ----------------------------------------------------
    def _load_all_sections(self, media_type):
        sections = self.movies_sections if media_type == "movies" else self.series_sections
        loaders_dict = self.movies_loaders if media_type == "movies" else self.series_loaders

        for sec_name, sec_data in sections.items():
            lw = sec_data["list"]
            loader = ListLoader(lw)
            loaders_dict[sec_name] = loader
            loader.load_from_section(sec_name, media_type)

    # ----------------------------------------------------
    def _connect_item_clicks(self, sections, media_type):
        for sec_name, sec_data in sections.items():
            lw = sec_data["list"]
            lw.itemClicked.connect(
                lambda item, s=sec_name: media_on_item_clicked(self, item, s, media_type)
            )

    # ----------------------------------------------------
    def _hide_search_bars(self, sections):
        for sec in sections.values():
            sec["search"].setHidden(True)

    # ----------------------------------------------------
    def _init_view_mode(self, mtype, sections, sync_func):
        saved_mode = self.settings.value(f"{mtype}_view_mode", "list") == "list"

        for sec in sections.values():
            sec["view_button"].setChecked(saved_mode)
            sec["view_button"].toggled.connect(sync_func)

    # ----------------------------------------------------
    def _connect_random_buttons(self, sections, media_type):
        for sec_data in sections.values():
            sec_data["random_button"].clicked.connect(
                lambda _, lw=sec_data["list"]: pick_random_item(self, lw, media_type)
            )

    # ----------------------------------------------------
    def _connect_search_filter(self, sections, media_type):
        for sec_data in sections.values():
            sec_data["search"].textChanged.connect(
                lambda text, lw=sec_data["list"]: media_filter_list(text, lw, media_type)
            )

    # ----------------------------------------------------
    def _setup_sorting(self, sections, media_type):
        options = [
            "Name (A-Z)", "Name (Z-A)",
            "Year (Newest-Oldest)", "Year (Oldest-Newest)",
            "IMDB Rating (High-Low)", "IMDB Rating (Low-High)",
            "User Rating (High-Low)", "User Rating (Low-High)"
        ]

        for sec_name, sec_data in sections.items():
            combo = sec_data["combobox"]

            combo.blockSignals(True)
            combo.clear()
            combo.addItems(options)

            saved = self.settings.value(f"{media_type}_{sec_name}_sort_by_text")
            combo.setCurrentText(saved or "")
            combo.blockSignals(False)

            combo.currentTextChanged.connect(
                lambda text, s=sec_name: media_on_sort_changed(self, s, media_type, text)
            )

    # ==========================================================================
    # PAGE SWITCHING
    # ==========================================================================
    def show_home(self):   self.ui.stacked_body_Widget.setCurrentIndex(0)
    def show_movies(self): self.ui.stacked_body_Widget.setCurrentIndex(1)
    def show_series(self): self.ui.stacked_body_Widget.setCurrentIndex(2)
    def show_games(self):  self.ui.stacked_body_Widget.setCurrentIndex(3)
    def show_books(self):  self.ui.stacked_body_Widget.setCurrentIndex(4)
    def show_comics(self): self.ui.stacked_body_Widget.setCurrentIndex(5)
    def show_setting(self): self.ui.stacked_body_Widget.setCurrentIndex(6)

    # ==========================================================================
    # ADD MEDIA WINDOWS
    # ==========================================================================
    def open_add_movie_window(self):
        win = AddMediaWindow("movies")
        win.media_added.connect(lambda *_: self.refresh_all_sections("movies"))
        win.exec()

    def open_add_series_window(self):
        win = AddMediaWindow("series")
        win.media_added.connect(lambda *_: self.refresh_all_sections("series"))
        win.exec()

    # ==========================================================================
    # REFRESH FUNCTIONS
    # ==========================================================================
    def refresh_all_sections(self, media_type):
        print("refresh all sections", media_type)
        self._load_all_sections(media_type)

    def refresh_one_section(self, section, media_type, lw):
        loader = ListLoader(lw)
        loader.load_from_section(section, media_type)

    # ==========================================================================
    # VIEW MODE SYNC
    # ==========================================================================
    def on_view_mode_changed(self, mode, media_type):
        loaders = self.movies_loaders if media_type == "movies" else self.series_loaders
        for loader in loaders.values():
            loader.set_view_mode(mode, media_type)

    def sync_movies_view_buttons(self, checked):
        for s in self.movies_sections.values():
            if s["view_button"].isChecked() != checked:
                s["view_button"].setChecked(checked)

    def sync_series_view_buttons(self, checked):
        for s in self.series_sections.values():
            if s["view_button"].isChecked() != checked:
                s["view_button"].setChecked(checked)

    # ==========================================================================
    # PROFILE PICTURE
    # ==========================================================================
    @staticmethod
    def set_profile_pic(label, url, size=50, radius=20):
        if not url:
            return
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()

            pix = QPixmap()
            pix.loadFromData(r.content)
            pix = pix.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

            rounded = QPixmap(size, size)
            rounded.fill(Qt.transparent)

            painter = QPainter(rounded)
            painter.setRenderHint(QPainter.Antialiasing)
            path = QPainterPath()
            path.addRoundedRect(0, 0, size, size, radius, radius)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, pix)
            painter.end()

            label.setPixmap(rounded)
            label.setScaledContents(True)

        except Exception as e:
            print("Could not load profile picture:", e)
