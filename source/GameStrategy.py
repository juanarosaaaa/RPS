
from abc import abstractmethod


class Game_Strategy :

    @abstractmethod    
    def play_against(strategy) :
        pass

    @abstractmethod    
    def get_score():
        return 1

    @abstractmethod
    def set_ui_result():
        pass