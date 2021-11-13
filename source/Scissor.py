import HandStrategy as Parent
import Paper 
import Rock
class Hand_Scissor(Parent.Hand_Strategy):
    def play_against( handStrategy) :
    
        hand_result = {
            Paper.Hand_Paper:1,
            Rock.Hand_Rock:-1,
            __class__:0
        }
        return hand_result.get(handStrategy)