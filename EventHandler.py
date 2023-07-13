import pygame
# from game import GameManager as gm
from enum import Enum
from dataclasses import dataclass
# from game import gameState


# userEvent = Enum('UserEvents', ['QUIT', 'PAUSE', 'RESUME', 'CLICKED_HIGHER', 'CLICKED_LOWER'])

class userEvent(Enum):
    QUIT = 0
    PAUSE = 1
    RESUME = 2
    CLICKED_HIGHER = 3
    CLICKED_LOWER = 4


class gameState(Enum):
    INIT = 0
    START = 1
    RUNNING = 2
    GAMEOVER = 3
    ANIMATING = 4
    PAUSED = 5
    QUIT = 6

userEvent.CLICKED_HIGHER

class EventManager:

    currentUserEvent : userEvent = None

    def CheckUserEvents(self):
        pass


    def HandleNewEvents(self, gameState:gameState):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.userEvent = userEvent.QUIT
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print('a')
                if event.key == pygame.K_h:
                    print('higher_key')
                    self.currentUserEvent = userEvent.CLICKED_HIGHER
                if event.key == pygame.K_l:
                    print('lower_key')
                    self.currentUserEvent = userEvent.CLICKED_LOWER
                if event.key == pygame.K_SPACE:
                    print('space')
                
                if event.key == pygame.K_ESCAPE:
                    # self.userEvents.append(userEvent.QUIT)
                    self.userEvent = userEvent.QUIT
                    quit()


    def CheckForInput(self, _gameState) -> userEvent:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                quit()
                return userEvent.QUIT

            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_ESCAPE:
                    # self.userEvents.append(userEvent.QUIT)
                    self.userEvent = userEvent.QUIT
                    quit()

                if _gameState == gameState.RUNNING:
                    if event.key == pygame.K_h:
                        print('higher_key')
                        return userEvent.CLICKED_HIGHER
                    if event.key == pygame.K_l:
                        print('lower_key')
                        return userEvent.CLICKED_LOWER

                if event.key == pygame.K_SPACE:
                    print('space')
            

                
                
            # if ()