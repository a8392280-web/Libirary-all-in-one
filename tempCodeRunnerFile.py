print("No internet connection. Running in offline mode.")
init_db()
app = QtWidgets.QApplication(sys.argv)
main_widget = Widget()
main_widget.show()
app.exec()
sys.exit()

