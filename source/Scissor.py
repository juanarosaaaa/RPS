import GameStrategy as Parent
import Paper 
import Rock
import PaperWinDialog
import PaperLoseDialog
import PaperDrawDialog
import Scissor
from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
class Hand_Scissor(Parent.Game_Strategy):
    
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
        hand_dialog = {
            Rock.Hand_Rock: PaperWinDialog.Ui_DialogPaperWin(),
            Scissor.Hand_Scissor:PaperLoseDialog.Ui_DialogPaperLose(),
            __class__: PaperDrawDialog.Ui_DialogPaperDraw()}