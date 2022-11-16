import requests


class Location:

    def __init__(self):
        self.ip = self.get_ip()
        response = requests.get(f'https://ipapi.co/{self.ip}/json/').json()
        self.latitude = response.get("latitude")
        self.longitude = response.get("longitude")
        self.city = response.get("city")

    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

    def show(self):
        print(self.ip, [self.latitude, self.longitude], self.city)

