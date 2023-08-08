import pygame
from pygame import Rect, Vector2
from pygame.math import Vector2
from pygame.color import Color as pgColor
from pygame.font import Font
from typing import Callable as function
# from GameObjects import GameObject

from components.utils.FONTS import *
from components.utils.VARS import COLOR, WIDTH, HEIGHT

from components.utils.PData import Prompt

# import tween
from components.utils.Tweener import Tween
import random

import tween

# WIDTH = 1920//2
# HEIGHT = 1080//2



class GameObject():
    instances : list = []
    enabled = True
    debug = False
    screen = None
    scale : float = 1
    isScaled = True
    fromCenter : Vector2
    dummy : int = 0
    # tweener : Tween = None

    def __init__(self, positionCenter : Vector2):
        # super().__init__(positionCenter)
        GameObject.instances.append(self)
        self.position : Vector2 = positionCenter
        self.size = Vector2(0,0)
        self.rect : Rect = Rect(*positionCenter, *self.size)
        self.screen = GameObject.screen

        self.randomDebugColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        return self

    def MoveTo(self, positionCenter : Vector2):
        self.position = positionCenter
        self.rect.center = self.position
        return self
    
    # def TweenTo(self, pos: Vector2, duration: float):
    #     return super().TweenTo(pos, duration)

    def OnUpdate(self, dt : float):
        pass

    def Scale(self, scale : float):
        self.scale = scale
        return self
    
    def TweenTo(self, pos,  duration : float, tweenType : str = "easeInOutCubic"):
        self.tween = tween.to(self, "position", Vector2(pos), duration, tweenType)
        self.tween.on_update(lambda: self.MoveTo(self.position))
        # self.tween.on_update(lambda: print(self.position) )
        return self
    
    def TweenScale(self, value, duration : float, tweenType : str = "easeInOutCubic" ):
        self.tween = tween.to(self, "scale", value, duration, tweenType)
        self.tween.on_update(lambda: self.Scale(self.scale))

    def WaitForThen(self, duration : float, func : callable):
        self.tween = tween.to(self, "dummy", 0, duration, "linear")
        self.tween.on_complete(func)
        return self

    def Draw(self):
        if self.debug:
            pygame.draw.circle(self.screen, self.randomDebugColor, self.position, 5)
            unscaledRect = Rect(0,0, *self.size)
            unscaledRect.center = self.position
            pygame.draw.rect(self.screen, self.randomDebugColor, unscaledRect, 1)
        return self

    def __str__(self) -> str:
        return f'GameObject {__name__} at {self.position}'
    
    def __repr__(self) -> str:
        return f'GameObject {__name__} at {self.position}'
    
    # def __eq__(self, o: object) -> bool:
    #     return self.position == o.position

    def Enable(self, enable: bool):
        self.enabled = enable
        return self
    
    @property
    def x(self):
        return self.position[0]
    @property
    def y(self):
        return self.position[1]
    

        
        
        
        



class Text(GameObject):
    UseAntialias = True
    def __init__(self, positionCenter : Vector2, text = "TextBox", font : Font = small_font , color : pgColor= COLOR.BLACK, isnumber : bool = False):
        super().__init__(positionCenter)
        self.text = text
        self.font = font
        self.color = color
        self.surface = self.font.render(self.text, self.UseAntialias, self.color)
        self.rect = self.surface.get_rect(center = self.position)
        self.needUpdate = False
    
    def Draw(self):
        if type(self.text) == int or type(self.text) == float:
            text = str ( int (self.text ))
        else:
            text = str(self.text)
        super().Draw()
        if (self.enabled):
            self.surface = self.font.render(text, self.UseAntialias, self.color)
            textSurface = pygame.transform.smoothscale_by(
                self.surface, self.scale)
            self.rect = textSurface.get_rect(center = self.position)
            self.screen.blit(textSurface, self.rect)
        


