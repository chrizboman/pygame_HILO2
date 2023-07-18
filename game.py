import numpy as np
import pygame
from dataclasses import dataclass

from utils.FONTS import *
from utils.VARS import *
from utils.PData import Prompt, ImportCalories
from components.components import *
from gameSession import GameSession

from EventHandler import EventManager, userEvent, GameState

import tween

WIDTH = 1920//2
HEIGHT = 1080//2




pygame.init()

class GameManager:

    debug_animationUPPERPOS = False
    animating = False

    menuShow = False

    active = True
    gameSession = None
    eventManager = EventManager()
    
    component = Components()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    gameState = GameState.INIT

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
            pass
            # self.component.promptCard.Update(self.gameSession.standingPrompt, self.gameSession.newestPrompt)
            # self.component.scoreTable.Update(self.gameSession.score)
            # self.gameState = GameState.ANIMATING
        


    def Draw(self):
        self.dt = self.clock.tick(60)/1000
        tween.update(self.dt)

        if self.gameState == GameState.RUNNING:
            self.gameSession.standingPrompt.Draw(self.screen)
            # self.gameSession.standingPrompt.
            self.gameSession.newestPrompt.Draw(self.screen)

        self.screen.fill(COLOR.BLACK)
        self.component.scoreTable.Draw(self.screen)
        # self.component.promptCard.Draw(self.screen)
        if self.menuShow:
            self.component.pauseMeny.Draw(self.screen)
        pygame.display.update()


    
    def HandleEvents(self):
        event = self.eventManager.CheckForInput(self.gameState)

        if event == userEvent.QUIT: #never happen, it is handled in EventHandler
            quit()
        elif event == userEvent.CLICKED_HIGHER:
            pass
        elif event == userEvent.CLICKED_LOWER:
            pass
        elif event == userEvent.PAUSE:
            self.menuShow = True            
        elif event == userEvent.RESUME:
            self.menuShow = False
        elif event == userEvent.DEBUG_ANIM:
            self.component.promptCard.NextPos()
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
