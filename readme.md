
## Projekt Inżynieria Oprogramowania ISI2 - aplikacja z informacjami pogodowymi

* Witold Nowogórski
* Adam Pliszka
* Kaja Dzielnicka
* Bartłomiej Stępniewski

# Uruchamianie #
```
git clone https://github.com/witek3100/Weather-app-IO
```  
- Windows
plik WeatherApp otwiera aplikacje 
lub 

```
python ../src/gui.py

```

- Linux 
```
python ..src/gui.py

```

### Struktura aplikacji 
 
 Aplikacja określa lokalizacje poprzez zewnętrzne api, następnie dla tej lub podanej przez użytkownika miejscowości z pomocą kolejnego api pobiera informacje pogodowe, które zostają odpowiednio przetworzone i wyświetlone w oknie aplikacji
 
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

 
 
 
