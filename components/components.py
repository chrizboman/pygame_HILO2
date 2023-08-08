import pygame

if __name__ == "__main__":
    "Do not run this file directly"
    "Run main.py instead"
else:
    from utils.VARS import COLOR, CONSTANTS
    from utils.FONTS import small_font, medium_font, large_font, huge_font

WIDTH = CONSTANTS.WIDTH
HEIGHT = CONSTANTS.HEIGHT
HCENTER = WIDTH//2
VCENTER = HEIGHT//2
MIDDLE = (WIDTH, HEIGHT)

class Button():
    corner_rad = 10
    def __init__(self, text, size : tuple[int, int], x_center = HCENTER, y_center = VCENTER, font = small_font):
        self.text = text
        self.left = x_center - size[0]//2
        self.top = y_center + size[1]//2
        self.width = size[0]
        self.height = size[1]
        self.font = font
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
    
    def Draw(self, screen):
        pygame.draw.rect(screen, COLOR.WHITE, self.rect, border_radius = self.corner_rad, width=2)

        text = self.font.render(self.text, True, COLOR.BLACK)
        text_rect = text.get_rect()
        screen.blit(text, text_rect)
        



class Text():
    enabled = True
    def __init__(self, font, x, y, color = (255, 255, 255), text:str = "Text Box"  ) -> None:
        self.font : pygame.font= font
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        
    def Draw(self, screen):
        if self.enabled:
            score_text = self.font.render(self.text, True, self.color)
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (self.x , self.y)
            screen.blit(score_text, score_text_rect)
    
    def UpdateText(self, text):
        self.text = text







class RectBox:
    rect : pygame.Rect = None
    def __init__(self, size : tuple[2], color, xy_center = (HCENTER, VCENTER), border:int = 0) -> None:
        self.xy_center = xy_center
        self.color = color
        width = size[0]
        height = size[1]
        left = xy_center[0] - width//2
        top = xy_center[1] - height//2
        print(left, top, width, height)
        self.rect = pygame.Rect(left, top, width, height)
        self.border = border
    
    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border)



class GameOverBox:
    TOP = 0.0
    size = (500, 500)
    highscore = 0

    txt_GO = Text(huge_font, HCENTER, TOP + 200, COLOR.BLACK, text="Game Over")
    txt_Score = Text(small_font, HCENTER, TOP + 300, COLOR.BLACK, text="Score: " + str(0))
    btn_restart = Button("Restart", (100, 50), y_center=TOP + 400)
    btn_quit = Button("Quit", (100, 50), y_center=TOP + 450)
    rect_BG = RectBox(size, COLOR.WHITE, border=20)        

    def SetScore(self, score: int):
        self.scoreText.UpdateText("Score: " + str(score))
        if score > self.highscore:
            self.highscore = score
            self.highscoreText.UpdateText("Highscore: " + str(self.highscore))
    
    def Draw(self, screen):
        for drawable in [self.rect_BG, self.txt_GO, self.txt_Score, self.btn_restart, self.btn_quit]:
            drawable.Draw(screen)


