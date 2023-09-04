import numpy as np
import json
import pygame
from pygame import QUIT
from dataclasses import dataclass
from pygame import Vector2

from components.utils.FONTS import *
from components.utils.VARS import *
from components.utils.PData import Prompt
from components.NameEditor import NameEditor
from components.PlayerData import PlayerData
# from components.components import Button, Card, Collection, PauseMenu, GameObject, Text
from gameSession import GameSession
from GameObjects import GameObject, Button, Card, Collection, PauseMenu, Text, ScoreCard, GameOverMenu, StartMenu, StartMenuLeaderBoard, TimerBar

from components.Mixer import Mixer

from EventHandler import EventManager, userEvent, GameState

import random
import tween

scale = 1


OO = Vector2(0,0)


FULLSCREEN = False





        

# test = ImportCalories().Prompts20()

pygame.init()

class GameManager:

    mixer = Mixer()
    mixer.PlayMusic('menu')
    

    playerData = PlayerData()
    # highScoresNew = HighScoresNew()

    menuShow = False

    active = True
    gameSession = None
    highscore : int = 0
    eventManager = EventManager()

    dt = 0
    clock = pygame.time.Clock()
    # screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN) if FULLSCREEN else pygame.display.set_mode((WIDTH, HEIGHT) )
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Game")

    GameObject.screen = screen

    # timerBar = TimerBar()

    gameState = GameState.MAINMENU

    scoreCard : ScoreCard = ScoreCard(RCOL_CENTER, (RCOL_WIDTH, HEIGHT))

    pauseMenu : PauseMenu = PauseMenu().Enable(False)
    gameOverMenu : GameOverMenu = GameOverMenu().Enable(False)

    startMenuTemp = StartMenuLeaderBoard().Enable(True)

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
        self.scoreCard.LoadLeaderboard(self.playerData.HighScores(ScoreCard.HIGHSCORESTOSHOW))
        if self.gameSession and self.gameSession.score == 50:
            self.playerData.AddPlayerScore(self.nameEditor.playerName, self.gameSession.score)
            self.GameOver()


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
            self.startMenuTemp.LoadLeaderboard(self.playerData.HighScores(self.startMenuTemp.HIGHSCORESTOSHOW))
        
        

        


        
    def Draw(self):     

        self.screen.fill(COLOR.BLACK)

        if self.gameState == GameState.MAINMENU:
            self.startMenuTemp.txt_name.text = self.nameEditor.playerName
            self.startMenuTemp.Draw()
            line = pygame.draw.line(self.screen, COLOR.BLACK, (1300,100), (1300, 1000))

        if self.gameState == GameState.RUNNING:
            self.scoreCard.Draw()
            self.gameSession.Draw()
            self.gameSession.timerBar.Draw()
                    
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

        elif event == userEvent.START:
            self.gameState = GameState.START
            self.mixer.PlayMusic('playing')
            self.mixer.PlaySound('start')


    def GameOver(self):
        self.gameState = GameState.GAMEOVER
        self.playerData.AddPlayerScore(self.nameEditor.playerName, self.gameSession.score)
        self.gameOverMenu.SetName(self.nameEditor.playerName)
        # self.highScoresNew.Add(self.nameEditor.playerName, self.gameSession.score)
        self.mixer.Stop()
        self.mixer.PlaySound('gameOver')
        return




game = GameManager()
# game.InitAnimations()

while game.active:
    game.Update()
    game.Draw()
    game.HandleEvents()
