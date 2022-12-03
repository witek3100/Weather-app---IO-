
## Projekt Inżynieria Oprogramowania ISI2 - Desktopowa aplikacja z informacjami pogodowymi

* Witold Nowogórski
* Adam Pliszka
* Kaja Dzielnicka
* Bartłomiej Stępniewski
  
=======================================================================================
<pre>
├ src                           #folder źródłowy  
   ├── gui
   │    ├── gui.py
   │    └── main_window.py
   ├── location-api
   │      ├── location_request.py      # łączenie z google geolocation i geocoding api -> zapisywanie odpowiedzi do loc.json  
   │      └── loc.json               
   ├── weather-api                        
   │      ├── weather_data_request.py     # łączenie z open meteo api -> zapisywanie odpowiedzi do weather_data.json    
   │      └── weather_data.json
</pre>

 ### Struktura aplikacji 
 
 Aplikacja określa lokalizacje poprzez zewnętrzne api, następnie dla tej lub podanej przez użytkownika miejscowości z pomocą kolejnego api pobiera informacje pogodowe, które zostają odpowiednio przetworzone i wyświetlone w oknie aplikacji
 
 ![app structure diagram](https://github.com/witek3100/Weather-app-IO/blob/master/app_structure_diagram.png)
 
 ### Główne interfejsy
