import json
import requests
import re
import subprocess
import os


# z loc.json odczytujemy lokalizacje dla jekiej pobieramy informacje
with open(os.path.relpath("../WeatherApp/src/location/loc.json")) as loc_file:
    loc = json.load(loc_file)

lat = loc["results"][1]['geometry']['location']['lat']
lon = loc["results"][1]['geometry']['location']['lng']

#adres url open meteo api
API_URL = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,' \
          'dewpoint_2m,apparent_temperature,precipitation,rain,showers,snowfall,snow_depth,freezinglevel_height,weatherc' \
          'ode,pressure_msl,surface_pressure,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,visibility,evapotr' \
          'anspiration,windspeed_10m,windspeed_80m,windgusts_10m,temperature_80m&daily=weathercode,temperature_2m_max,te' \
          'mperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,rain_sum,' \
          'showers_sum,snowfall_sum,precipitation_hours,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&timezone=auto'
def get_weather():
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

get_weather()