class Button(GameObject):
    CORNER_RADIUS = 10
    BORDER_WIDTH = 5
    HILO_BTN_SIZE = (100, 50)

    def __init__(self, 
                positionCenter : Vector2,
                size : Vector2,
                text : str = "Button", 
                font : Font = small_font,
                txtColor : pgColor = (128, 128, 128),
                btnColor : pgColor = (128, 128, 128),
                borderColor : pgColor = (255, 255, 255),
                onClick : function = None):
        super().__init__(positionCenter)

        self.size = size
        self.text = text
        self.font = font
        self.txtColor = txtColor
        self.btnClor = btnColor
        self.borderColor = borderColor
        self.onClick = onClick
        
        width = self.size[0]
        height = self.size[1]
        left = self.position[0] - width//2
        top = self.position[1] - height//2
        self.rect = pygame.Rect(left, top, width, height)
        self.textSurface = self.font.render(self.text, True, self.txtColor)
        self.textRect = self.textSurface.get_rect(center = self.position)
        self.textRect.center = self.rect.center
    
    # def Scale(self, scale : float):
    #     super().Scale(scale)

    def Draw(self):
        # self.rect.center = self.position
        screen = self.screen
        newRect = self.rect.copy()
        newRect.scale_by_ip(self.scale)
        if (self.enabled):
            #Draw the inner background
            pygame.draw.rect(screen,
                             self.borderColor,
                             newRect,
                             border_radius = self.CORNER_RADIUS,
            )
            #Draw the outer border
            pygame.draw.rect(screen, 
                            self.btnClor, 
                            newRect, 
                            border_radius = self.CORNER_RADIUS, 
                            width = self.BORDER_WIDTH)
            #Draw the text
            if self.scale == 1:
                textpos = (self.x - self.textSurface.get_width()//2, self.y - self.textSurface.get_height()//2)
                textpos = textpos[0] * self.scale, textpos[1] * self.scale
                screen.blit(self.textSurface, textpos)
        
        if self.debug:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            pygame.draw.circle(screen, (255, 0, 0), self.position, 5)
    
    def Scale(self, scale: float):
        return super().Scale(scale)
        




class Card (GameObject):
    BG_COLOR = (250,250, 250)
    BORDER_COLOR = (100, 100, 100)
    BORDER_WIDTH = 8
    CORNER_RADIUS = 15
    MARGIN = 10

    def __init__(self, 
                 positionCenter : Vector2, 
                 size : Vector2, 
                 colorBG : pgColor = BG_COLOR,
                 colorBorder : pgColor = BORDER_COLOR,):
        super().__init__(positionCenter)
        self.size = size - Vector2(self.MARGIN*2, self.MARGIN*2)
        self.colorBG = colorBG
        self.colorBorder = colorBorder
        self.rect = pygame.Rect(0,0, self.size[0], self.size[1])
        self.rect.center = self.position
        
    def Draw(self):
        if (self.enabled):
            pygame.draw.rect(self.screen, self.colorBG, self.rect, border_radius=self.CORNER_RADIUS+self.BORDER_WIDTH)
            pygame.draw.rect(self.screen, self.colorBorder, self.rect, self.BORDER_WIDTH, self.CORNER_RADIUS)
        
        if self.debug:
            fullRect = pygame.Rect(self.x - self.size[0]//2, self.y - self.size[1]//2, self.size[0], self.size[1])
            pygame.draw.rect(self.screen, (255, 0, 0), fullRect, 1)
            pygame.draw.circle(self.screen, (255, 0, 0), self.position, 5)
        

class MENU():
    CORNER_RADIUS = 10



class Collection(GameObject):
    
    
    def __init__(self, positionCenter: Vector2, gameObjects : list[GameObject] = []):
        super().__init__(positionCenter)
        self.tposition = Vector2(positionCenter)
        self.gameObjects : list[GameObject] = gameObjects

        for child in self.gameObjects:
            child.MoveTo((Vector2(self.position) + child.position ))
        # self.MoveTo(self.position)
    
    def Add(self, gameObject : GameObject):
        gameObject.MoveTo((Vector2(self.position) + gameObject.position ))
        self.gameObjects.append(gameObject)
        return gameObject
    
    def AddMany(self, gameObjects : list[GameObject]):
        for gameObject in gameObjects:
            gameObject.MoveTo((Vector2(self.position) + gameObject.position ))
        self.gameObjects.extend(gameObjects)
        return self

    def MoveTo(self, pos : Vector2):
        distance = Vector2( Vector2(pos) - self.position )
        for child in self.gameObjects:
            child.MoveTo((distance + child.position ))
        super().MoveTo(pos)
        return self
    
    def TweenTo(self, pos : Vector2, duration : float, tweenType : str = "easeInOutCubic"):
        self.tweenTo = tween.to(self, "tposition", Vector2(pos), duration, tweenType)
        self.tweenTo.on_update(lambda: self.MoveTo(self.tposition))

    
    def Draw(self):
        self.MoveTo(self.position)
        super().Draw()
        for gameObject in self.gameObjects:
            gameObject.Draw()
        return self
        #these are already drawn automatically by themselves

    def Enable(self, enable: bool):
        super().Enable(enable)
        for gameObject in self.gameObjects:
            gameObject.Enable(enable)
        return self
    
    # def Scale(self, scale: float):
    #     super().Scale(scale)
    #     for gameObject in self.gameObjects:
    #         gameObject.Scale(scale)
    #     return self





class PauseMenu(Collection, MENU):
    showing : bool = False
    CORNER_RADIUS = MENU.CORNER_RADIUS
    BACKGROUND_COLOR = COLOR.WHITE
    BORDER_COLOR = COLOR.DARK_GRAY
    POSIITON = (WIDTH//2, HEIGHT//2)
    SIZE =  (WIDTH-100, HEIGHT-100)
    def __init__(self):
        
        self.card = Card((0,0), self.SIZE)
        self.txt_Title = Text((0,-100), "PAUSED", font = huge_font)
        self.btn_Restart : Button = Button((0,100), (100, 50), "Restart", font = small_font)
        self.btn_Quit : Button = Button((0,150), (100, 50), "Quit", font = small_font)

        super().__init__(self.POSIITON, [self.card, self.btn_Quit, self.btn_Restart, self.txt_Title])

        self.BGcolor = self.BACKGROUND_COLOR
        self.BDcolor = self.BORDER_COLOR


    # def OnDraw(self, screen):
    #     #can i make a transparent background under the pausemenu?
    #     pass

    def Toggle(self):
        self.showing = not self.showing
        return self




class GameOverMenu(Collection):
    CORNER_RADIUS = 10
    BACKGROUND_COLOR = COLOR.WHITE
    BORDER_COLOR = COLOR.DARK_GRAY

    POSITION = Vector2( WIDTH//2, HEIGHT//2 )
    SIZE = Vector2( WIDTH-100, HEIGHT-100 )

    def __init__(self):
        size = self.SIZE
        positionCenter = self.POSITION
        
        self.card = Card((0,0), size)
        self.txt_Title = Text((0,-100), "GAME OVER", font = huge_font, color = COLOR.BLACK)
        self.txt_Score = Text((0,-20), "Score: ", font = large_font, color = COLOR.BLACK)
        self.btn_Restart : Button = Button((0,100), (100, 50), "Restart", font = small_font)
        self.btn_Quit : Button = Button((0,150), (100, 50), "Quit", font = small_font)

        super().__init__(positionCenter, [self.card, self.txt_Score, self.btn_Quit, self.btn_Restart, self.txt_Title])

        self.BGcolor = self.BACKGROUND_COLOR
        self.BDcolor = self.BORDER_COLOR
        self.size = size


    def Show(self, score : int = 0, highscore : int = 0):
        self.txt_Score.text = f'Score: {score}'
        self.Enable(True)
        self.Scale(0)
        # self.TweenScale(1, 1.5)
        return self



class ScoreCard(Collection):
    
    def __init__(self, positionCenter: Vector2, size : Vector2):
        super().__init__(positionCenter)
        self.score = 0
        self.highscore = 0
        self.card                = self.Add( Card((0,0), size) )
        self.txt_score           = self.Add( Text((0,-200), 'Score: ', font = medium_font) )
        self.txt_scoreNum        = self.Add( Text((0,-150), f'{self.score}', font = huge_font) )
        self.txt_highscore       = self.Add( Text((0,0), 'Highscore: ', font = medium_font) )
        self.txt_highscoreNum    = self.Add( Text((0,50), f'{self.highscore}', font = huge_font))
        self.txt_debug           = self.Add( Text((0,150), 'Debug', font = small_font))
