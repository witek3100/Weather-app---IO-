from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 322)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 112, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(30, 100, 190);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 120, 51))
        self.label.setStyleSheet("background:rgba(191, 64, 64, 2);\n"
"color:rgb(255,255,255);\n"
"font: 75 20pt \"Ubuntu Condensed\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 101, 51))
        self.label_2.setStyleSheet("background:rgba(191, 64, 64, 2);\n"
"color:rgb(255,255,255);\n"
"font: 75 15pt \"Ubuntu Condensed\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 120, 91, 25))
        self.comboBox.setStyleSheet("background-color: rgba(15, 86, 245, 159);")
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 80, 101, 51))
        self.label_3.setStyleSheet("background:rgba(191, 64, 64, 2);\n"
"color:rgb(255,255,255);\n"
"font: 75 12pt \"Ubuntu Condensed\";")
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 120, 86, 25))
        self.comboBox_2.setStyleSheet("background-color: rgba(15, 86, 245, 159);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, 80, 101, 51))
        self.label_4.setStyleSheet("background:rgba(191, 64, 64, 2);\n"
"color:rgb(255,255,255);\n"
"font: 75 12pt \"Ubuntu Condensed\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(298, 274, 111, 41))
        self.pushButton.setStyleSheet("background-color: rgba(15, 86, 245, 159);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(180, 150, 101, 51))
        self.label_5.setStyleSheet("background:rgba(191, 64, 64, 2);\n"
"color:rgb(255,255,255);\n"
"font: 75 15pt \"Ubuntu Condensed\";")
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 190, 86, 25))
        self.comboBox_3.setStyleSheet("background-color: rgba(15, 86, 245, 159);")
        self.comboBox_3.setObjectName("comboBox_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Settings"))
        self.label_2.setText(_translate("Form", "units"))
        self.label_3.setText(_translate("Form", "temeprature"))
        self.label_4.setText(_translate("Form", "wind"))
        self.pushButton.setText(_translate("Form", "apply"))
        self.label_5.setText(_translate("Form", "theme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
