cmake_minimum_required(VERSION 3.23)
project(Weather_app)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(Weather_app main.cpp)
target_link_libraries(Weather_app
        Qt::Core
        Qt::Gui
        Qt::Widgets
        )

