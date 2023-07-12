import pygame
from VARS import COLOR

class Button():
    def __init__(self, text: str, pos_x: int, pos_y: int, width: int, height: int, fromCenter=False):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
    
    def Draw(self, screen ):
        pygame.draw.rect(screen, COLOR.WHITE, (self.pos_x, self.pos_y, self.width, self.height))
        if self.text != '':
            font = pygame.font.Font(None, 30)
            text = font.render(self.text, True, COLOR.BLACK)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

class Text():
    pass

class PromptPanel():
    width: int
    height: int
    pos_x: int
    pos_y: int
    prompt: Text = 'Here goes the prompt'
    answer: Text = 'Here goes the answer'
    source: Text = 'Here goes the source'
    btn_higher : Button = None
    btn_lower : Button = None
