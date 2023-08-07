from . utils.VARS import *
from GameObjects import *
import tween
import math
from typing import Callable
from . Animation import Animation

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
        self.tposition = positionCenter

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

        self.txt_answer : Text = self.Add(Text(self.ANSWER_POS, 
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
        
    def CheckAnswerAnimation(self, onCompleteFunc: Callable):
        self.__Tween_AwayButtons()
        self.__Tween_ShowAnswer(delay=.5)
        self.__Tween_NumberTo(delay=.9).on_complete(
            onCompleteFunc
        )
        
    def __Tween_AwayButtons(self):
        # tween.to(self.btn_higher, 'position', self.btn_higher.position + Vector2(0, -100), 0.5, tween.easeOutQuad)
        self.tween_higher = tween.to(self.btn_higher, "scale", 0, .5, 'easeInOutQuad')
        self.tween_lower = tween.to(self.btn_lower, "scale", 0, .5, 'easeInOutQuad')
        self.tween_qm = tween.to(self.txt_qm, "scale", 0, .5, 'easeInOutQuad')
        self.tween_qm.on_update(lambda: self.Scale(self.scale))

    def __Tween_ShowAnswer(self, delay : float = 0.0):
        self.txt_answer.Enable(True)
        self.txt_answer.Scale(0)
        self.tween_answer = tween.to(self.txt_answer, "scale", 1, .5, 'easeInOutQuad', delay=delay)
        self.tween_answer.on_update(lambda: self.Scale(self.scale))
        return self.tween_answer
    
    def __Tween_NumberTo(self, value = None, duration = 1.0, delay : float = 0.0):
        if not value:
            value = int( self.prompt.answer)
        self.txt_answer.Enable(True)
        self.txt_answer.text = 0
        self.tween_answer = tween.to(self.txt_answer, "text", value, duration, ease_type='easeOutQuint', delay=delay)
        return self.tween_answer
    
    def TweenUP(self):
        print('tweenuo')
        self.uptween = tween.to(self, 'tposition', self.position - Vector2(0, WIDTH/4 + 30), 2, ease_type='easeInOutCubic')
        self.uptween.on_update(lambda: self.MoveTo(self.tposition))
        # self.uptween.on_update(lambda: print(self.position))
        # self.position += Vector2(0, -WIDTH/4)
        pass
        
