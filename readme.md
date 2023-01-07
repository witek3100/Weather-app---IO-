
## Projekt Inżynieria Oprogramowania ISI2 - aplikacja z informacjami pogodowymi

* Witold Nowogórski
* Adam Pliszka
* Kaja Dzielnicka
* Bartłomiej Stępniewski
  
=======================================================================================
<pre>
├ src                           #folder źródłowy  
   ├── gui     - interfejs użytkownika
   ├── location_request.py     - pobieranie lokalilizacji przy użyciu google geolocation api         
   ├── weather_data_request.py       - pobierania informacji pogodowych dla określonej lokalizacji przy użyciu open-meteo api
├ tests                      
   ├── tests.py      - testy 
</pre>

 ### Struktura aplikacji 
 
 Aplikacja określa lokalizacje poprzez zewnętrzne api, następnie dla tej lub podanej przez użytkownika miejscowości z pomocą kolejnego api pobiera informacje pogodowe, które zostają odpowiednio przetworzone i wyświetlone w oknie aplikacji
 
 
