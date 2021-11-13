from HandStrategy import Hand_Strategy as Parent
import Paper
import Scissor


class Hand_Rock(Parent):
    def play_against(handStrategy):
       
        hand_result = {
            Scissor.Hand_Scissor:1,
            Paper.Hand_Paper:-1,
            __class__:0}

        return hand_result.get(handStrategy)    