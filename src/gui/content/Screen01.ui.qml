

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2
import Weatherapp

Rectangle {
    id: main
    width: 1600
    height: 900
    color: "#fce58f"

    TextField {
        id: localisationSearchField
        x: 105
        y: 57
        width: 1128
        height: 65
        text: "Enter your city..."
        font.pointSize: 23
        placeholderText: qsTr("Text Field")
    }

    Button {
        id: button
        x: 1245
        y: 57
        width: 274
        height: 65
        text: qsTr("Take localisation automatically")
        font.pointSize: 14
    }

    Rectangle {
        id: rectangle1
        x: 105
        y: 230
        width: 1414
        height: 562
        color: "#fbf6d1"
        radius: 8
        border.color: "#fbf6d1"
        border.width: 8

        Image {
            id: currentWeatherIco
            x: 0
            y: 0
            width: 393
            height: 393
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        ComboBox {
            id: comboBox
            x: 657
            y: 11
            displayText: "1h"
            currentIndex: 1
            textRole: ""
        }

        Text {
            id: localisationtext
            x: 949
            y: 0
            width: 465
            height: 77
            text: qsTr("Weather for:")
            font.pixelSize: 39
            font.bold: false
        }

        Text {
            id: timeIntervalLabel
            x: 404
            y: 2
            width: 247
            height: 62
            text: qsTr("Time interval:")
            font.pixelSize: 39
            font.bold: false
        }

        Text {
            id: weatherDescription
            x: 441
            y: 129
            width: 533
            height: 76
            text: qsTr("[WEATHER DESCRIPTION]")
            font.pixelSize: 46
        }

        Text {
            id: temperature
            x: 448
            y: 265
            width: 533
            height: 76
            text: qsTr("[TEMPERATURE]")
            font.pixelSize: 46
        }
    }

    Button {
        id: button1
        x: 1348
        y: 752
        width: 171
        height: 40
        text: qsTr("Compare Mode...")
    }

    Button {
        id: button2
        x: 0
        y: 860
        text: qsTr("Settings")
        icon.source: "images/126472.png"
    }
    states: [
        State {
            name: "clicked"
            when: button.checked
        }
    ]
}
