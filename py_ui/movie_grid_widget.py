# movie_list_widget.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout
from app.utils.my_functions import link_to_image
from app.models.movie import Movie

class MovieGridItemWidget(QFrame):
    """Widget for grid view (Netflix style) using QFrame."""

    def __init__(self, movie: Movie, index: int = 1, parent=None):
        super().__init__(parent)
        self.movie = movie
        self.index = index
        self.is_pressed = False
        self.setup_ui()

    def setup_ui(self):
        m = self.movie
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignTop)

        # Create overlay container for poster
        poster_container = QFrame()
        poster_container.setFixedSize(150, 225)
        poster_layout = QVBoxLayout(poster_container)
        poster_layout.setContentsMargins(0, 0, 0, 0)
        poster_layout.setSpacing(0)

        # Poster
        self.poster_label = QLabel()
        self.poster_label.setFixedSize(150, 225)
        self.poster_label.setAlignment(Qt.AlignCenter)
        self.poster_label.setStyleSheet("""
            QLabel {
                background-color: #222; 
                border: none; 
            }
        """)
        link_to_image(m.poster_path, self.poster_label, 150, 225)

        # Use overlay layout
        poster_layout.addWidget(self.poster_label)

        # Title
        title_label = QLabel(m.title)
        title_label.setAlignment(Qt.AlignLeft)
        title_label.setStyleSheet("""
            QLabel {
                color: #b1bac1;
                font-family: "Roboto";
                font-size: 12px;
                font-weight: bold;
                background: transparent;
            }
        """)
        title_label.setWordWrap(True)
        title_label.setMaximumHeight(40)

        # Rating and Year row
        info_row = QFrame()
        info_row.setStyleSheet("background: transparent;")
        info_layout = QHBoxLayout(info_row)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(8)

        # Rating - left aligned
        rating_label = QLabel(f"⭐ {m.imdb_rating if m.imdb_rating else 'N/A'}")
        rating_label.setAlignment(Qt.AlignLeft)
        rating_label.setStyleSheet("""
            QLabel {
                color: #b1bac1;
                font-family: "Roboto";
                font-size: 12px;
                background: transparent;
            }
        """)

        # Year - right aligned
        year_label = QLabel(str(m.year))
        year_label.setAlignment(Qt.AlignRight)
        year_label.setStyleSheet("""
            QLabel {
                color: #b1bac1;
                font-family: "Roboto";
                font-size: 12px;
                background: transparent;
                font-weight: bold;
            }
        """)

        # Add rating (left) and year (right) to the info row
        info_layout.addWidget(rating_label)  # Left side
        info_layout.addStretch()             # Pushes year to the right
        info_layout.addWidget(year_label)    # Right side

        layout.addWidget(poster_container)
        layout.addWidget(title_label)
        layout.addWidget(info_row)

        # Grid item styling - Transparent with subtle hover and press effects
        self.setFixedSize(170, 300)
        self.setFrameStyle(QFrame.NoFrame)
        self.apply_normal_style()

    def apply_normal_style(self):
        """Apply normal (non-pressed) styling."""
        self.setStyleSheet("""
            MovieGridItemWidget {
                background-color: transparent;
                border: 1px solid transparent;
                border-radius: 8px;
            }
            MovieGridItemWidget:hover {
                background-color: rgba(39, 48, 58, 0.3);
                border: 1px solid rgba(79, 90, 101, 0.5);
            }
        """)

    def apply_pressed_style(self):
        """Apply pressed styling with white transparent overlay."""
        self.setStyleSheet("""
            MovieGridItemWidget {
                background-color: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 8px;
            }
        """)

    def mousePressEvent(self, event):
        """Handle mouse press event."""
        self.is_pressed = True
        self.apply_pressed_style()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """Handle mouse release event."""
        self.is_pressed = False
        self.apply_normal_style()
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        """Handle mouse move event."""
        if self.is_pressed:
            # If mouse moves outside while pressed, revert to normal style
            if not self.rect().contains(event.pos()):
                self.is_pressed = False
                self.apply_normal_style()
        super().mouseMoveEvent(event)