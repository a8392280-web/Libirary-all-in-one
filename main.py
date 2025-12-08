import sys
from PySide6 import QtWidgets
from app.windows.main_widget import Widget
from app.windows.sign_in_widget import SignIn
from app.auth.google_auth import GoogleAuth 
from app.sync.drive_sync import build_drive_service, upload_db
from pathlib import Path
import socket
from app.db.sqlite_manger import init_db
LOCAL_DB_PATH = Path.cwd() / "data"


# def has_internet():
#     try:
#         # Connect to DNS server of Google
#         socket.create_connection(("8.8.8.8", 53), timeout=3)
#         return True
#     except OSError:
#         return False

# print(has_internet())




# # ONLINE
# if __name__ == "__main__":

#     if has_internet():
#         app = QtWidgets.QApplication(sys.argv)
#         sign_in = SignIn()
#         app.exec()
        
#         try:
#             service = build_drive_service(GoogleAuth().login()) 
#             response = upload_db(service, "data/movies.db", "movies.db") 
#             print("DB uploaded successfully:", response) 
#         except Exception as e: 
#             print("DB upload failed:", e)
            

# OFFLINE     
    # else:
print("No internet connection. Running in offline mode.")
init_db()
app = QtWidgets.QApplication(sys.argv)
main_widget = Widget()
main_widget.show()
app.exec()
sys.exit()


