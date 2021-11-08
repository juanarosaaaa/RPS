# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseHand.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.paper_picture_big = QtWidgets.QLabel(self.centralwidget)
        self.paper_picture_big.setGeometry(QtCore.QRect(530, 10, 331, 411))
        self.paper_picture_big.setStyleSheet("\n"
"image: url(:/new/images/Paper.svg);")
        self.paper_picture_big.setText("")
        self.paper_picture_big.setPixmap(QtGui.QPixmap("python/Papel (1).svg"))
        self.paper_picture_big.setObjectName("paper_picture_big")
        self.label_play = QtWidgets.QLabel(self.centralwidget)
        self.label_play.setGeometry(QtCore.QRect(570, 470, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_play.setFont(font)
        self.label_play.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_play.setAlignment(QtCore.Qt.AlignCenter)
        self.label_play.setObjectName("label_play")
        self.label_option = QtWidgets.QLabel(self.centralwidget)
        self.label_option.setGeometry(QtCore.QRect(620, 530, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_option.setFont(font)
        self.label_option.setStyleSheet("color: rgb(28, 28, 28);")
        self.label_option.setObjectName("label_option")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(470, 610, 431, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.pictureshorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.pictureshorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pictureshorizontalLayout.setObjectName("pictureshorizontalLayout")
        self.rock_picture = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.rock_picture.setStyleSheet("image: url(:/new/images/rock_small.svg);")
        self.rock_picture.setText("")
        self.rock_picture.setObjectName("rock_picture")
        self.pictureshorizontalLayout.addWidget(self.rock_picture)
        self.paper_scissor = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.paper_scissor.setStyleSheet("\n"
"image: url(:/new/images/paper_small.svg);")
        self.paper_scissor.setText("")
        self.paper_scissor.setObjectName("paper_scissor")
        self.pictureshorizontalLayout.addWidget(self.paper_scissor)
        self.scissor_picture = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.scissor_picture.setStyleSheet("image: url(:/new/images/scissor_small.svg);")
        self.scissor_picture.setText("")
        self.scissor_picture.setObjectName("scissor_picture")
        self.pictureshorizontalLayout.addWidget(self.scissor_picture)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_play.setText(_translate("MainWindow", "LET\'S PLAY!"))
        self.label_option.setText(_translate("MainWindow", "PICK AN OPTION:"))

from images import ResourceImage


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
