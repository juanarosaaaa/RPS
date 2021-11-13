
import Rock
import Scissor
import Paper
from random import randint
from HandStrategy import Hand_Strategy

class Enemy_Hand():
    def create_enemy() -> Hand_Strategy:
        n = randint(0,2)
        hand_result ={
            0:Rock.Hand_Rock,
            1:Scissor.Hand_Scissor,
            2:Paper.Hand_Paper
        }
    
        return hand_result.get(n)