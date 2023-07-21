import pygame
from pygame import Color

from EventHandler import EventManager, userEvent, GameState
from GameObject import *
from gameSession import GameSession, HIDDEN, BOTTOM, TOP, HIDDEN2

from utils.VARS import COLOR

WIDTH = 1920//2
HEIGHT = 1080//2
VCENTER = HEIGHT//2
HCENTER = WIDTH//2

CENTER = (WIDTH//2, HEIGHT//2)

RCOL_WIDTH = 200
RCOL_CENTER = (WIDTH - RCOL_WIDTH//2, VCENTER)

LCOL_WIDTH = WIDTH - RCOL_WIDTH
LCOL_HCENTER = LCOL_WIDTH//2
LCOL_CENTER = (LCOL_HCENTER, VCENTER)

TL = (0, 0)





pygame.init()

class GameManager:

    active = True
    eventManager =  EventManager()
    gameState = GameState.INIT
    # GameObject.debug = True
    
    dt = pygame.time.Clock().tick(60) // 1000

    # text = Text(TL, "Hello World", pygame.font.SysFont('Arial', 50), COLOR.WHITE)
    # btn = Button((0,50), (100, 50), txtColor = COLOR.BLUE_AUTOLIV2, font = pygame.font.SysFont('Arial', 20))
    # card = Card(TL, (RCOL_WIDTH, HEIGHT), COLOR.WHITE, COLOR.DARK_GRAY).MoveTo(RCOL_CENTER)


    # print(PauseMenu(CENTER, (200, 200), COLOR.WHITE, COLOR.DARK_GRAY).rect)

    # collection = Collection(LCOL_CENTER, []).MoveTo(LCOL_CENTER-Vector2(200, 0))

    
    
    pauseMenu = PauseMenu(CENTER, (500, 500)).Enable(False)
    gameSession = GameSession()
    

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game")
    
    def Update(self):
        for gameObject in GameObject.instances:
            gameObject.OnUpdate(self.dt)
        
    def Draw(self):
        self.screen.fill(COLOR.BLACK)
        
        for gameObject in GameObject.instances:
            gameObject.OnDraw(self.screen)

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
            self.pauseMenu.Enable( True) 
            self.gameState = GameState.PAUSED 

        elif event == userEvent.RESUME:
            self.menuShow = False
            self.pauseMenu.Enable(False)
            self.gameState = GameState.RUNNING
            print('resume')

        elif event == userEvent.DEBUG_ANIM:
            print( GameObject.instances)
        elif event == userEvent.START:
            self.gameState = GameState.START




game = GameManager()
# game.InitAnimations()

while game.active:
    game.Update()
    # print(game.gameState)
    game.Draw()
    game.HandleEvents()
