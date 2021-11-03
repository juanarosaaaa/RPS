from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Rock Paper Scissors")
        self.initUI()


    def initUI(self):
       self.label = QtWidgets.QLabel(self)
       self.label.setText("Text Label")
       self.label.move(50, 50)


       self.button = QtWidgets.QPushButton(self)
       self.button.setText("Push Button")
       self.button.clicked.connect(self.onClick)


    def onClick(self):
        self.label.setText("Changed!")


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    sys.exit(app.exec())

    
window()
