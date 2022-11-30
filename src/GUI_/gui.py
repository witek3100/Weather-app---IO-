from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow
from main_window import MainWindow
import os
import json

class Gui:
    def __init__(self):
        while True:
            app = QApplication([])
            app.setApplicationName("Weather Info")
            window = MainWindow()
            window.resize(800, 500)
            window.show()
            app.exec()

if __name__ == "__main__":
    gui = Gui()