from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QWidget, QHBoxLayout, QVBoxLayout, QLabel,QListWidget
from PySide6.QtGui import QPixmap
from app.utils.my_functions import link_to_image
import re
from app.models.movie import Movie



class MovieListItemWidget(QWidget):

    def __init__(self,movie : Movie,index: int=1, parent=None):
        super().__init__(parent)

        self.movie = movie
        self.index = index
        self.setup_ui()
        

    # ----------------------------------------------------------------
    # UI Setup
    # ----------------------------------------------------------------

    def setup_ui(self):

        m = self.movie
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)

        # ---------------------- Index label -----------------------
        index_label = QLabel(f"{self.index }-")
        index_label.setFixedWidth(50)
        index_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        index_label.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 18px;
                color: #aaaaaa;  
            }
        """)
        
        #---------------------------- Movie poster (from online link) ----------------------
        self.poster_label = QLabel()
        self.poster_label.setFixedSize(60, 90)
        self.poster_label.setAlignment(Qt.AlignCenter)
        self.poster_label.setStyleSheet("background-color: #222; border: 1px solid #555; color: gray;")
        link_to_image(m.poster_path,self.poster_label,60,90)

        # -------------------------------- Movie info -----------------------------------
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(15, 0, 0, 0)
        info_layout.setSpacing(2)  # Reduced spacing between info elements
        
        # ------------------------------ movie title --------------------------------------
        title_label = QLabel(m.title)
        title_label.setStyleSheet("color: #E0E6F0; font-weight: bold; font-size: 16px;")
        
        # ---------------------------- year,runtime widget -----------------------------------
        year_runtime_widget = QWidget()
        year_runtime_layout = QHBoxLayout(year_runtime_widget)
        year_runtime_layout.setContentsMargins(0, 0, 0, 0)
        year_runtime_layout.setSpacing(10)


        # ---------------------------------- Year ----------------------------------------------
        year_label = QLabel(f"({m.year})")
        year_label.setStyleSheet("color: #666; font-size: 14px;")
        

        #----------------------------------- Runtime -------------------------------------------
        
        runtime_label = QLabel(self.format_runtime(m.runtime))
        runtime_label.setStyleSheet("color: #666; font-size: 14px;")
        

        # ------------------- Layout --------------------------------

        year_runtime_layout.addWidget(year_label)
        year_runtime_layout.addWidget(runtime_label)
        year_runtime_layout.addStretch()
        
        info_layout.addWidget(title_label)
        info_layout.addWidget(year_runtime_widget)
        info_layout.addStretch()
        
        #------------------------ Rating-------------------------------

        # IMDb-like rating (yellow stars)
        rating_widget = self.create_rating_widget(m.imdb_rating, color="#aca13e",label_text="IMDB:-")

        # User rating (blue stars)
        user_rating_widget = self.create_rating_widget(m.user_rating, color="#2a418b",label_text="My Rating:-")

        # Combine both vertically
        all_rating_widget = QWidget()
        all_rating = QVBoxLayout(all_rating_widget)
        all_rating.setContentsMargins(0, 0, 0, 0)
        all_rating.addWidget(rating_widget)
        all_rating.addSpacing(4)
        all_rating.addWidget(user_rating_widget)

        #----------------------------- Add all widgets to main layout --------------------------------------

        layout.addWidget(index_label)  # Add index label first
        layout.addWidget(self.poster_label)
        layout.addWidget(info_widget)
        layout.addStretch()
        layout.addWidget(all_rating_widget)
        
        # Set hover effect and border
        self.setFixedHeight(100)
        # self.setStyleSheet("""
        #     MovieListItemWidget {
        #         border: 1px solid #333;
        #         border-radius: 4px;
        #         background-color: #1a1a1a;
        #     }
        #     MovieListItemWidget:hover {
        #         background-color: #2a2a2a;
        #         border: 1px solid #555;
        #     }
        # """)


    # ----------------------------------------------------------------
    # Helper functions
    # ----------------------------------------------------------------
    
    def format_runtime(self, runtime_value) -> str:
        """Converts runtime like '2h 10m', '130', or '1 hour 30 min' into '⏱️ Xh Ymin'."""
        if not runtime_value:
            return "⏱️ N/A"

        time_str = str(runtime_value).lower().strip()

        hours_match = re.search(r'(\d+)\s*(h|hour|hours)', time_str)
        minutes_match = re.search(r'(\d+)\s*(m|min|mins|minute|minutes)', time_str)

        total_minutes = 0

        if hours_match:
            total_minutes += int(hours_match.group(1)) * 60
        if minutes_match:
            total_minutes += int(minutes_match.group(1))
        if not hours_match and not minutes_match and time_str.isdigit():
            total_minutes = int(time_str)

        hours = total_minutes // 60
        remaining_minutes = total_minutes % 60

        return f"⏱️ {hours}h {remaining_minutes}min"


    def create_rating_widget(self, value, color="#B1BB1F", icon_path=None, label_text=None):
        """Create a star rating widget with optional icon and text label."""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setAlignment(Qt.AlignRight)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)  # small gap between items

        # Optional icon (like IMDb or user icon)
        if icon_path:
            icon_label = QLabel()
            pixmap = QPixmap(icon_path)
            icon_label.setPixmap(pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(icon_label)

        # Optional text beside icon (e.g. "IMDb" or "My Rate")
        if label_text:
            text_label = QLabel(label_text)
            text_label.setStyleSheet("font-weight: bold; font-size: 15px; color: #156919")
            layout.addWidget(text_label)

        # Handle missing or invalid rating values safely
        try:
            rating_value = float(value)
        except (ValueError, TypeError):
            rating_value = 0.0

        # Convert rating to star count (0–5 scale)
        stars_count = int(rating_value) if rating_value > 0 else 0
        stars_label = QLabel("★" * stars_count)
        stars_label.setStyleSheet(f"color: {color}; font-size: 20px;")

        # Numeric rating or "N/A"
        value_label = QLabel(str(value) if value else "N/A")
        value_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #aaa;")

        layout.addWidget(stars_label)
        layout.addWidget(value_label)

        return widget
    
    

           