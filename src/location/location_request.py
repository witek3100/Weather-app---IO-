import json
import requests
import re
import subprocess

api_url = "https://www.googleapis.com/geolocation/v1/geolocate?key="    #adres url do google geolocation api
api_key = "AIzaSyB1PUPXMdxyKLi3EdVufBQqWXbd-oIBxjs"                     #klucz api  (konto wnowogorski10@gmail.com)
complete_api_url = api_url + api_key

request = {'considerIp' : 'true'}   #zapytanie które zostanie wysłane na 'complete_api_url'

### TWORZENIE ZAPYTANIA ###
try:
    cmdout = subprocess.check_output('netsh wlan show networks mode=bssid').decode(encoding="437")      #zwraca dostępne wifi-access-pointy
    mac_addresses = re.findall(r'(?:[0-9a-fA-F]:?){12}', cmdout)    #\
    signals_quality = re.findall(r'([\d]+)(%)', cmdout)              #| parsowanie cmdout przy użyciu wyrażeń regularnych
    channels = re.findall(r'(Channel[\W]+: )([\d]+)', cmdout)       #/
    if not (len(mac_addresses) == len(signals_quality) == len(channels)):      #musi się zgadzac ilość adresów mac i odpowiadających im wartości jakości sygnału
        raise ("error")
except:
    print("Unable to retrive wifi access points...")
else:
    wifi_list = []                          #lista dostępnych punktów wifi
    for i in range(len(mac_addresses)):                     # pętla for uzupełnia wifi_list wartościami pobranymi przez komendę netsh (linia 13)
        wifi_list.append({'macAddress' : mac_addresses[i],
                          'signalStrength' : str(int(signals_quality[i][0])/2-100),
                          'channel' : channels[i][1]
                          })
    request['wifiAccessPoints'] = wifi_list        #dodawanie wifi_list do zapytania


### OTRZYMYWANIE ODPOWIEDŹI ###

try:
    response = requests.post(complete_api_url, json=request)
    loc = response.json()
    if 'error' in loc.keys():
        raise  requests.RequestException()
except Exception as e:
    print(e)
else:
    json_object = json.dumps(loc, indent=3)     #wrzucanie odpowiedzi do pliku json
    with open("loc.json", "w") as outfile:
        outfile.write(json_object)
