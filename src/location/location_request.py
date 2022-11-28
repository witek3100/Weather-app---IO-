import json
import requests
import re
import subprocess

api_url = "https://www.googleapis.com/geolocation/v1/geolocate?key="
api_key = "AIzaSyB1PUPXMdxyKLi3EdVufBQqWXbd-oIBxjs"

request = {'considerIp' : 'true'}

try:
    cmdout = subprocess.check_output('netsh wlan show networks mode=bssid').decode(encoding="437")
    mac_addresses = re.findall(r'(?:[0-9a-fA-F]:?){12}', cmdout)
    signals_quality = re.findall(r'([\d]+)(%)', cmdout)
    channels = re.findall(r'(Channel[\W]+: )([\d]+)', cmdout)
    if not (len(mac_addresses) == len(signals_quality) == len(channels)):
        pass
except:
    print("error")
else:
    wifi_list = []
    for i in range(len(mac_addresses)):
        wifi_list.append({'macAddress' : mac_addresses[i],
                          'signalStrength' : str(int(signals_quality[i][0])/2-100),
                          'channel' : channels[i][1]
                          })
    request['wifiAccessPoints'] = wifi_list



try:
    response = requests.post(api_url+api_key, json=request)
    data = response.json()
    if 'error' in data.keys():
        raise  requests.RequestException()
except Exception as e:
    print(e)
else:
    lat = data['location']['lat']
    lon = data['location']['lng']
    accuracy = data['accuracy']
    print(lat)
    print(lon)
    print(accuracy)


json_object = json.dumps(data, indent=3)
with open("loc.json", "w") as outfile:
    outfile.write(json_object)
