import json
import requests
import re
import subprocess
import os


class WeatherApi:
    @staticmethod
    def get_weather(lat, lon):
        """
        fetching weather data from open-meteo api to weather_data.json
        :param lat: latitude of location
        :param lon: longtitude of location
        """
        # adres url open meteo api
        API_URL = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,' \
                  'dewpoint_2m,apparent_temperature,precipitation,rain,showers,snowfall,snow_depth,freezinglevel_height,weatherc' \
                  'ode,pressure_msl,surface_pressure,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,visibility,evapotr' \
                  'anspiration,windspeed_10m,windspeed_80m,windgusts_10m,temperature_80m&daily=weathercode,temperature_2m_max,te' \
                  'mperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,rain_sum,' \
                  'showers_sum,snowfall_sum,precipitation_hours,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&timezone=auto'

        try:
            response = requests.get(API_URL)  # wysylanie zapytania
            loc = response.json()
            if 'error' in loc.keys():
                raise requests.RequestException()
        except Exception as e:
            print(e)
        else:
            json_object = json.dumps(loc, indent=3)
            with open("weather_data.json", "w") as outfile:          #wrzucanie odpowiedzi do pliku json
                outfile.write(json_object)


