from PySide6.QtCore import Qt, QSettings, Signal
from PySide6.QtWidgets import QWidget,QMessageBox
import random
from py_ui.main_ui import Ui_main_widget
from app.windows.movies_show_widget import ShowMovieWindow
from app.windows.movies_add_widget import AddMovieWindow
from app.controllers.list_widget import MovieListLoader
import json
import requests
from PySide6.QtGui import QPixmap,QPainter,QPainterPath
from io import BytesIO

class Widget(QWidget):
    
    view_mode_changed = Signal(str)

    def __init__(self):
        super(Widget, self).__init__() # Initialize the parent class
         
        self.ui = Ui_main_widget()
        self.ui.setupUi(self) # Set up the UI from the imported class

        self.setWindowTitle("My Library") # set the window title
        self.settings = QSettings("MyCompany", "MyApp") # learn about it then see

        # Store loaders
        self.section_loaders = {}

        # Connect the signal
        self.view_mode_changed.connect(self.on_view_mode_changed)
        # Connect toggled signal

        self.ui.movies_view_1.toggled.connect(lambda checked: self.view_mode_changed.emit("list" if checked else "grid"))

        with open("log", "r", encoding="utf-8") as f:
            user_info = json.loads(f.read())
            self.set_profile_pic(self.ui.name_lable, user_info.get("profile_pic"))
            self.ui.photo_lable.setText(user_info.get("name", "Guest")) 

        # section with its content
        self.sections = {
            "watching": {
                "list": self.ui.movies_list_1,
                "search": self.ui.movies_search_1,
                "combobox": self.ui.movies_sort_by_1,
                "random_button": self.ui.movies_random_button_1,
                "view_button" : self.ui.movies_view_1
            },
            "want_to_watch": {
                "list": self.ui.movies_list_2,
                "search": self.ui.movies_search_2,
                "combobox": self.ui.movies_sort_by_2,
                "random_button": self.ui.movies_random_button_2,
                "view_button" : self.ui.movies_view_2
            },
            "continue_later": {
                "list": self.ui.movies_list_3,
                "search": self.ui.movies_search_3,
                "combobox" : self.ui.movies_sort_by_3,
                "random_button": self.ui.movies_random_button_3,
                "view_button" : self.ui.movies_view_3
            },
            "dont_want_to_continue": {
                "list": self.ui.movies_list_4,
                "search": self.ui.movies_search_4,
                "combobox": self.ui.movies_sort_by_4,
                "random_button": self.ui.movies_random_button_4,
                "view_button" : self.ui.movies_view_4
            },
            "watched": {
                "list": self.ui.movies_list_5,
                "search": self.ui.movies_search_5,
                "combobox": self.ui.movies_sort_by_5,
                "random_button": self.ui.movies_random_button_5,
                "view_button" : self.ui.movies_view_5
            },
            
        }


        # set up  widget:-
        self.ui.stacked_body_Widget.setCurrentIndex(0) # Home page

        #---------------------------- Set up buttons and shortcuts ----------------------

        self.ui.show_home.setChecked(True) # Home button is checked by default
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

        # make search bars not focus until it gets clicked
        for section_name, section_data in self.sections.items():
            search_widget = section_data["search"]
            search_widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Load movies data at startup
        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            loader = MovieListLoader(list_widget)
            self.section_loaders[section_name] = loader
            loader.load_from_section(section_name)

        # Show item info on click 
        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            list_widget.itemClicked.connect(
            lambda item, section=section_name: self.on_item_clicked(item, section) # When Qt emits itemClicked, it passes the clicked item — that becomes item.
            )
        
        # movies search icon
        for section_name, section_data in self.sections.items():
            search_line = section_data["search"]
            search_line.setHidden(True)

        #---------------------------- Set up View buttons --------------------------------------
                
        if self.settings.value("movie_view_mode", "list") == "list":
            for section_name, section_data in self.sections.items():
                view = section_data["view_button"]
                view.setChecked(True)
        else:
            for section_name, section_data in self.sections.items():
                view = section_data["view_button"]
                self.ui.movies_view_1.setChecked(False)

        # Connect all view_buttons to the same slot
        for section_name, section_data in self.sections.items():
            view_button = section_data["view_button"]
            view_button.toggled.connect(self.sync_view_buttons)



        #-------------------------- Setup Random buttons -------------------------------
        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            random_button = section_data["random_button"]
            random_button.clicked.connect(lambda checked=False, lw=list_widget: self.pick_random_movie(lw))

        #-------------------------- Setup Search buttons -------------------------------

        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            search_line = section_data["search"]
            search_line.textChanged.connect(lambda text, lw=list_widget: self.filter_list(text, lw))

        #-------------------------------Setup Sort_by box -------------------------------------------

        # Define the combo box options once
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

        # Configure all combo boxes in one loop
        for section_name, section_data in self.sections.items():
            combo_widget = section_data["combobox"]
            combo_widget.blockSignals(True)  # Prevent triggering signal while setting up # learn about it

            combo_widget.clear()
            combo_widget.addItems(options)

            # Restore saved sort option (if exists)
            saved_text = self.settings.value(f"{section_name}_sort_by_text")
            if saved_text:
                combo_widget.setCurrentText(saved_text)
            else:
                combo_widget.setCurrentIndex(-1)

            combo_widget.blockSignals(False)  # Re-enable signals

            # Connect the signal AFTER setup
            combo_widget.currentTextChanged.connect(
                lambda text, section=section_name: self.on_sort_changed(section, text)
            )


    # Slots:-----------------------------------------------------------------

    # set up side buttons:-
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

    
    def open_add_movie_window(self):
        # Open the Add Movie window as a modal dialog
        self.add_window = AddMovieWindow()  # Create a separate standalone window
        # Connect to the movie_added signal
        self.add_window.movie_added.connect(self.refresh_all_sections)

        self.add_window.exec()              # Use exec() for QDialog to make it modal( blocks interaction with other windows).
        # self.add_window.show()


    def on_item_clicked(self, item, section):
        # Open the movie info window for the selected item
        movie = item.data(Qt.UserRole)  # This returns a Movie object
        if movie and hasattr(movie, 'id'):
            self.selected_id = movie.id  # Get the actual ID from the Movie object
            self.show_movie_window = ShowMovieWindow(section=section, movie_id=self.selected_id)
            
            # Connect the refresh signals
            self.show_movie_window.movie_deleted.connect(self.refresh_all_sections)
            self.show_movie_window.movie_moved.connect(self.refresh_all_sections)


            self.show_movie_window.exec()
            
    def filter_list(self, text, list_widget):
        # Filter movies in the list based on the entered text
        text = text.strip().lower()
        
        # If search is empty, show all items
        if text == "":
            for i in range(list_widget.count()):
                item = list_widget.item(i)
                item.setHidden(False)
            return
        
        # If there's search text, filter items by TITLE and YEAR only
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            movie = item.data(Qt.UserRole)
            
            if movie and hasattr(movie, 'title'):
                # Search in title and year only
                name = str(movie.title or "").lower()
                year = str(movie.year or "").lower()
                
                # Combine only title and year for searching
                search_text = f"{name} {year}"
                
                # Show item if search text is found in title OR year
                item.setHidden(text not in search_text)
            else:
                # If no movie data, hide the item
                item.setHidden(True)


    def pick_random_movie(self, list_widget):
        "Picks a random movie from the given list"
        count = list_widget.count()
        if count == 0:
            QMessageBox.information(self, "No Movies", "This list is empty!")
            return
        
        # Pick a random index
        random_index = random.randint(0, count - 1)
        item = list_widget.item(random_index)

        # Scroll to and highlight the random movie
        list_widget.scrollToItem(item)
        item.setSelected(True)

        # Get the movie data using Qt.UserRole (not Qt.UserRole + 1)
        movie = item.data(Qt.UserRole)
        if movie and hasattr(movie, 'title'):
            movie_name = movie.title
            print(f"🎬 Random movie: {movie_name}")

            # Optional: show a popup
            QMessageBox.information(
                self,
                "Random Pick",
                f"🎬 Your random movie is:\n\n{movie_name}"
            )
        else:
            # Fallback if movie data is not found
            QMessageBox.information(
                self,
                "Random Pick",
                "🎬 Your random movie is:\n\nUnknown"
            )



    def on_sort_changed(self, section, sort_by):
        "Sort movies in the selected section based on the chosen criteria"        
        if sort_by == "Name (A-Z)":
            sort_key, reverse = "title", False
        elif sort_by == "Name (Z-A)":
            sort_key, reverse = "title", True
        elif sort_by == "Year (Newest-Oldest)":
            sort_key, reverse = "year", True
        elif sort_by == "Year (Oldest-Newest)":
            sort_key, reverse = "year", False
        elif sort_by == "IMDB Rating (High-Low)":
            sort_key, reverse = "rating", True
        elif sort_by == "IMDB Rating (Low-High)":
            sort_key, reverse = "rating", False
        elif sort_by == "User Rating (High-Low)":
            sort_key, reverse = "user_rating", True
        elif sort_by == "User Rating (Low-High)":
            sort_key, reverse = "user_rating", False
        else:
            return  # unknown option

        # Save user preference
        self.settings.setValue(f"{section}_sort_by_text", sort_by)
        self.settings.setValue(f"{section}_sort_by", sort_key)
        self.settings.setValue(f"{section}_sort_by_reverse", reverse)

        # Reload the list with sorting
        self.refresh_one_section(section, self.sections[section]["list"])


    def refresh_all_sections(self):
        "refres all list widgets"
        for section_name, section_data in  self.sections.items():
            loader= MovieListLoader(section_data["list"])
            loader.load_from_section(section_name)

    def refresh_one_section(self, section, list_widget):
        "Refresh one list widget with sorting"
        # Get saved sort preferences
        sort_key = self.settings.value(f"{section}_sort_by", "title")  # default to title
        reverse = self.settings.value(f"{section}_sort_by_reverse", False, type=bool)
        
        # Convert reverse to descending for the database query
        descending = bool(reverse)
        
        # Load with sorting
        loader = MovieListLoader(list_widget)
        loader.load_from_section(section, order_by=sort_key, descending=descending)
        



    def on_view_mode_changed(self, view_mode):
        """Update view mode using stored loaders"""
        for loader in self.section_loaders.values():
            loader.set_view_mode(view_mode)

    # Slot to sync all buttons
    def sync_view_buttons(self, checked):
        """Makes sure that all view buttons are sync"""
        for section_name, section_data in self.sections.items():
            view_button = section_data["view_button"]
            if view_button.isChecked() != checked:
                view_button.setChecked(checked)



    def set_profile_pic(self,label, url, size=50, radius=20):
        if not url:
            return
        
        try:
            # Download image
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            pixmap = QPixmap()
            pixmap.loadFromData(response.content)

            # Resize to a fixed size (square)
            pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

            # Create rounded mask
            rounded = QPixmap(size, size)
            rounded.fill(Qt.transparent)

            painter = QPainter(rounded)
            painter.setRenderHint(QPainter.Antialiasing)

            path = QPainterPath()
            path.addRoundedRect(0, 0, size, size, radius, radius)
            painter.setClipPath(path)

            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            # Set to QLabel
            label.setPixmap(rounded)
            label.setScaledContents(True)

        except Exception as e:
            print("Could not load profile picture:", e)





