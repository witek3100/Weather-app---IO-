import sys
import random
from PyQt6.QtWidgets import *
from location import Location

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.location = Location()

        self.frame = QtWidgets.QFrame()
        self.button = QtWidgets.QPushButton("Update")
        self.text_1 = QtWidgets.QLabel(str(self.location.longitude), alignment=QtCore.Qt.AlignLeft)
        self.text_2 = QtWidgets.QLabel(str(self.location.latitude), alignment=QtCore.Qt.AlignLeft)

        self.frame.drawFrame(QtWidgets.QStylePainter(self.text_1, self.text_2))

        self.layout = QtWidgets.QVBoxLayout(self)

        self.button.clicked.connect(self.magic)


    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = QWidget()