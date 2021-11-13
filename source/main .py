from AbstractHandStrategy import Abstract_Strategy
import Rock
import Scissor


x = Abstract_Strategy(Scissor.Hand_Scissor)
print(x.play_against(Rock.Hand_Rock))