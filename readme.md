
## Projekt Inżynieria Oprogramowania ISI2 - aplikacja z informacjami pogodowymi

* Witold Nowogórski
* Adam Pliszka
* Kaja Dzielnicka
* Bartłomiej Stępniewski

# URUCHAMIANIE #
```
git clone https://github.com/witek3100/Weather-app-IO/edit/master/readme.md
```  
- Windows
plik WeatherApp otwiera aplikacje 
lub 

```
python ../WeatherApp/src/gui.py

```

- Linux 
```
python ../WeatherApp/src/gui.py

```

=======================================================================================
<pre>
├ icons             #ikony używane przez aplikacje
├ src                           #folder źródłowy  
   ├── gui.py     - interfejs użytkownika
   ├── location_request.py     - pobieranie lokalilizacji przy użyciu google geolocation api         
   ├── weather_data_request.py       - pobierania informacji pogodowych dla określonej lokalizacji przy użyciu open-meteo api
├ tests                      
   ├── tests.py      - testy 
</pre>

 ### Struktura aplikacji 
 
 Aplikacja określa lokalizacje poprzez zewnętrzne api, następnie dla tej lub podanej przez użytkownika miejscowości z pomocą kolejnego api pobiera informacje pogodowe, które zostają odpowiednio przetworzone i wyświetlone w oknie aplikacji
 
 
