import pygame
# from game import GameManager as gm
from enum import Enum
from dataclasses import dataclass
# from game import gameState


# userEvent = Enum('UserEvents', ['QUIT', 'PAUSE', 'RESUME', 'CLICKED_HIGHER', 'CLICKED_LOWER'])
#
# 
#  keys allowed in the main menu name selection
ALLOWED_NAME_KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v', 'w', 'x', 'y', 'z', 'BACKSPACE', 'SPACE', 'PERIOD']
allowedPyKeys = [getattr(pygame, 'K_' + key) for key in ALLOWED_NAME_KEYS]

swedishKeys = {
    'å' : 229,
    'ä' : 228,
    'ö' : 246, }

# allowedPyKeys.extend(swedishKeys.values())


class userEvent(Enum):
    QUIT = 0
    PAUSE = 1
    RESUME = 2
    CLICKED_HIGHER = 3
    CLICKED_LOWER = 4
    DEBUG_ANIM = 9
    START = 10
    TYPING = 11
    W = 11
    A = 12


class GameState(Enum):
    INIT = -1
    MAINMENU = 0
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


    def CheckForInput(self, _gameState) -> userEvent:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                quit()
                return userEvent.QUIT

            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_ESCAPE:
                    # self.userEvents.append(userEvent.QUIT)
                    quit()
                    return userEvent.QUIT


                if _gameState == GameState.RUNNING:
                    if event.key == pygame.K_h:
                        print('higher_key')
                        return userEvent.CLICKED_HIGHER
                    if event.key == pygame.K_l:
                        print('lower_key')
                        return userEvent.CLICKED_LOWER
                
                if _gameState == GameState.GAMEOVER:
                    if event.key == pygame.K_r:
                        print('r')
                        return userEvent.START
                    if event.key == pygame.K_q:
                        print('q')
                        return userEvent.QUIT
                
                if _gameState == GameState.MAINMENU:

                    if event.key == pygame.K_RETURN:
                        return userEvent.START
                    
                    if event.key in allowedPyKeys:
                        # print('event.key', event.key)
                        return userEvent.TYPING, pygame.key.name(event.key)
                    
                    if event.unicode in swedishKeys.keys():
                        print('unicode', event.unicode)
                        return userEvent.TYPING, event.unicode
                    
                    if event.key == pygame.K_1:
                        print('key_1')
                        return userEvent.START
                    


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
                
                if event.key == pygame.K_w:
                    print('w')
                    return userEvent.W
                if event.key == pygame.K_a:
                    print('a')
                    return userEvent.A
            

                
                
            # if ()