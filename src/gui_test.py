import sys
import json
import requests
import re
import subprocess
import os
import unittest
import gui
from PyQt5.QtGui import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt



def test_show_weather_for_city(self):
    self.search_bar.setText("Kraków")
    self.show_weather_for_city()
    self.assertEqual(self.city_label.text(), "Kraków")
    self.assertEqual(self.current_location_label.text(), "Kraków : 50.06143, 19.93658")

    self.search_bar.setText("Bydgoszcz")
    self.show_weather_for_city()
    self.assertEqual(self.city_label.text(), "Bydgoszcz")
    self.assertEqual(self.current_location_label.text(), "Bydgoszcz : 53.1235, 18.00762")

    self.search_bar.setText("Łódź")
    self.show_weather_for_city()
    self.assertEqual(self.city_label.text(), "Łódź")
    self.assertEqual(self.current_location_label.text(), "Łódź : 51.77058, 19.47395")

    self.search_bar.setText("Sdasxcas234%#!@^%&^$&*:{.]l;")
    self.show_weather_for_city()
    self.assertEqual(self.current_location_label.text(), "Unable to find this city...")

def test_reload_location(self):
    self.assertEqual(self.lat, loc["results"][1]['geometry']['location']['lat'])

def test_show_daily_forecast(self):
    self.show_daily_forecast()
    self.assertTrue(self.hours.isHidden())
    self.assertFalse(self.max.isHidden())
    self.assertFalse(self.min.isHidden())
    self.assertFalse(self.dates.isHidden())
    for i in self.hourly_temperatures:
        self.assertTrue(i.isHidden())
    for i in self.hourly_icons:
        self.assertTrue(i.isHidden())
    for i in self.min_temperatures:
       self.assertFalse(i.isHidden())
    for i in self.max_temperatures:
        self.assertFalse(i.isHidden())
    for i in self.daily_icons:
        self.assertFalse(i.isHidden())

def test_show_hourly_forecast(self):
    self.show_hourly_forecast()
    self.assertFalse(self.hours.isHidden())
    self.assertTrue(self.max.isHidden())
    self.assertTrue(self.min.isHidden())
    self.assertTrue(self.dates.isHidden())
    for i in self.hourly_temperatures:
        self.assertFalse(i.isHidden())
    for i in self.hourly_icons:
        self.assertFalse(i.isHidden())
    for i in self.min_temperatures:
       self.assertTrue(i.isHidden())
    for i in self.max_temperatures:
        self.assertTrue(i.isHidden())
    for i in self.daily_icons:
        self.assertTrue(i.isHidden())

def test_choose_icon(self):
    self.reloead_location()
    self.update_weather(self.lat, self.lon)

    if self.weather["daily"]["precipitation_hours"][0] < 3:
        self.assertEqual(self.choose_icon(dh="daily", x=0), QtGui.QPixmap('../icons/sun_small.png'))
    if 3 <= self.weather["daily"]["precipitation_hours"][0] < 6:
        self.assertEqual(self.choose_icon(dh="daily", x=0), QtGui.QPixmap('../icons/few_clouds_small.png'))
    if 6 <= self.weather["daily"]["precipitation_hours"][0]:
        self.assertEqual(self.choose_icon(dh="daily", x=0), QtGui.QPixmap('../icons/rain_day_small.png'))


