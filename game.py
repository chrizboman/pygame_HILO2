import numpy as np
import pygame
from pygame import QUIT
from dataclasses import dataclass
from pygame import Vector2

from components.utils.FONTS import *
from components.utils.VARS import *
from components.utils.PData import Prompt, ImportCalories
# from components.components import Button, Card, Collection, PauseMenu, GameObject, Text
from gameSession import GameSession
from GameObjects import GameObject, Button, Card, Collection, PauseMenu, Text, ScoreCard

from EventHandler import EventManager, userEvent, GameState

# import tween

WIDTH = 1920//2
HEIGHT = 1080//2

VCENTER = HEIGHT//2
HCENTER = WIDTH//2

OO = Vector2(0,0)

CENTER = (WIDTH//2, HEIGHT//2)

RCOL_WIDTH = 200
RCOL_CENTER = (WIDTH - RCOL_WIDTH//2, VCENTER)

LCOL_WIDTH = WIDTH - RCOL_WIDTH
LCOL_HCENTER = LCOL_WIDTH//2
LCOL_CENTER = (LCOL_HCENTER, VCENTER)
LCOL_TCENTER = (LCOL_HCENTER, HEIGHT//4)
LCOL_BCENTER = (LCOL_HCENTER, HEIGHT - HEIGHT//4)


# class Components():
#     ScoreCard = ScoreCard( (0,0), (200, HEIGHT)).MoveTo(RCOL_CENTER)




pygame.init()

class GameManager:

    debug_animationUPPERPOS = False
    animating = False

    menuShow = False

    active = True
    gameSession = None
    eventManager = EventManager()



    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    GameObject.debug = True
    GameObject.screen = screen


    gameState = GameState.INIT

    scoreCard : ScoreCard = ScoreCard(RCOL_CENTER, (RCOL_WIDTH, HEIGHT))

    pauseMenu : PauseMenu = PauseMenu().Enable(False)

    listPrompts = ImportCalories().Prompts20()

    prompt1 = listPrompts.pop(0)
    prompt2 = listPrompts.pop(0)

    # promptCard1 : PromptCard = PromptCard(LCOL_TCENTER, (LCOL_WIDTH, HEIGHT//2), prompt1)
    # promptCard2 : PromptCard = PromptCard(OO, (LCOL_WIDTH, HEIGHT//2), prompt2, True).MoveTo(LCOL_BCENTER)


    


    def Update(self):
 
        if self.gameState == GameState.INIT:
            print('creating new game session')
            self.gameSession = GameSession()
            self.gameState = GameState.RUNNING

        if self.gameState == GameState.START:
            print('Start new game')
            self.gameSession = GameSession()
            self.gameState = GameState.RUNNING
        
        if self.gameState == GameState.RUNNING:
            for gameObject in GameObject.instances:
                gameObject.OnUpdate(self.dt)
            

    text = Text(CENTER, color=COLOR.WHITE)
    def Draw(self):
        self.dt = self.clock.tick(60)/1000

        self.screen.fill(COLOR.BLACK)

        if self.gameState == GameState.RUNNING:
            self.scoreCard.Draw()
            # self.promptCard1.Draw()
            # self.promptCard2.Draw()
            self.gameSession.Draw()

            

        if self.gameState == GameState.PAUSED:
            self.pauseMenu.Draw()


        if self.menuShow:
            pass
            # self.component.pauseMeny.Draw(self.screen)
        
        self.btn = Button(CENTER+Vector2(300,0), (300, 200)).Draw()
        self.btn = Button(CENTER, (300, 200)).Scale(.5).Draw()
        pygame.display.update()


    
    def HandleEvents(self):
        event = self.eventManager.CheckForInput(self.gameState)

        if event == userEvent.QUIT: #never happen, it is handled in EventHandler
            pygame.QUIT
            quit()
        elif event == userEvent.CLICKED_HIGHER:
            self.gameSession.ClickHigher()
            
        elif event == userEvent.CLICKED_LOWER:
            pass
        elif event == userEvent.PAUSE:
            self.pauseMenu.Enable(True)
            self.gameState = GameState.PAUSED

        elif event == userEvent.RESUME:
            self.pauseMenu.Enable(False)     
            self.gameState = GameState.RUNNING      

        elif event == userEvent.DEBUG_ANIM:
            self.gameSession.newestPrompt.Tween_AwayButtons()

        elif event == userEvent.START:
            self.gameState = GameState.START



    def NotAnimating(self):
        self.animating = False



def Print(msg):
    print(msg)












game = GameManager()
# game.InitAnimations()

while game.active:
    game.Update()
    game.Draw()
    game.HandleEvents()
