from PySide6.QtWidgets import QListWidget, QListWidgetItem
from app.models.movie import Movie
from app.utils.my_functions import link_to_image
from app.db.sqlite_manger import list_movies  # or your JSON loader
from py_ui.movie_list_widget import MovieListItemWidget
from PySide6.QtCore import Qt, QSettings

class MovieListLoader:
    """Handles loading movies into a QListWidget."""

    def __init__(self, list_widget: QListWidget):
        self.list_widget = list_widget

        self.settings = QSettings("MyCompany", "MyApp")

    def load_movies(self, movies: list[Movie]):
        """Populate the QListWidget with a list of Movie objects."""
        self.list_widget.clear()

        for index, movie in enumerate(movies, start=1):
            item_widget = MovieListItemWidget(movie, index=index)
            item = QListWidgetItem(self.list_widget)
            item.setSizeHint(item_widget.sizeHint())

            # Store movie object for later retrieval
            item.setData(Qt.UserRole, movie)  # Use Qt.UserRole directly

            # Disable selection if needed
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, item_widget)



    def load_from_section(self, section: str, order_by="title", descending=False):
        """Fetch movies from DB by section and load them."""

        sort_key = self.settings.value(f"{section}_sort_by", "title")  # default to title
        reverse = self.settings.value(f"{section}_sort_by_reverse", False, type=bool)
        descending = bool(reverse)

        movies = list_movies(section=section, order_by=sort_key, descending=descending)
        self.load_movies(movies)
