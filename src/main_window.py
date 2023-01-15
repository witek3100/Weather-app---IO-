from PyQt5 import QtCore, QtGui, QtWidgets
from weather_data_request import WeatherApi
from location_request import LocationApi
from cities_dict import cities
import time
import os
import json
import requests
import re
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        creating app GUI
        :param MainWindow: Main window QtWidget
        """

        """ size and background """
        MainWindow.setObjectName("Weather")
        MainWindow.setFixedSize(991, 719)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n""background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 112, 255, 255), stop:1 rgba(255, 255, 255, 255));\n""border-color: rgb(30, 100, 190);\n""}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        """ label displaying city name """
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(180, 60, 600, 81))
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setStyleSheet("font: 700 30pt \"Calibri\";\n""background-color: rgba(191, 64, 64, 2);\n""color: rgb(243, 243, 243);")
        self.city_label.setObjectName("city_label")

        """ upper bar """
        self.upper_bar = QtWidgets.QLabel(self.centralwidget)
        self.upper_bar.setGeometry(QtCore.QRect(-10, 0, 1001, 51))
        self.upper_bar.setStyleSheet("background-color:rgb(30, 100, 190)")
        self.upper_bar.setText("")
        self.upper_bar.setObjectName("label_2")

        """ buttons """
        self.settings_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.open_settings_window())
        self.settings_button.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.settings_button.setStyleSheet("background-color:rgb(100,200,250)")
        self.settings_button.setObjectName("pushButton")
        self.settings_button.setText('Settings')

        self.update_weather_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.update_weather(self.lat, self.lon))
        self.update_weather_button.clicked.connect(lambda: self.city_label.setText("Your Location"))
        self.update_weather_button.setGeometry(QtCore.QRect(140, 10, 121, 31))
        self.update_weather_button.setStyleSheet("background-color:rgb(100,200,250)")
        self.update_weather_button.setObjectName("pushButton_3")
        self.update_weather_button.setText('Your Location')

        self.Hourly_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.show_hourly_forecast())
        self.Hourly_button.setGeometry(QtCore.QRect(60, 470, 83, 29))
        self.Hourly_button.setStyleSheet("background-color:rgb(100,200,250)")
        self.Hourly_button.setObjectName("Hourly_button")
        self.Hourly_button.setText('Hourly')

        self.Daily_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.show_daily_forecast())
        self.Daily_button.setGeometry(QtCore.QRect(60, 510, 83, 29))
        self.Daily_button.setStyleSheet("background-color:rgb(100,200,250)")
        self.Daily_button.setObjectName("Daily_button")
        self.Daily_button.setText('Daily')

        self.search_bar = QtWidgets.QLineEdit(self.centralwidget, placeholderText=" search city")
        self.search_bar.setGeometry(QtCore.QRect(650, 10, 291, 31))
        completer = QtWidgets.QCompleter(cities)
        self.search_bar.setCompleter(completer)
        self.search_bar.setStyleSheet("background-color:rgb(130,200,250)")
        self.search_bar.setObjectName("lineEdit")

        self.search_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.show_weather_for_city())
        self.search_button.setGeometry(QtCore.QRect(950, 10, 31, 31))
        self.search_button.setStyleSheet("background-color:rgb(100,200,250)")
        self.search_button.setText("")
        self.search_button.setObjectName("seach_button")
        self.search_button.setIcon(QtGui.QIcon('../icons/search_button_icon.png'))

        """ current weather data labels """
        self.temperature_label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_label.setGeometry(QtCore.QRect(370, 130, 221, 101))
        self.temperature_label.setStyleSheet("font: 300 50pt \"Segoe UI Variable Display Light\";\n""color:rgb(255,255,255)")
        self.temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_label.setObjectName("temperature_label")

        self.wth = QtWidgets.QLabel(self.centralwidget)
        self.wth.setGeometry(QtCore.QRect(360, 240, 251, 41))
        self.wth.setStyleSheet("font: 20pt \"Calibri\";\n"
                               "color:rgb(255, 255, 255)")
        self.wth.setAlignment(QtCore.Qt.AlignCenter)
        self.wth.setObjectName("wth")

        self.current_data_label1 = QtWidgets.QLabel(self.centralwidget)
        self.current_data_label1.setGeometry(QtCore.QRect(250, 320, 461, 31))
        self.current_data_label1.setStyleSheet("color:rgb(255, 255, 255)")
        self.current_data_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.current_data_label1.setObjectName("current_data_label1")
        self.current_data_label1.setText("Wind  se 10ms       Visibility 10km       Barometer 1013 hpa")

        self.current_data_label2 = QtWidgets.QLabel(self.centralwidget)
        self.current_data_label2.setGeometry(QtCore.QRect(250, 290, 461, 31))
        self.current_data_label2.setStyleSheet("color:rgb(255, 255, 255)")
        self.current_data_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.current_data_label2.setObjectName("current_data_label2")
        self.current_data_label2.setText("Feels Like 24°C      Precipitation None        Humidity 80%")

        self.main_icon = QtWidgets.QLabel(self.centralwidget)
        self.main_icon.setGeometry(QtCore.QRect(230, 120, 141, 121))
        self.main_icon.setText("")
        self.main_icon.setObjectName("main_icon")

        self.current_location_label = QtWidgets.QLabel(self.centralwidget)
        self.current_location_label.setGeometry(QtCore.QRect(0, 700, 991, 21))
        self.current_location_label.setStyleSheet("background-color:rgba(30, 100, 190, 100);\n""font: 300 9pt \"Bahnschrift Light\";")
        self.current_location_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.current_location_label.setObjectName("label_4")
        self.current_location_label.setText(self.current_location_text)

        """ forecast data labels """
        self.frcs_label = QtWidgets.QLabel(self.centralwidget)
        self.frcs_label.setGeometry(QtCore.QRect(50, 410, 891, 221))
        self.frcs_label.setStyleSheet("background-color:rgba(30, 100, 190, 150);\n"
                                      "font: 300 9pt \"Bahnschrift Light\";\n"
                                      "border-radius:20px;")
        self.frcs_label.setText("")
        self.frcs_label.setObjectName("frcs_label")
        self.frcs_label.lower()

        self.forecast = QtWidgets.QLabel(self.centralwidget)
        self.forecast.setGeometry(QtCore.QRect(60, 430, 101, 31))
        self.forecast.setStyleSheet("font: 15pt \"Calibri\";\n""color:rgb(255, 255, 255)")
        self.forecast.setObjectName("forecast")
        self.forecast.setText('Forecast')

        self.hours = QtWidgets.QLabel(self.centralwidget)
        self.hours.setGeometry(QtCore.QRect(130, 530, 811, 20))
        self.hours.setStyleSheet("color:rgb(255,255,255);")
        self.hours.setObjectName("hours_2")
        self.hours.setText("                  3:00                        7:00                       11:00"
                             "                       15:00                       19:00                       23:00")

        self.hourly_temperatures = [QtWidgets.QLabel(self.centralwidget) for i in range(6)]
        for c, i in enumerate(self.hourly_temperatures):
            i.setGeometry(QtCore.QRect(208 + 123 * c, 510, 741, 20))
            i.setStyleSheet("font: 700 9pt \"Segoe UI\";""color: rgb(255,255,255)")
            i.setObjectName("hourly_temperature_{}".format(c+1))

        self.hourly_icons = [QtWidgets.QLabel(self.centralwidget) for i in range(6)]
        for c, i in enumerate(self.hourly_icons):
            i.setGeometry(QtCore.QRect(180 + c * 123, 440, 63, 51))
            i.setText("")
            i.setObjectName("h_icon_{}".format(c + 1))

        self.dates = QtWidgets.QLabel(self.centralwidget)
        self.dates.setGeometry(QtCore.QRect(130, 530, 738, 20))
        self.dates.setStyleSheet("color:rgb(255,255,255);")
        self.dates.setObjectName("dates_2")

        self.max_temperatures = [QtWidgets.QLabel(self.centralwidget) for i in range(6)]
        for c, i in enumerate(self.max_temperatures):
            i.setGeometry(QtCore.QRect(215 + c * 125, 510, 40, 20))
            i.setStyleSheet("font: 700 9pt \"Segoe UI\";""color: rgb(255,255,255)")
            i.setObjectName("max_temperature_{}".format(c+1))

        self.min_temperatures = [QtWidgets.QLabel(self.centralwidget) for i in range(6)]
        for c, i in enumerate(self.min_temperatures):
            i.setGeometry(QtCore.QRect(180 + c * 125, 510, 40, 20))
            i.setStyleSheet("font:10pt \"Calibri\";\n""color:rgb(172, 172, 172)")
            i.setObjectName("max_temperature_{}".format(c + 1))

        self.min = QtWidgets.QLabel(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(900, 500, 63, 21))
        self.min.setStyleSheet("font:9pt \"Calibri\";\ncolor:rgb(172, 172, 172)")
        self.min.setObjectName("min_4")
        self.min.setText('MIN')

        self.max = QtWidgets.QLabel(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(900, 520, 63, 21))
        self.max.setStyleSheet("font: 700 7pt \"Segoe UI\";color: rgb(255, 255, 255)")
        self.max.setObjectName("max")
        self.max.setText('MAX')

        self.daily_icons = [QtWidgets.QLabel(self.centralwidget) for i in range(6)]
        for c, i in enumerate(self.daily_icons):
            i.setGeometry(QtCore.QRect(180 + c * 123, 440, 63, 51))
            i.setText("")
            i.setObjectName("h_icon_{}".format(c + 1))

        self.actionChange_units = QtWidgets.QAction(MainWindow)
        self.actionChange_units.setObjectName("actionChange_units")
        self.actiontime_zone = QtWidgets.QAction(MainWindow)
        self.actiontime_zone.setObjectName("actiontime_zone")

        self.update_weather(self.lat, self.lon)
        self.show_daily_forecast()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_weather_for_city(self):
        city = self.search_bar.text()
        if not city in cities:
            self.current_location_label.setText("Unable to find this city...")
            return
        self.city_label.setText(city)
        self.update_weather(cities[city][0], cities[city][1])
        self.current_location_label.setText("{} : {} {}".format(city, cities[city][0], cities[city][1]))
    def update_weather(self, lat, lon):
        """
        updates lables displaying weather information
        :param lat
        :param lon
        """
        self.current_location_label.setText("{}   {}".format(lat, lon))
        """ get current weather """
        WeatherApi.get_weather(lat, lon)
        with open(os.path.relpath("weather_data.json")) as wth_file:
            self.weather = json.load(wth_file)
        t = time.localtime()
        hour = int(time.strftime("%H", t))

        """ set temperature label """
        self.temperature_label.setText("{}°C".format(self.weather["hourly"]["temperature_2m"][hour]))

        """ set wth label and main icon """
        clouds = self.weather["hourly"]["cloudcover"][hour]
        if 0 <= clouds < 10:
            self.wth.setText("Clear sky")
        elif 10 <= clouds < 30:
            self.wth.setText("Mostly clear")
        elif 30 <= clouds < 60:
            self.wth.setText("Partly clear")
        elif 60 <= clouds < 90:
            self.wth.setText("Broken clouds")
        elif 90 <= clouds <= 100:
            self.wth.setText("Overcast")
        rain = self.weather["hourly"]["rain"][hour]
        percipation = 0
        if rain > 0:
            self.wth.setText("Rain")
            percipation = rain
        snow = self.weather["hourly"]["snowfall"][hour]
        if snow > 0:
            self.wth.setText("Snow")
            percipation = snow
        pixmap2 = self.choose_icon('hourly', hour, small=False)
        self.main_icon.setPixmap(pixmap2)
        self.main_icon.resize(pixmap2.width(), pixmap2.height())

        """ set current_data_label1 """
        wind = self.weather["hourly"]["windspeed_10m"][hour]
        visibility = self.weather["hourly"]["visibility"][hour]
        barometer = self.weather["hourly"]["pressure_msl"][hour]
        self.current_data_label1.setText("Wind  {} km/h       Visibility {} m       Barometer {} hPa".format(wind, visibility, barometer))

        """ set current_data_label2 """
        feels_like = self.weather["hourly"]["apparent_temperature"][hour]
        humidity = self.weather["hourly"]["relativehumidity_2m"][hour]
        self.current_data_label2.setText("Feels Like {}°C      Precipitation {} mm       Humidity {}%".format(feels_like, percipation, humidity))

        """ set dates label"""
        self.dates.setText("                 {}                       {}                       {}"
                            "                       {}                       {}                       {}"
                            .format(self.weather['daily']['time'][1][8:10] + "." + self.weather['daily']['time'][1][5:7],
                                    self.weather['daily']['time'][2][8:10] + "." + self.weather['daily']['time'][2][5:7],
                                    self.weather['daily']['time'][3][8:10] + "." + self.weather['daily']['time'][3][5:7],
                                    self.weather['daily']['time'][4][8:10] + "." + self.weather['daily']['time'][4][5:7],
                                    self.weather['daily']['time'][5][8:10] + "." + self.weather['daily']['time'][5][5:7],
                                    self.weather['daily']['time'][6][8:10] + "." + self.weather['daily']['time'][6][5:7]))

        """ set hourly temperature labels """
        for c, i in enumerate(self.hourly_temperatures):
            i.setText("{}°C".format(int(self.weather['hourly']['temperature_2m'][3+c*4])))

        """ set max temperature labels """
        for c, i in enumerate(self.max_temperatures):
            i.setText("{}°C".format(int(self.weather['daily']['temperature_2m_max'][c+1])))

        """ set min temperature labels """
        for c, i in enumerate(self.min_temperatures):
            i.setText("{}°C".format(int(self.weather['daily']['temperature_2m_min'][c+1])))

        """ set daily forecast icons """
        for c, i in enumerate(self.daily_icons):
            pixmap = self.choose_icon('daily', c+1)
            i.setPixmap(pixmap)
            i.resize(pixmap.width(), pixmap.height())

        """ set hourly forecast icons """
        for c, i in enumerate(self.hourly_icons):
            pixmap = self.choose_icon('hourly', 3+4*c)
            i.setPixmap(pixmap)
            i.resize(pixmap.width(), pixmap.height())

    def reload_location(self):
        """
        reloads location data by running script from
         location_request and reading data from loc.json
        """
        try:
            LocationApi.get_location()
            with open(os.path.relpath("loc.json")) as loc_file:
                loc = json.load(loc_file)
                self.lat = loc["results"][1]['geometry']['location']['lat']
                self.lon = loc["results"][1]['geometry']['location']['lng']
        except:
            self.current_location_text = "UNABLE TO GET YOUR LOCATION"
        else:
            self.current_location_text = "YOUR CURRENT LOCATION: {}   {}".format(self.lat, self.lon)


    def show_daily_forecast(self):
        """
        shows daily forecast and hides hourly
        """
        """hide hourly"""
        self.hours.hide()
        for i in self.hourly_temperatures:
            i.hide()
        for i in self.hourly_icons:
            i.hide()
        """show daily"""
        self.max.show()
        self.min.show()
        self.dates.show()
        for i in self.min_temperatures:
            i.show()
        for i in self.max_temperatures:
            i.show()
        for i in self.daily_icons:
            i.show()

    def show_hourly_forecast(self):
        """
        shows hourly forecast and hides daily
        """
        """hide daily"""
        self.max.hide()
        self.min.hide()
        self.dates.hide()
        for i in self.min_temperatures:
            i.hide()
        for i in self.max_temperatures:
            i.hide()
        for i in self.daily_icons:
            i.hide()
        """show hourly"""
        self.hours.show()
        for i in self.hourly_temperatures:
            i.show()
        for i in self.hourly_icons:
            i.show()
            
    def choose_icon(self, dh, x, small=True):
        """
        function choose icon from icons folder for icon label pixmap
        :param dh: daily or hourly forecast
        :param x: position of weather data in json file
        :param small: if true returns small icon (for forecast labels) else returns normal icon (for main icon label)
        :return:
        """
        add_str = "_small" if small else ""
        if dh == "daily":
            if self.weather[dh]["precipitation_hours"][x] < 3:
                return QtGui.QPixmap('../icons/sun_small.png')
            if 3 <= self.weather[dh]["precipitation_hours"][x] < 6:
                return QtGui.QPixmap('../icons/few_clouds_small.png')
            if 6 <= self.weather[dh]["precipitation_hours"][x]:
                return QtGui.QPixmap('../icons/rain_day_small.png')
        if dh == "hourly":
            if self.weather[dh]["precipitation"][x] > 1:
                return QtGui.QPixmap('../icons/rain_day{}.png'.format(add_str))
            if self.weather[dh]["cloudcover"][x] < 20:
                return QtGui.QPixmap('../icons/sun{}.png'.format(add_str))
            if 20 <= self.weather[dh]["cloudcover"][x] < 80:
                return QtGui.QPixmap('../icons/few_clouds{}.png'.format(add_str))
            if self.weather[dh]["cloudcover"][x] >= 80:
                return QtGui.QPixmap('../icons/ovc_clouds{}.png'.format(add_str))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather"))
        self.city_label.setText(_translate("MainWindow", "Your Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.reload_location()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
