#include <list>
#include <iostream>

#define API_URL "https://www.googleapis.com/geolocation/v1/geolocate?key="
#define API_KEY "AIzaSyCp-MDszx8jqk2s0rWxeKbfsCa268M7KVY"
#define API_REQUEST API_URL API_KEY

class LocationRequest {

public:

    LocationRequest(){}
    void getLocation();
    void printLocation();
    char* buildRequestJSON();
    int getWifiAccessPoints();

private:

    struct wifiAccessPoint {
        char macAdress[44];
        long signalQuality;
    };
    std::list<wifiAccessPoint> wifiAccessPointsList;

};