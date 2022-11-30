from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow
from main_window import MainWindow


class Gui:

    location =

    def __init__(self):
        while True:
            app = QApplication([])
            app.setApplicationName("Weather Info")
            window = MainWindow()
            window.resize(500, 500)
            window.display_location("loc")
            window.show()
            app.exec()

    def update_location():



if __name__ == "__main__":
    gui = Gui()