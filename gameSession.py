from utils.PData import Prompt, ImportCalories
from components.components import PromptCard
import random

HIDDEN = PromptCard.Pos.HIDDEN
BOTTOM = PromptCard.Pos.BOTTOM
TOP = PromptCard.Pos.TOP
HIDDEN2 = PromptCard.Pos.HIDDEN2

class GameSession:
    score = 0
    gameOver = False
    prompts : list[Prompt]
    standingPrompt : PromptCard = None
    # standingPrompt_card : PromptCard = None
    newestPrompt : PromptCard = None
    # newestPrompt_card : PromptCard = None

    def __init__(self) -> None:
        self.prompts = ImportCalories().Prompts20()
        self.standingPrompt = PromptCard(self.prompts.pop(0), pos = BOTTOM)
        self.newestPrompt = PromptCard(self.prompts.pop(0), pos = TOP)

    # def NewRound(self):
    #     self.standingPrompt = self.newestPrompt
    #     self.newestPrompt = self.prompts.pop(0)
    
    def CheckAnswer(self, answeredHigher : bool ) -> bool:
        isHigher = self.newestPrompt.answer > self.standingPrompt.answer
        if isHigher and answeredHigher:
            return True
        else :
            return False
    
    def ClickHigher(self):
        return self.CheckAnswer(True)
    
    def ClickLower(self):
        return self.CheckAnswer(False)
    


