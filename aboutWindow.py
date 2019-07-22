# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutWindow(QtWidgets.QDialog):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(400, 154)
        self.label_2 = QtWidgets.QLabel(AboutWindow)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 211, 101))
        self.label_2.setObjectName("label_2")
        self.btnAye = QtWidgets.QPushButton(AboutWindow)
        self.btnAye.setGeometry(QtCore.QRect(300, 120, 80, 23))
        self.btnAye.setObjectName("btnAye")
        self.label = QtWidgets.QLabel(AboutWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("rsc/cursed_cat.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About"))
        self.label_2.setText(_translate("AboutWindow", "<html><head/><body><p>Created by Ivan Ongko in Python</p><p>in our beloved UNIKOM &lt;3</p><p><a href=\"https://github.com/cathean\"><span style=\" text-decoration: underline; color:#0000ff;\">github</span></a></p></body></html>"))
        self.btnAye.setText(_translate("AboutWindow", "AYE AYE"))

        self.btnAye.clicked.connect(self.on_btn_aye_clicked)

    def on_btn_aye_clicked(self):
        self.close()
        print('THIS IS BUG AAAAA I CAN\'T CLOSE IT')
