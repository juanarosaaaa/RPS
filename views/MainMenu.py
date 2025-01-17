# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
from screeninfo import get_monitors
from ChooseHand import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1000, 768)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background:rgb(81, 81, 81)")
        for m in get_monitors():
          screenHeight = m.height
          screenWidth = m.width
        MainWindow.setGeometry((screenWidth/2)-(1000/2),(screenHeight/2)-(768/2),1000,768)
        self.window = MainWindow
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 680, 291, 61))
        self.startButton = self.pushButton
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);")
        self.startButton.setObjectName("startButton")
        self.pushButton.clicked.connect(self.openChooseHand)
     
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 330, 201, 321))
        self.label.setStyleSheet("image: url(:/new/images/Scissor.svg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Tesoura (1).svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 431, 171))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Thin")
        font.setPointSize(35)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "ROCK\n"
"/PAPER/\n"
"SCISSOR"))

    def openChooseHand(self):
        self.windows2 = QtWidgets.QMainWindow()
        self.ui = ChooseHandWindow()
        self.ui.setupUi (self.windows2)
        self.windows2.show()  
        self.window.close()

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
