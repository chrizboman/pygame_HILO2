import numpy as np
import pygame
from dataclasses import dataclass

from components.FONTS import *
from components.VARS import *
from components.PData import Prompt, ImportCalories

import tween

COLOR.AL_BLUE

WIDTH = 1920//2
HEIGHT = 1080//2



@dataclass
class gameState:
    INIT = 0
    START = 1
    RUNNING = 2
    GAMEOVER = 3
    ANIMATING = 4
    PAUSED = 5
    QUIT = 6

pygame.init()

class Game:
    active = True
    
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
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.active = False
                self.gameState = gameState.QUIT
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print('a')
                if event.key == pygame.K_d:
                    print('d')
                if event.key == pygame.K_SPACE:
                    print('space')
                if event.key == pygame.K_ESCAPE:
                    self.active = False
                    self.gameState = gameState.QUIT
                    quit()
                



game = Game()

while game.active:
    game.Update()
    game.Draw()
    game.HandleEvents()
