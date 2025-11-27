from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import QWidget
from pathlib import Path
from py_ui.sign_in_widget import DarkGoogleSignIn
from app.auth.google_auth import GoogleAuth, get_user_info
from app.sync.drive_sync import sync_on_login
from app.windows.main_widget import Widget
from app.db.sqlite_manger import init_db
from app.auth.google_auth import get_user_info
import json

LOCAL_DB_PATH = Path.cwd() / "data" / "movies.db"
LOCAL_DB_PATH.parent.mkdir(parents=True, exist_ok=True)


class SignIn(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = DarkGoogleSignIn()
        self.setWindowTitle("Sign In")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #121212;")
        self.hide()
        layout = self.ui.layout()
        self.setLayout(layout)
        self.logic()

        self.ui.google_btn.clicked.connect(lambda: self.sign_in(True))


    def log_in(self):
        try:
            auth = GoogleAuth()
            creds = auth.login()
            if creds and creds.valid:
                print("Auto-login successful inside SignIn widget. Emitting success...")
                

                with open("log", "w", encoding="utf-8") as f:
                    f.write(json.dumps(get_user_info(creds), ensure_ascii=False, indent=2))


                return True
            else:
                print("No saved login or token invalid inside SignIn widget. Emitting failure...")

                return False
        except Exception as e:
            print(f"Auto-login error inside SignIn widget: {e}")
            return False


    def sign_in(self, success):
        """Called when authentication completes"""
        if success:
            try:
                # Get user info
                auth = GoogleAuth()
                creds = auth.sign_in() # You can reuse creds from worker if stored
                user = get_user_info(creds)
                if user:
                    print("User info:", user)

                # Sync DB
                result = sync_on_login(creds, str(LOCAL_DB_PATH))
                print("Sync result:", result)
                print("Sign-in successful.")

                with open("log", "w", encoding="utf-8") as f:
                    f.write(json.dumps(get_user_info(creds), ensure_ascii=False, indent=2))
                    
                self.start_main_app()
                
            except Exception as e:
                print(f"Post-auth error: {e}")
                success = False
        else:
            print("Sign-in failed.")

        # Reset button
        self.ui.google_btn.setText("Sign in with Google")
        self.ui.google_btn.setEnabled(True)


    def logic(self):
        signal = self.log_in()
  
        print(signal)
        if signal == True:
            self.start_main_app()

        else:
            self.show()


    def start_main_app(self):
        main_window = Widget()
        main_window.show()
        self.close()