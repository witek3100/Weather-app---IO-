import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from location import Location

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.location = Location()

        self.button = QtWidgets.QPushButton("Update")
        self.text = QtWidgets.QLabel(str(self.location.longitude), alignment=QtCore.Qt.AlignLeft)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())