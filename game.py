import numpy as np
import pygame
from dataclasses import dataclass

from components.FONTS import *
from components.VARS import *
from components.PData import Prompt, ImportCalories

from EventHandler import EventManager, userEvent, gameState

import tween

COLOR.AL_BLUE

WIDTH = 1920//2
HEIGHT = 1080//2




pygame.init()

class GameManager:
    active = True
    gameSession = None
    eventManager = EventManager()
    
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    gameState = gameState.INIT

    def Update(self):
        self.dt = self.clock.tick(60)/1000
        tween.update(self.dt)

        if self.gameState == gameState.START:
            print('Start new game')
            self.gameState = gameState.RUNNING

    def Draw(self):
        self.screen.fill(COLOR.BLACK)
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
            pass
        elif event == userEvent.RESUME:
            pass




        

                



game = GameManager()

while game.active:
    game.Update()
    game.Draw()
    game.HandleEvents()
