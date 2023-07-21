from components.utils.PData import Prompt, ImportCalories
# from components.components import PromptCard
import random
# from GameObjects import PromptCard, PROMPCARD_POS
from components.utils.VARS import *
from components.PromptCard import PromptCard, PROMPCARD_POS



class GameSession:
    score = 0
    gameOver = False
    prompts : list[Prompt]

    standingPrompt : PromptCard
    newestPrompt : PromptCard
    nextPrompt : PromptCard

    def __init__(self) -> None:
        self.prompts = ImportCalories().Prompts20()
        self.standingPrompt = PromptCard(PROMPCARD_POS.TOP, self.prompts.pop(0), showAnswer=True)
        self.newestPrompt = PromptCard(PROMPCARD_POS.BOTTOM, self.prompts.pop(0), showButtons=True)
        self.nextPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN, self.prompts.pop(0))
    
    def Draw(self):
        self.standingPrompt.Draw()
        self.newestPrompt.Draw()
        self.nextPrompt.Draw()
    
    def CheckAnswer(self, answeredHigher : bool ) -> bool:
        isHigher = self.newestPrompt.prompt.answer > self.standingPrompt.prompt.answer
        if isHigher and answeredHigher:
            return True
        else :
            return False
    
    def ClickHigher(self):
        self.newestPrompt.TweenTo((500, 500), 1).OnTweenComplete(
            lambda : self.newestPrompt.TweenTo(PROMPCARD_POS.BOTTOM, 1).OnTweenComplete(
                lambda : print(self.CheckAnswer(True))
            )
        )
        return self.CheckAnswer(True)
    
    def ClickLower(self):
        return self.CheckAnswer(False)
    


