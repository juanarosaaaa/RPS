
import HandStrategy 

class Abstract_Strategy :
    def __init__(self, strategy:HandStrategy.Hand_Strategy) :
        self.strategy = strategy


    def play_against(self, strategy:HandStrategy.Hand_Strategy) :
        return  self.strategy.play_against(strategy)