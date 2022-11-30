

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
    border.width: 2
    gradient: Gradient {
        GradientStop {
            position: 0
            color: "#c7b571"
        }

        GradientStop {
            position: 1
            color: "#5d5c57"
        }
        orientation: Gradient.Vertical
    }

    Rectangle {
        id: rectangle1
        x: 105
        y: 230
        width: 1414
        height: 562
        radius: 8
        border.color: "#ece8c9"
        border.width: 0
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#65ca68"
            }

            GradientStop {
                position: 1
                color: "#d8e3d9"
            }
            orientation: Gradient.Vertical
        }

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

        Button {
            id: compareModeButton
            x: 1237
            y: 515
            width: 171
            height: 40
            text: qsTr("Compare Mode...")
            font.pointSize: 15
        }

        Button {
            id: settingsButton
            x: -97
            y: 623
            width: 214
            height: 39
            text: qsTr("Settings")
            font.pointSize: 17
            smooth: true
            highlighted: false
            flat: false
            icon.source: "images/126472.png"
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

        ComboBox {
            id: cityList
            x: 0
            y: -173
            width: 1110
            height: 65
        }

        Button {
            id: takeLocalisationButton
            x: 1140
            y: -173
            width: 274
            height: 65
            text: qsTr("Take localisation automatically")
            font.pointSize: 14
        }
    }
    states: [
        State {
            name: "clicked"
            when: takeLocalisationButton.checked
        }
    ]
}
