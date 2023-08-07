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

    standingPrompt : PromptCard = None
    newestPrompt : PromptCard = None
    nextPrompt : PromptCard = None

    animationComplete = True

    def __init__(self) -> None:
        self.prompts = ImportCalories().Prompts20()
        self.standingPrompt = PromptCard(PROMPCARD_POS.TOP, self.prompts.pop(0), showAnswer=True)
        self.newestPrompt = PromptCard(PROMPCARD_POS.BOTTOM, self.prompts.pop(0), showButtons=True)
        self.nextPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN, self.prompts.pop(0))
    
    def Draw(self):
        self.standingPrompt.Draw()
        self.newestPrompt.Draw()
        self.nextPrompt.Draw()
    
    def CheckAnswer(self, answeredHigher : bool ):
        isHigher = int(self.newestPrompt.prompt.answer) > int(self.standingPrompt.prompt.answer)
        if isHigher and answeredHigher:
            self.Correct()
        else :
            self.GameOver()
    
    def ClickHigher(self, higher: bool):
        # self.newestPrompt.Tween_AwayButtons()
        # self.newestPrompt.Tween_ShowAnswer(delay=.5)
        # self.newestPrompt.Tween_NumberTo( delay=.9)
        self.animationComplete = False
        self.newestPrompt.CheckAnswerAnimation(
            onCompleteFunc= lambda: self.CheckAnswer(higher)
        )

        # return self.CheckAnswer(True)

    def Correct(self):
        print('correct')
        self.score += 1
        self.NewPrompt()

    def GameOver(self):
        print('game over')
        self.gameOver = True

    def NewPrompt(self):
        self.newestPrompt.TweenUP()

