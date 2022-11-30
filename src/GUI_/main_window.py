from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon("icons\sun.png"))
        self.setWindowTitle("Weather app")

    def display_location(self, loc):
        loc_label = QLabel(self)
        loc_label.setGeometry(10, 470, 500, 20)
        loc_label.setText("your current location: " + str(loc[0]) + " " + str(loc[1]))
        loc_label.setAlignment(Qt.AlignLeft)
        vbox = QVBoxLayout()
        vbox.addWidget(loc_label)
        self.setLayout(vbox)

