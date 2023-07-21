from . utils.VARS import *
from GameObjects import *

RCOL_HCENTER = (WIDTH - 200)//2
from enum import Enum

class PROMPCARD_POS():
    TOP = (RCOL_HCENTER, HEIGHT//4)
    BOTTOM = (RCOL_HCENTER, HEIGHT//4*3)
    OFFSCREEN = (RCOL_HCENTER, HEIGHT + 200)



class PromptCard(Collection):
    SIZE = (WIDTH-200, HEIGHT//2)

    BTN_SIZE = (100, 50)
    BTN_POS = (0, 40)
    BTN_DIST = Vector2(-70, 0)

    PROMPT_POS = (0, -80)
    ANSWER_POS = (0, 40)

    showButtons : bool = False
    showAnswer : bool = False

    def __init__(self, positionCenter: Vector2, prompt : Prompt = None, showButtons : bool = False, showAnswer : bool = False):
        super().__init__(positionCenter, [])

        self.prompt = prompt
        self.showButtons = showButtons
        self.showAnswer = showAnswer
        self.card = self.Add(Card((0,0), self.SIZE))
        self.txt_prompt = self.Add(Text(self.PROMPT_POS, self.prompt.prompt, font = large_font))
        self.txt_is = self.Add(Text((0,-40), 'are', font = medium_font))
        self.txt_source = self.Add(Text((-250,100), self.prompt.source, font = small_font))
        self.txt_qm = self.Add(Text(self.BTN_POS, '?', font = medium_font))
        
        self.btn_higher = self.Add(Button(
                                        self.BTN_POS - self.BTN_DIST, 
                                        self.BTN_SIZE, "Higher", 
                                        font = small_font)
                                        )
        self.btn_lower = self.Add(Button(
                                        self.BTN_POS + self.BTN_DIST,
                                         self.BTN_SIZE, 
                                         "Lower", 
                                         font = small_font )
                                         )

        self.txt_answer = self.Add(Text(self.ANSWER_POS, 
                                        f'{self.prompt.answer}', 
                                        font = huge_font))
        # if self.showButtons:
        if self.showButtons:
            self.txt_answer.Enable(False)
            self.txt_qm.Enable(True)
            self.btn_higher.Enable(True)
            self.btn_lower.Enable(True)

        if self.showAnswer:
            self.txt_answer.Enable(True)
            self.txt_qm.Enable(False)
            self.btn_higher.Enable(False)
            self.btn_lower.Enable(False)
        
        if not showButtons and not self.showAnswer:
            self.txt_answer.Enable(False)
            self.txt_qm.Enable(False)
            self.btn_higher.Enable(False)
            self.btn_lower.Enable(False)

    def Tween_AwayButtons(self):
        self.btn_higher.TweenTo(scale = 0, duration=1)
        self.btn_lower.TweenTo(scale = 0, duration=1)
        # self.txt_qm.TweenTo(self.BTN_POS, 1)


