from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from location import Location

def update():
    label.setText("Updated")


def retrieve():
    print(label.text())

location = Location()

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(100, 100, 700, 450)
win.setWindowTitle("Weather")

label = QtWidgets.QLabel(win)
label.setText("lon: " + str(location.longitude) + "\nlat:" + str(location.latitude) + "\ncity: " + str(location.city))
label.adjustSize()
label.move(10, 10)



win.show()
sys.exit(app.exec_())