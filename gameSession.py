from components.utils.PData import Prompt, ImportAutolivQuestions
# from components.components import PromptCard
import random
# from GameObjects import PromptCard, PROMPCARD_POS
from components.utils.VARS import *
from components.PromptCard import PromptCard, PROMPCARD_POS
from GameObjects import TimerBar

from components.Mixer import Mixer


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
        self.prompts = ImportAutolivQuestions().GenerateBalansedQuestions(50)
        print('prompts', len(self.prompts))
        print('prompts', self.prompts[0])

        self.standingPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN_BOTTOM, self.prompts.pop(0), showAnswer=True)
        self.newestPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN_BOTTOM, self.prompts.pop(0), showButtons=True)
        # self.nextPrompt = PromptCard(PROMPCARD_POS.OFFSCREEN_BOTTOM, self.prompts.pop(0))
        self.standingPrompt.TweenTo(PROMPCARD_POS.TOP, 1)
        self.newestPrompt.TweenTo(PROMPCARD_POS.BOTTOM, 1)
        self.mixer : Mixer = mixer

        self.timerBar = TimerBar()
        self.StartTimer()
    
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
        elif int(self.newestPrompt.prompt.answer) == int(self.standingPrompt.prompt.answer):
            self.Correct()
        else :
            self.GameOver()
    
    def ClickHigher(self, higher: bool):
        self.StopTimer()
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

        self.StartTimer()
        self.newestPrompt.WaitForThen(1.5, lambda: self.__setattr__("animationComplete", True))


    def StartTimer(self):
        delay, duration = 5, 10
        if self.score < 3:
            delay = 10
            duration = 20
        elif self.score < 10:
            delay, duration = 1, 10
        elif self.score < 20:
            delay, duration = 1, 5
        elif self.score < 30:
            delay, duration = 1, 3
            
        self.timerBar.StartCountDown(delay = delay, duration=duration, onComplete=self.TimerRanOut)

    def StopTimer(self):
        if self.timerBar != None:
            self.timerBar.StopCountDown()

    def TimerRanOut(self):
        print('timer ran out')
        self.newestPrompt.Tween_AwayButtons()
        self.GameOver()

        