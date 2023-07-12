from components.PData import Prompt, ImportCalories
import random

class GameSession:
    score = 0
    gameOver = False
    prompts : list[Prompt]
    standingPrompt : Prompt = None
    newestPrompt : Prompt = None

    def __init__(self):
        self.prompts = ImportCalories().Prompts20()
        self.standingPrompt = self.prompts.pop(0)
        self.newestPrompt = self.prompts.pop(0)
    
    def NewRound(self):
        self.standingPrompt = self.newestPrompt
        self.newestPrompt = self.prompts.pop(0)
    
    def CheckAnswer(self, answeredHigher : bool ) -> bool:
        isHigher = self.newestPrompt.answer > self.standingPrompt.answer
        if isHigher and answeredHigher:
            return True
        else :
            return False
        
    
gameSession = GameSession()
