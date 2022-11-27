//
// Created by witek on 27.11.2022.
//

#ifndef WEATHER_APP_IO_LOCATIONREQUEST_H
#define WEATHER_APP_IO_LOCATIONREQUEST_H

#define API_URL "https://www.googleapis.com/geolocation/v1/geolocate?key="
#define API_KEY "AIzaSyCp-MDszx8jqk2s0rWxeKbfsCa268M7KVY"
#define API_REQUEST API_URL API_KEY

class LocationRequest {
    void getLocation();
    void printLocation();
private:

};


#endif //WEATHER_APP_IO_LOCATIONREQUEST_H
