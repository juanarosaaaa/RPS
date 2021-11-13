# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaperDrawDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
from screeninfo import get_monitors


class Ui_DialogPaperDraw(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 626)
        Dialog.setFixedSize(1000,626)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(400, 240, 181, 41))
        for m in get_monitors():
          screenHeight = m.height
          screenWidth = m.width
        Dialog.setGeometry((screenWidth/2)-(1000/2),(screenHeight/2)-(768/2),1000,768)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(360, 290, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(390, 370, 201, 261))
        self.label_16.setStyleSheet("image: url(:/new/images/Hand_Big.png);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(400, -20, 201, 271))
        self.label_18.setStyleSheet("image: url(:/new/images/Hand_Big_Upside.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 0, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_17.setText(_translate("Dialog", "IT\'S A DRAW!"))
        self.pushButton_11.setText(_translate("Dialog", "PLAY AGAIN"))
        self.pushButton_12.setText(_translate("Dialog", "X"))



