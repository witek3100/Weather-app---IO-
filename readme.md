
## Projekt Inżynieria Oprogramowania ISI2 - aplikacja z informacjami pogodowymi

* Witold Nowogórski
* Adam Pliszka
* Kaja Dzielnicka
* Bartłomiej Stępniewski

# Uruchamianie #
```
git clone https://github.com/witek3100/Weather-app-IO
```  
```  
pip inistall pyqt5
```  
w folderze repozytorium:
```  
python ../src/gui.py
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

 
 
 
