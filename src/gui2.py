# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 648)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 112, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(30, 100, 190);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(390, 60, 191, 81))
        self.city_label.setStyleSheet("font: 700 30pt \"Calibri\";\n"
"background-color: rgba(191, 64, 64, 2);\n"
"color: rgb(243, 243, 243);")
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 1001, 51))
        self.label_2.setStyleSheet("background-color:rgb(30, 100, 190)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.pushButton.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 10, 121, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.pushButton_3.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(650, 10, 291, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(130,200,250)")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 10, 31, 31))
        self.pushButton_4.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionChange_units = QtWidgets.QAction(MainWindow)
        self.actionChange_units.setObjectName("actionChange_units")
        self.actiontime_zone = QtWidgets.QAction(MainWindow)
        self.actiontime_zone.setObjectName("actiontime_zone")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.city_label.setText(_translate("MainWindow", "Kraków"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.pushButton_2.setText(_translate("MainWindow", "Reload location"))
        self.pushButton_3.setText(_translate("MainWindow", "Update Weather"))
        self.lineEdit.setText(_translate("MainWindow", "search city ..."))
        self.actionChange_units.setText(_translate("MainWindow", "Units"))
        self.actiontime_zone.setText(_translate("MainWindow", "Time zone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())