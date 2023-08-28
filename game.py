import numpy as np
import json
import pygame
from pygame import QUIT
from dataclasses import dataclass
from pygame import Vector2

from components.utils.FONTS import *
from components.utils.VARS import *
from components.utils.PData import Prompt, ImportCalories
from components.NameEditor import NameEditor
from components.PlayerData import *
# from components.components import Button, Card, Collection, PauseMenu, GameObject, Text
from gameSession import GameSession
from GameObjects import GameObject, Button, Card, Collection, PauseMenu, Text, ScoreCard, GameOverMenu, StartMenu

from EventHandler import EventManager, userEvent, GameState

import random
import tween

scale = .5

WIDTH = 1920 *scale
HEIGHT = 1080 * scale

VCENTER = HEIGHT//2
HCENTER = WIDTH//2

OO = Vector2(0,0)

CENTER = (WIDTH//2, HEIGHT//2)

RCOL_WIDTH = 400 * scale
RCOL_CENTER = (WIDTH - RCOL_WIDTH//2, VCENTER)

LCOL_WIDTH = WIDTH - RCOL_WIDTH
LCOL_HCENTER = LCOL_WIDTH//2
LCOL_CENTER = (LCOL_HCENTER, VCENTER)
LCOL_TCENTER = (LCOL_HCENTER, HEIGHT//4)
LCOL_BCENTER = (LCOL_HCENTER, HEIGHT - HEIGHT//4)








class Mixer:

    def __init__(self):
        pygame.mixer.init()
        self.correct = pygame.mixer.Sound('assets/sounds/bell.wav')
        self.wrong = pygame.mixer.Sound('assets/sounds/failure.wav')
        self.gameOver = pygame.mixer.Sound('assets/sounds/gameOver.mp3')
        self.click = pygame.mixer.Sound('assets/sounds/click.mp3')
        self.start = pygame.mixer.Sound('assets/sounds/explosion.wav')
    
    def PlayMusic(self, music : str):
        self.playing = music
        if music == 'menu':
            pygame.mixer.music.load('assets/music/menu.mp3')
            pygame.mixer.music.play()
        elif music == 'playing':
            pygame.mixer.music.load('assets/music/play.mp3')
            pygame.mixer.music.play()

    def PlaySound(self, sound : str):
        if sound == 'correct':
            self.correct.play()
        elif sound == 'wrong':
            self.wrong.play()
        elif sound == 'gameOver':
            self.gameOver.play()
        elif sound == 'click':
            self.click.play()
        elif sound == 'start':
            self.start.play()
        
    def Stop(self):
        pygame.mixer.music.fadeout(1000)

        

# test = ImportCalories().Prompts20()

pygame.init()

class GameManager:

    mixer = Mixer()
    mixer.PlayMusic('menu')

    highScores = HighScores()

    menuShow = False

    active = True
    gameSession = None
    highscore : int = 0
    eventManager = EventManager()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    # GameObject.debug = True
    GameObject.screen = screen


    gameState = GameState.MAINMENU

    scoreCard : ScoreCard = ScoreCard(RCOL_CENTER, (RCOL_WIDTH, HEIGHT))

    pauseMenu : PauseMenu = PauseMenu().Enable(False)
    gameOverMenu : GameOverMenu = GameOverMenu().Enable(False)

    startMenuTemp = StartMenu().Enable(True)

    listPrompts = ImportCalories().Prompts20()

    # prompt1 = listPrompts.pop(0)
    # prompt2 = listPrompts.pop(0)

    # promptCard1 : PromptCard = PromptCard(LCOL_TCENTER, (LCOL_WIDTH, HEIGHT//2), prompt1)
    # promptCard2 : PromptCard = PromptCard(OO, (LCOL_WIDTH, HEIGHT//2), prompt2, True).MoveTo(LCOL_BCENTER)

    btn = Button((0,0), (100, 50), 'Start', font=medium_font).MoveTo(LCOL_CENTER)

    circle = pygame.draw.circle(screen, COLOR.WHITE, (LCOL_CENTER), 40)
    circle2 = pygame.draw.circle(screen, COLOR.LIGHT_GRAY, (LCOL_CENTER), 40, width=6)

    coll = Collection((CENTER), [])
    coll.Add(
        Button((0,0), (100, 50), 'collection', font=medium_font)
    )

    print('instances' , len(GameObject.instances))

    nameEditor : NameEditor = NameEditor()



    def Update(self):
        pygame.display.set_caption(f"FPS: {int(self.clock.get_fps())}, gamestate: {self.gameState}, playing as: {self.nameEditor.playerName}, lat. usr. event: {self.lastEvent}", )
        self.dt = self.clock.tick(60)/1000

        currentScore = self.gameSession.score if self.gameSession else 0
        self.scoreCard.UpdateScore(currentScore)
        self.highscore = currentScore if currentScore > self.highscore else self.highscore
        self.scoreCard.UpdateHighscore(self.highscore)
        self.scoreCard.UpdateName(self.nameEditor.playerName)
        self.scoreCard.LoadLeaderboard(self.highScores.playerHighScores)


        if self.gameState == GameState.START:
            if self.gameSession:
                self.gameSession.gameOver = False
            print('Starting new game')
            self.gameSession = GameSession(self.mixer)         
            self.gameState = GameState.RUNNING
            pass

        
        if self.gameState == GameState.RUNNING:
            tween.update(self.dt)
            if self.gameSession.gameOver:
                self.GameOver()
                return
            
            for gameObject in GameObject.instances:
                gameObject.OnUpdate(self.dt)
                
                
        if self.gameState == GameState.ANIMATING:
            tween.update(self.dt)
            for gameObject in GameObject.instances:
                gameObject.OnUpdate(self.dt)
            if self.gameSession.animationComplete:
                self.gameSession.animationComplete = False
                self.gameState = GameState.RUNNING
            
            if self.gameSession.gameOver:
                self.GameOver()
                return
        
        if self.gameState == GameState.GAMEOVER:
            pass

        if self.gameState == GameState.MAINMENU:
            self.startMenuTemp.UpdateName(str(self.nameEditor.playerName))
        
        

        


        
    def Draw(self):     

        self.screen.fill(COLOR.BLACK)

        if self.gameState == GameState.MAINMENU:
            self.startMenuTemp.txt_name.text = self.nameEditor.playerName
            self.startMenuTemp.Draw()

        if self.gameState == GameState.RUNNING:
            self.scoreCard.Draw()
            self.gameSession.Draw()
                    
        if self.gameState == GameState.ANIMATING:
            self.gameSession.Draw()
            self.scoreCard.Draw()

        if self.gameState == GameState.PAUSED:
            self.pauseMenu.Draw()
        
        if self.gameState == GameState.GAMEOVER:
            self.gameOverMenu.Enable(True)
            self.gameOverMenu.SetScore(self.gameSession.score)
            self.gameOverMenu.Draw()
        
        if self.gameState == GameState.GAMEOVER:
            self.gameOverMenu.Draw()

        # self.scoreCard.TweenTo(pygame.mouse.get_pos(), 0.1)
        # self.startMenuTemp.Draw()

        pygame.display.update()

    



    lastEvent = None
    def HandleEvents(self):
        event = self.eventManager.CheckForInput(self.gameState)
        if event : self.lastEvent = event
        
        if isinstance(event, tuple):
            # has sent a TYPING with a data string
            char = event[1]
            self.nameEditor.InputChar(char)

        if event == userEvent.QUIT: #never happen, it is handled in EventHandler
            self.gameState = GameState.MAINMENU
            self.mixer.PlayMusic('menu')
            self.nameEditor = NameEditor()
            self.gameSession = None
            print('quit')

        elif event == userEvent.CLICKED_HIGHER:
            self.mixer.PlaySound('click')
            self.gameState = GameState.ANIMATING
            self.gameSession.ClickHigher(True)
            
        elif event == userEvent.CLICKED_LOWER:
            self.mixer.PlaySound('click')
            self.gameState = GameState.ANIMATING
            self.gameSession.ClickHigher(False)

        elif event == userEvent.PAUSE:
            self.pauseMenu.Enable(True)
            self.gameState = GameState.PAUSED

        elif event == userEvent.RESUME:
            self.pauseMenu.Enable(False)     
            self.gameState = GameState.RUNNING      

        elif event == userEvent.DEBUG_ANIM:
            self.scoreCard.TweenTo(Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT) ), 5)
            pass
            
        elif event == userEvent.W:
            self.btn.scale = 1

        elif event == userEvent.A:
            pass 

        elif event == userEvent.START:
            self.gameState = GameState.START
            self.mixer.PlayMusic('playing')
            self.mixer.PlaySound('start')


    def GameOver(self):
        self.gameState = GameState.GAMEOVER
        self.gameOverMenu.SetName(self.nameEditor.playerName)
        self.highScores.Add(self.nameEditor.playerName, self.gameSession.score)
        self.mixer.Stop()
        self.mixer.PlaySound('gameOver')
        return











game = GameManager()
# game.InitAnimations()

while game.active:
    game.Update()
    game.Draw()
    game.HandleEvents()
