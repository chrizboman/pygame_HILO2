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

    oldPrompt : PromptCard = None
    standingPrompt : PromptCard = None
    newestPrompt : PromptCard = None
    # nextPrompt : PromptCard = None

    animationComplete = True

    def __init__(self, mixer) -> None:
        self.prompts = ImportCalories().Prompts20()
        self.standingPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN_BOTTOM, self.prompts.pop(0), showAnswer=True)
        self.newestPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN_BOTTOM, self.prompts.pop(0), showButtons=True)
        # self.nextPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN_BOTTOM, self.prompts.pop(0))
        self.standingPrompt.TweenTo(PROMPCARD_POS.TOP, 1)
        self.newestPrompt.TweenTo(PROMPCARD_POS.BOTTOM, 1)
        self.mixer = mixer
    
    def Draw(self):
        self.standingPrompt.Draw()
        self.newestPrompt.Draw()
        # self.nextPrompt.Draw()
        if self.oldPrompt != None:
            self.oldPrompt.Draw()
    
    def CheckAnswer(self, answeredHigher : bool ):
        isHigher = int(self.newestPrompt.prompt.answer) > int(self.standingPrompt.prompt.answer)
        
        if isHigher and answeredHigher:
            self.Correct()
        elif not isHigher and not answeredHigher:
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
        print('---correct---')
        self.score += 1
        self.NewPrompt()
        self.mixer.PlaySound('correct')

    def GameOver(self):
        self.mixer.PlaySound('wrong')
        print('✝✝✝ game over ✝✝✝')
        # self.newestPrompt.TweenScale(0,1) # scale is not impemented for a collection
        # self.standingPrompt.TweenScale(0,1)
        self.standingPrompt.TweenTo(PROMPCARD_POS.OFFSCREEN_TOP, .5, delay=1)
        self.newestPrompt.TweenTo(PROMPCARD_POS.OFFSCREEN_BOTTOM, .5, delay=1)
        self.standingPrompt.WaitForThen(1.5, lambda: self.__setattr__("gameOver", True))
        


    def NewPrompt(self):

        self.oldPrompt = self.standingPrompt
        self.standingPrompt = self.newestPrompt
        self.newestPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN_BOTTOM, self.prompts.pop(0), showButtons=True)
        self.newestPrompt.showButtons = True
        
        self.oldPrompt.TweenTo(PROMPCARD_POS.OFFSCREEN_TOP, 1)
        self.standingPrompt.TweenTo(PROMPCARD_POS.TOP, 1)
        self.newestPrompt.TweenTo(PROMPCARD_POS.BOTTOM, 1)

        self.newestPrompt.WaitForThen(1.5, lambda: self.__setattr__("animationComplete", True))

