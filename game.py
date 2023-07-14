import numpy as np
import pygame
from dataclasses import dataclass


from utils import VARS
from utils.PData import Prompt, ImportCalories
from components.components import GameOverBox, RectBox, Text, Button, Components
from gameSession import GameSession
from EventHandler import EventManager, userEvent, gameState

import tween

WIDTH = 1920//2
HEIGHT = 1080//2



pygame.init()

class GameManager:
    components = Components()

    active = True
    gameSession = None
    eventManager = EventManager()
    # 
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
        self.screen.fill(VARS.BLACK)
        self.components.GameOverBox.Draw(self.screen)  
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
