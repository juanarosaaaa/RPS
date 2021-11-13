from GameStrategy import Game_Strategy as Parent
import Rock
import Scissor
from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
import PaperWinDialog 
import PaperLoseDialog
import PaperDrawDialog
import MainMenu as mm


class Hand_Paper(Parent):


    def play_against(self,handStrategy) :
        self.strategy = handStrategy
        

        MainWindow = QtWidgets.QMainWindow()
        ui = mm.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        
        

    def get_score(self):
        self.hand_result = {
            Rock.Hand_Rock:1,
            Scissor.Hand_Scissor:-1,
            __class__: 0}
        return self.hand_result.get(self.strategy)          


    def set_ui_result(self):
        self.window = QtWidgets.QMainWindow()
        self.hand_window = {
            Rock.Hand_Rock: PaperWinDialog.Ui_DialogPaperWin(),
            Scissor.Hand_Scissor:PaperLoseDialog.Ui_DialogPaperLose(),
            __class__: PaperDrawDialog.Ui_DialogPaperDraw()}

        self.ui = self.hand_window.get(self.strategy)
        self.ui.setupUi(self.window)    
