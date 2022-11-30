from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow
from main_window import MainWindow
import os
import json

class Gui:
    def __init__(self):
        self.location = self.update_location()
        while True:
            app = QApplication([])
            app.setApplicationName("Weather Info")
            window = MainWindow()
            window.resize(500, 500)
            window.display_location(self.location)
            window.show()
            app.exec()

    def update_location(self):

        with open(os.path.relpath("../location/loc.json")) as loc_file:
            loc = json.load(loc_file)
        return [loc['location']['lat'],loc['location']['lng']]

if __name__ == "__main__":
    gui = Gui()