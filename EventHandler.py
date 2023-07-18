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
    DEBUG_ANIM = 9
    START = 10


class GameState(Enum):
    INIT = 0
    START = 1
    RUNNING = 2
    GAMEOVER = 3
    ANIMATING = 4
    PAUSED = 5
    QUIT = 6

# userEvent.CLICKED_HIGHER

class EventManager:
    menuShowing = False
    currentUserEvent : userEvent = None

    def CheckUserEvents(self):
        pass


    def HandleNewEvents(self, gameState:GameState):
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

                if _gameState == GameState.RUNNING:
                    if event.key == pygame.K_h:
                        print('higher_key')
                        return userEvent.CLICKED_HIGHER
                    if event.key == pygame.K_l:
                        print('lower_key')
                        return userEvent.CLICKED_LOWER

                if event.key == pygame.K_SPACE:
                    print('space')
                    print(pygame.mouse.get_pos())
                
                if event.key == pygame.K_e:
                    print('e')
                    return userEvent.DEBUG_ANIM
                if event.key == pygame.K_p:
                    print('p')
                    if self.menuShowing:
                        self.menuShowing = False
                        return userEvent.RESUME
                    else:
                        self.menuShowing = True
                        return userEvent.PAUSE
                if event.key == pygame.K_SPACE:
                    print('space')
                    return userEvent.START
            

                
                
            # if ()