import sys

from PySide6 import QtWidgets
from app.controllers.main_widget import Widget
from app.db.sqlite_manger import init_db
init_db()
app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show() 

app.exec()


