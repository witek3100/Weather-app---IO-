import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 400
    height: 600
    gradient: Gradient {
        GradientStop {
            position: 1
            color: "#304e90"
        }

        GradientStop {
            position: 0.04795
            color: "#c7b571"
        }

        GradientStop {
            position: 0.98174
            color: "#1d2d3e"
        }

        orientation: Gradient.Vertical
    }

    Switch {
        id: switch1
        x: 11
        y: 164
        width: 378
        height: 40
        text: qsTr("Time format [12h/24h]")
        font.pointSize: 20
        font.italic: true
        font.bold: true
        icon.color: "#b18282"
    }

    Rectangle {
        id: rectangle
        x: 0
        y: 0
        width: 400
        height: 150
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#89e067"
            }

            GradientStop {
                position: 1
                color: "#000000"
            }
            orientation: Gradient.Vertical
        }

        Text {
            id: text1
            x: 0
            y: 35
            width: 400
            height: 59
            text: qsTr("Settings")
            font.pixelSize: 67
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.underline: false
            font.italic: true
            font.bold: true
        }
    }

    Switch {
        id: switch2
        x: 11
        y: 217
        width: 378
        height: 40
        text: qsTr("Language[Eng/Pl]")
        font.bold: true
        font.pointSize: 20
        icon.color: "#b18282"
        font.italic: true
    }

    Switch {
        id: switch3
        x: 11
        y: 266
        width: 378
        height: 40
        text: qsTr("Dark mode")
        font.pointSize: 20
        font.bold: true
        icon.color: "#b18282"
        font.italic: true
    }
}
