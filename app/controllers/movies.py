# movie_controller.py
import random
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from app.windows.movies_show_widget import ShowMovieWindow
# ---------------------------------------------
def pick_random_movie(self, list_widget):
    count = list_widget.count()
    if count == 0:
        QMessageBox.information(self, "No Movies", "This list is empty!")
        return

    random_index = random.randint(0, count - 1)
    item = list_widget.item(random_index)

    list_widget.scrollToItem(item)
    item.setSelected(True)

    movie = item.data(Qt.UserRole)
    if movie and hasattr(movie, 'title'):
        QMessageBox.information(self, "Random Pick", f"🎬 Your random movie is:\n\n{movie.title}")
    else:
        QMessageBox.information(self, "Random Pick", "Unknown")

# ---------------------------------------------
def movie_filter_list(text, list_widget):
    text = text.strip().lower()

    if text == "":
        for i in range(list_widget.count()):
            list_widget.item(i).setHidden(False)
        return

    for i in range(list_widget.count()):
        item = list_widget.item(i)
        movie = item.data(Qt.UserRole)

        if movie:
            name = str(movie.title or "").lower()
            year = str(movie.year or "").lower()
            search_text = f"{name} {year}"
            item.setHidden(text not in search_text)
        else:
            item.setHidden(True)

# ---------------------------------------------
def movie_on_sort_changed(main_widget, section, sort_by):
    if sort_by == "Name (A-Z)":
        sort_key, reverse = "title", False
    elif sort_by == "Name (Z-A)":
        sort_key, reverse = "title", True
    elif sort_by == "Year (Newest-Oldest)":
        sort_key, reverse = "year", True
    elif sort_by == "Year (Oldest-Newest)":
        sort_key, reverse = "year", False
    elif sort_by == "IMDB Rating (High-Low)":
        sort_key, reverse = "imdb_rating", True
    elif sort_by == "IMDB Rating (Low-High)":
        sort_key, reverse = "imdb_rating", False
    elif sort_by == "User Rating (High-Low)":
        sort_key, reverse = "user_rating", True
    elif sort_by == "User Rating (Low-High)":
        sort_key, reverse = "user_rating", False
    else:
        return

    main_widget.settings.setValue(f"movies_{section}_sort_by_text", sort_by)
    main_widget.settings.setValue(f"movies_{section}_sort_by", sort_key)
    main_widget.settings.setValue(f"movies_{section}_sort_by_reverse", reverse)
    print("movie on sort change")
    main_widget.refresh_one_section(section, "movies", main_widget.movies_sections[section]["list"])

# ---------------------------------------------
def movie_on_item_clicked(self, item, section):
    movie = item.data(Qt.UserRole)
    if movie and hasattr(movie, "id"):
        self.selected_id = movie.id
        self.show_movie_window = ShowMovieWindow(section=section, movie_id=self.selected_id)
        self.show_movie_window.movie_deleted.connect(self.refresh_all_movies_sections)
        self.show_movie_window.movie_moved.connect(self.refresh_all_movies_sections)
        self.show_movie_window.exec()

# ---------------------------------------------

