from PySide6.QtWidgets import QListWidget, QListWidgetItem, QListView
from PySide6.QtCore import Qt, QSettings, QSize
from app.db.movies_db import list_movies
from app.db.series_db import list_series
from py_ui.list_widget import ListItemWidget
from py_ui.grid_widget import GridItemWidget

GRID_SIZE = QSize(170, 300)

class ListLoader:

    def __init__(self, list_widget: QListWidget):
        self.list_widget = list_widget
        self.settings = QSettings("MyCompany", "MyApp")

        # Save current view modes
        self.view_mode = {
            "movies": self.settings.value("movies_view_mode", "list"),
            "series": self.settings.value("series_view_mode", "list")
        }

        # Track last displayed data
        self.current = {"movies": [], "series": []}
        self.current_section = {"movies": None, "series": None}

        # Initialize UI
        self.setup_view_mode("movies")
        self.setup_view_mode("series")

    # ---------------------------------------------------------
    # VIEW MODE SETUP
    # ---------------------------------------------------------
    def setup_view_mode(self, type):
        view = self.view_mode[type]

        if view == "grid":
            self.list_widget.setViewMode(QListView.IconMode)
            self.list_widget.setFlow(QListView.LeftToRight)
            self.list_widget.setWrapping(True)
            self.list_widget.setResizeMode(QListView.Adjust)
            self.list_widget.setGridSize(GRID_SIZE)
            self.list_widget.setSpacing(10)
        else:
            self.list_widget.setViewMode(QListView.ListMode)
            self.list_widget.setFlow(QListView.TopToBottom)
            self.list_widget.setWrapping(False)
            self.list_widget.setResizeMode(QListView.Adjust)
            self.list_widget.setGridSize(QSize())
            self.list_widget.setSpacing(5)

    # ---------------------------------------------------------
    # CHANGE VIEW MODE
    # ---------------------------------------------------------
    def set_view_mode(self, view_mode: str, type):
        self.view_mode[type] = view_mode
        self.settings.setValue(f"{type}_view_mode", view_mode)
        self.setup_view_mode(type)

        # Always reload from DB when section is active
        if self.current_section[type]:
            self.load_from_section(self.current_section[type], type)
        else:
            self.load(self.current[type], type)


    # ---------------------------------------------------------
    # LOAD DATA INTO UI
    # ---------------------------------------------------------
    def load(self, items: list, type):
        """Load movies or series into the QListWidget."""
        self.list_widget.clear()
        self.current[type] = items

        grid_mode = self.view_mode[type] == "grid"

        for index, obj in enumerate(items, start=1):
            item_widget = GridItemWidget(obj, index=index) if grid_mode else ListItemWidget(obj, index=index)
            item_size = GRID_SIZE if grid_mode else item_widget.sizeHint()

            item = QListWidgetItem(self.list_widget)
            item.setSizeHint(item_size)
            item.setData(Qt.UserRole, obj)
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, item_widget)

    # ---------------------------------------------------------
    # LOAD FROM DATABASE
    # ---------------------------------------------------------
    def load_from_section(self, section: str, type):
        if type == "movies":
            sort_key = self.settings.value(f"movies_{section}_sort_by", "title")
            reverse = self.settings.value(f"movies_{section}_sort_by_reverse", False, type=bool)
            items = list_movies(section=section, order_by=sort_key, descending=reverse)
        else:
            sort_key = self.settings.value(f"series_{section}_sort_by", "title")
            reverse = self.settings.value(f"series_{section}_sort_by_reverse", False, type=bool)
            items = list_series(section=section, order_by=sort_key, descending=reverse)

        self.current_section[type] = section
        self.load(items, type)
