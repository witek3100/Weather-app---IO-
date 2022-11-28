project(Weather_APP_IO)
cmake_minimum_required(VERSION 3.15)

find_package(Qt5 COMPONENTS
        Core
        REQUIRED)


add_executable(Weather-app-IO src/location/LocationRequest.cpp src/location/LocationRequest.h main.cpp)
target_link_libraries(WOLocation Qt5::Core)

