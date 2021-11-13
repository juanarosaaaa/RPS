from HandStrategy import Hand_Strategy as Parent
import Rock
import Scissor

class Hand_Paper(Parent):
    def play_against( handStrategy) :
        
        hand_result = {
            Rock.Hand_Rock:1,
            Scissor.Hand_Scissor:-1,
            __class__: 0}

        return hand_result.get(handStrategy)          

