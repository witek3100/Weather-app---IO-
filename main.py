from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from location import Location

class Main:

    def __init__(self):
        self.location = Location()
        self.city = self.location.city
        self.main()

    def main(self):
        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(100, 100, 700, 450)
        win.setWindowTitle("Weather")

        loc_label = QtWidgets.QLabel(win)
        loc_label.setText("show weather for: ")
        loc_label.adjustSize()
        loc_label.move(150, 10)

        city_search = QtWidgets.QLineEdit(win)
        city_search.setFixedWidth(300)
        city_search.move(150, 30)

        button_search = QtWidgets.QPushButton(win)
        button_search.setText("Search")
        button_search.clicked.connect(self.search_city)
        button_search.move(470, 30)

        update_button = QtWidgets.QPushButton(win)
        update_button.setText("update")
        update_button.resize(60, 20)
        update_button.clicked.connect(self.update_location)
        update_button.move(245, 425)

        loc_label = QtWidgets.QLabel(win)
        loc_label.setText(
            "current location: " + str(self.location.longitude) + "   " + str(self.location.latitude))
        loc_label.adjustSize()
        loc_label.move(10, 430)

        current_weather_lebel = QtWidgets.QLabel(win)
        current_weather_lebel.setText(
            "current weather for " + str(self.location.city) + ": ")
        current_weather_lebel.setFont(QFont('Arial', 20))
        current_weather_lebel.resize(500, 100)
        current_weather_lebel.move(150, 35)


        win.show()
        sys.exit(app.exec_())

    def display(self):


    def search_city(self):
        pass

    def update_location(self):
        self.location = Location()

Main()