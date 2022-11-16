import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtWidgets

from location import Location

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.location = Location()
        self.initUI()


    def initUI(self):
        from PyQt5 import QtWidgets
        from PyQt5.QtWidgets import QApplication, QMainWindow
        import sys

        def update():
            label.setText("Updated")

        def retrieve():
            print(label.text())

        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(400, 400, 500, 300)
        win.setWindowTitle("CodersLegacy")

        label = QtWidgets.QLabel(win)
        label.setText("GUI application with PyQt5")
        label.adjustSize()
        label.move(100, 100)

        button = QtWidgets.QPushButton(win)
        button.clicked.connect(update)
        button.setText("Update Button")
        button.move(100, 150)

        button2 = QtWidgets.QPushButton(win)
        button2.clicked.connect(retrieve)
        button2.setText("Retrieve Button")
        button2.move(100, 200)

        win.show()
        sys.exit(app.exec_())