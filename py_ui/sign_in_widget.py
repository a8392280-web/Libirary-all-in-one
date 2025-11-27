import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QLabel, QPushButton)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPixmap

class DarkGoogleSignIn(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(30)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel("Welcome")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #ffffff;
                margin-bottom: 10px;
            }
        """)
        
        # Google sign-in button
        self.google_btn = QPushButton(" Sign in with Google")
        self.google_btn.setCursor(Qt.PointingHandCursor)
        self.google_btn.setFixedSize(250, 50)
        
        # Style the button - ALL styles in one place
        self.google_btn.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                padding: 12px 20px;
            }
            QPushButton:hover {
                background-color: #3367d6;
            }
            QPushButton:pressed {
                background-color: #2851a3;
            }
        """)
        
        # Add to layout
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(self.google_btn, 0, Qt.AlignCenter)
        layout.addStretch()
        
        self.setLayout(layout)
        
        # Window setup
        self.setWindowTitle("Sign In")
        self.setFixedSize(350, 300)
        self.setStyleSheet("background-color: #1a1a1a;")
        
