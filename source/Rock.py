import GameStrategy as Parent
import Paper 
import Rock
import RockWinDialog
import RockLoseDialog
import RockDrawDialog
import Scissor
from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage

class Hand_Rock(Parent):

    def play_against(self,handStrategy) :
        self.strategy = handStrategy


    def get_score(self):
        self.hand_result = {
            Scissor.Hand_Scissor:1,
            Paper.Hand_Paper:-1,
            __class__:0}
        return self.hand_result.get(self.strategy)    

    def set_ui_result(self):
        self.window = QtWidgets.QMainWindow()
        self.hand_window = {
            Scissor.Hand_Scissor:RockWinDialog.Ui_DialogRockWin,
            Paper.Hand_Paper: RockLoseDialog.Ui_DialogRockLose,
            __class__:RockDrawDialog.Ui_Dialog}
        self.ui = self.hand_window.get(self.strategy)
        self.ui.setupUi(self.window)