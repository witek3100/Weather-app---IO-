import requests


class Location:

    def __init__(self):
        self.ip = self.get_ip()
        response = requests.get(f'https://ipapi.co/{self.ip}/json/').json()     # api do przetworzenia adresu ip na lokalizacje

        self.latitude = response.get("latitude")     #
        self.longitude = response.get("longitude")    #   Odczyt najważniejszych informacji z response
        self.city = response.get("city")             #

    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()     # api do pobrania adresu ip
        return response["ip"]

    def show(self):
        print(self.ip, [self.latitude, self.longitude], self.city)

