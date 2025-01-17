# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScissorsLoseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
from screeninfo import get_monitors



class Ui_DialogScissorLose(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 626)
        Dialog.setFixedSize(1000,626)
        for m in get_monitors():
          screenHeight = m.height
          screenWidth = m.width
        Dialog.setGeometry((screenWidth/2)-(1000/2),(screenHeight/2)-(768/2),1000,768)
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(360, 300, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(0, 10, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(400, 250, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(390, 380, 201, 261))
        self.label_23.setStyleSheet("image: url(:/new/images/Scissor_Big.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(400, -10, 201, 261))
        self.label_24.setStyleSheet("image: url(:/new/images/Rock_Big_Upside.png);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_15.setText(_translate("Dialog", "PLAY AGAIN"))
        self.pushButton_16.setText(_translate("Dialog", "X"))
        self.label_22.setText(_translate("Dialog", "YOU LOSE!"))



