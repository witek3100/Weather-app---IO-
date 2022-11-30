from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
sys.path.append("C:/Users/witek/PycharmProjects/WeatherApp/src/location")
sys.path.append("C:/Users/witek/PycharmProjects/WeatherApp/src/weather-api")
import location_request
import weather_data_request
import os
import json

class MainWindow(QMainWindow):
    def __init__(self):
        self.location = self.update_location()
        self.city = 'KRAKÓW'
        self.get_weather()
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon("sun.png"))
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Weather app")
        self.display_location(self.location)
        self.UiComponents()

    def display_location(self, loc):
        loc_label = QLabel(self)
        loc_label.setGeometry(10, 470, 500, 20)
        loc_label.setText("your current location: " + str(loc[0]) + " " + str(loc[1]))
        loc_label.setAlignment(Qt.AlignLeft)
        self.vbox.addWidget(loc_label)

    def UiComponents(self):

        update_loc_button = QPushButton('update location', self)
        update_loc_button.move(300, 462)
        update_loc_button.clicked.connect(self.update_location)

        set_manually_button = QPushButton('set manually', self)
        set_manually_button.move(400, 462)
        set_manually_button.clicked.connect(self.set_location_manualy)

        update_weather_button = QPushButton('update weather', self)
        update_weather_button.move(500, 462)
        update_weather_button.clicked.connect(self.get_weather)

        settings_button = QPushButton('settings', self)
        settings_button.move(650, 20)
        settings_button.clicked.connect(self.open_settings_window)

        current_weather_label = QLabel(self)
        current_weather_label.setGeometry(40, 40, 600, 70)
        current_weather_label.setText("CURRENT WEATHER FOR " + str(self.city))
        current_weather_label.setFont(QFont('Arial', 20))
        self.vbox.addWidget(current_weather_label)

        current_temp_label = QLabel(self)
        current_temp_label.setGeometry(45, 80, 400, 100)
        current_temp_label.setText("temperature: " + str(self.temp))
        current_temp_label.setFont(QFont('Arial', 10))
        self.vbox.addWidget(current_weather_label)

        current_cloud_cover_label = QLabel(self)
        current_cloud_cover_label.setGeometry(45, 110, 400, 100)
        current_cloud_cover_label.setText("cloud cover: " + str(self.cloud_cover) + "%")
        current_cloud_cover_label.setFont(QFont('Arial', 10))
        self.vbox.addWidget(current_cloud_cover_label)

        wind_label = QLabel(self)
        wind_label.setGeometry(45, 140, 400, 100)
        wind_label.setText("wind: " + str(self.wind) + "km/h")
        wind_label.setFont(QFont('Arial', 10))
        self.vbox.addWidget(current_cloud_cover_label)

        forecast_label = QLabel(self)
        forecast_label.setGeometry(45, 200, 400, 100)
        forecast_label.setText("FORECAST: ")
        forecast_label.setFont(QFont('Arial', 15))
        self.vbox.addWidget(forecast_label)

        time_zone_label = QLabel(self)
        time_zone_label.setGeometry(620, 5, 200, 15)
        time_zone_label.setText("time zone:  " + str(self.time_zone))
        time_zone_label.setFont(QFont('Arial', 8))
        self.vbox.addWidget(time_zone_label)

        forecast_temp_label = QLabel(self)
        forecast_temp_label.setGeometry(45, 300, 600, 15)
        forecast_temp_label.setText("temp:    " + str(self.temp_forecast[0]) +
                                    "               " + str(self.temp_forecast[1]) +
                                    "               " + str(self.temp_forecast[2]) +
                                    "               " + str(self.temp_forecast[3]) +
                                    "               " + str(self.temp_forecast[4]) +
                                    "               " + str(self.temp_forecast[5]) +
                                    "               " + str(self.temp_forecast[6]))
        forecast_temp_label.setFont(QFont('Arial', 8))
        self.vbox.addWidget(forecast_temp_label)

        forecast_days_label = QLabel(self)
        forecast_days_label.setGeometry(45, 280, 600, 15)
        forecast_days_label.setText(
            "day:  " + str(self.forecast_days[0]) + "   " + str(self.forecast_days[1]) + "   " + str(
                self.forecast_days[2]) + "   " + str(self.forecast_days[3]) + "   " + str(
                self.forecast_days[4]) + "   " + str(self.forecast_days[5]) + "   " + str(
                self.forecast_days[6]) + "   ")
        forecast_temp_label.setFont(QFont('Arial', 8))
        self.vbox.addWidget(forecast_temp_label)

        self.setLayout(self.vbox)

    def update_location(self):
        location_request.get_location()
        with open(os.path.relpath("loc.json")) as loc_file:
            loc = json.load(loc_file)
        return [loc['location']['lat'],loc['location']['lng']]

    def get_weather(self):
        weather_data_request.get_weather()
        with open(os.path.relpath("../weather-api/weather_data.json")) as loc_file:
            wth = json.load(loc_file)
        self.temp = wth['hourly']['temperature_2m'][0]
        self.cloud_cover = wth['hourly']['cloudcover'][0]
        self.wind = wth['hourly']['windspeed_10m'][0]
        self.time_zone = wth['timezone']
        self.temp_forecast = wth['daily']['temperature_2m_max']
        self.forecast_days = wth['daily']['time']
    def set_location_manualy(self):
        lat = input('lat:')
        lon = input('lon:')
        self.location = [lat][lon]

    def open_settings_window(self):
        pass
