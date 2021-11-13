from GameStrategy import Game_Strategy as Parent
import Paper 
import Rock
import ScissorsDrawDialog
import ScissorsLoseDialog
import ScissorsWinDialog
import Scissor
from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
class Hand_Scissor(Parent):
    

    def play_against(self,handStrategy) :
        self.strategy = handStrategy


    def get_score(self):
        self.hand_result = {
            Paper.Hand_Paper:1,
            Rock.Hand_Rock:-1,
            __class__:0
        }
        return self.hand_result.get(self.strategy)
    


    def set_ui_result(self):

        self.window = QtWidgets.QMainWindow()
        self.hand_window = {
            Paper.Hand_Paper: ScissorsWinDialog.Ui_DialogScissorsWin(),
            Rock.Hand_Rock:ScissorsLoseDialog.Ui_DialogScissorLose(),
            __class__: ScissorsDrawDialog.Ui_DialogScissorsDraw()
            }

        self.ui = self.hand_window.get(self.strategy)    
        self.ui.setupUi(self.window)
        self.window.show()