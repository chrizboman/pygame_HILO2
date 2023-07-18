import pygame
import tween
from enum import Enum
from utils.PData import Prompt, ImportCalories

if __name__ == "__main__":
    "Do not run this file directly"
    "Run main.py instead"
else:
    from utils.VARS import COLOR, CONSTANTS
    from utils.FONTS import mini_font, small_font, medium_font, large_font, huge_font

WIDTH = CONSTANTS.WIDTH
HEIGHT = CONSTANTS.HEIGHT
HCENTER = WIDTH//2
VCENTER = HEIGHT//2
MIDDLE = (WIDTH, HEIGHT)

# LEFTCENTER 

promptsTable = ImportCalories()
examplePrompt = promptsTable.PromptsOne()


class Button():
    corner_rad = 5
    def __init__(self, text, size : tuple[int, int], x_center = HCENTER, y_center = VCENTER, font = small_font, color = COLOR.WHITE, border = None):
        self.text = text
        self.x_c = x_center
        self.y_c = y_center
        self.width = size[0]
        self.height = size[1]
        self.font = font
        self.color = color
        self.border = border

        left = self.x_c - self.width//2
        top = self.y_c - self.height//2
        self.rect = pygame.Rect(left, top, self.width, self.height)
        
    def Draw(self, screen):
        if self.border:
            pygame.draw.rect(screen, self.border, self.rect, border_radius = self.corner_rad, width = self.border)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius = self.corner_rad )

        text = self.font.render(self.text, True, COLOR.BLACK)
        text_rect = text.get_rect()
        screen.blit(text, (self.x_c - text_rect.width//2, self.y_c - text_rect.height//2 ))
        

    def Position(self, y):
        self.y_c = y
        self.rect.center = (self.x_c, y)


    

class HILOButtons():
    _SIZE = (100, 50)
    _BTN1_DFC = -100
    _BTN2_DFC = 100
    _y_center = 0

    button1 = Button("Higher", _SIZE, y_center= _y_center, color=COLOR.GREEN, border=5)
    button2 = Button("Lower"  , _SIZE, y_center= _y_center, color=COLOR.RED, border=5)

    def Draw(self, screen):
        self.button1.Draw(screen)
        self.button2.Draw(screen)

    def Position(self, y):
        self.button1.Position(y)
        self.button2.Position(y)



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
    
    def Position(self, y):
        self.x, self.y = (self.x, y)





class RectBox:
    rect : pygame.Rect = None
    def __init__(self, size : tuple[2], color, x_center = HCENTER, y_center = VCENTER, corner:int = 0, border:int = 0) -> None:
        self.x_c = x_center
        self.y_c = y_center
        self.color = color
        width = size[0]
        height = size[1]
        left = x_center - width//2
        top = y_center - height//2
        print(left, top, width, height)
        self.rect = pygame.Rect(left, top, width, height)
        self.border = border
        self.corner = corner
    
    def Draw(self, screen):
        if self.border:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=self.corner, width=self.border)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=self.corner)
    
    def Position(self, y):
        self.rect.center = (self.x_c, y)




class GameOverMenu:
    TOP = 0.0
    size = (500, 500)

    rect_BG = RectBox(size, COLOR.WHITE, corner=20)
    rect_border = RectBox(size, COLOR.DARK_GRAY, border=10, corner=20)       
    txt_GO = Text(huge_font, HCENTER, 150, COLOR.BLACK, text="Game Over")
    txt_Score = Text(small_font, HCENTER, 250, COLOR.BLACK, text="Score: " + str(0))
    btn_restart = Button("Restart"  , (100, 50), y_center= 400, color=COLOR.GREEN, border=5)
    btn_quit = Button(  "Quit"      , (100, 50), y_center= 470, color=COLOR.RED, border=5)

    def SetScore(self, score: int):
        self.scoreText.UpdateText("Score: " + str(score))
    
    def Draw(self, screen):
        self.rect_BG.Draw(screen)
        self.rect_border.Draw(screen)
        for drawable in [self.txt_GO, self.txt_Score, self.btn_restart, self.btn_quit]:
            drawable.Draw(screen)




class PauseMeny:
    size = (450, 450)

    rect_BG = RectBox(size, COLOR.WHITE, corner=20)
    rect_Border = RectBox(size, COLOR.DARK_GRAY, border=10, corner=20)
    txt_paused = Text(huge_font, HCENTER, 150, COLOR.BLACK, text="PAUSED")

    btn_resume = Button("Resume"  , (100, 50), y_center= 350, color=COLOR.GREEN, border=5)
    btn_quit = Button(  "Quit"      , (100, 50), y_center= 420, color=COLOR.RED, border=5)

    def SetScore(self, score: int):
        self.scoreText.UpdateText("Score: " + str(score))
    
    def Draw(self, screen):
        self.rect_BG.Draw(screen)
        self.rect_Border.Draw(screen)
        for drawable in [self.txt_paused, self.btn_resume, self.btn_quit]:
            drawable.Draw(screen)



class ScoreTable:
    margin = 10
    width = 200
    size = (width, HEIGHT-margin*2)
    x_center = WIDTH - width//2 - margin

    rect_BG = RectBox(size, COLOR.WHITE, corner=20, x_center=x_center)
    rect_border = RectBox(size, COLOR.DARK_GRAY, border=10, corner=20, x_center=x_center)

    txt_Score = Text(large_font, x_center, 100, COLOR.BLACK, text="Score:")
    txtNum_Score = Text(huge_font, x_center, 200, COLOR.BLACK,  str(0))
    txt_highscore = Text(medium_font, x_center, 350, COLOR.BLACK, text="Highscore: ")
    txtNum_highscore = Text(large_font, x_center, 420, COLOR.BLACK, str(0))

    def Draw(self, screen):
        self.rect_BG.Draw(screen)
        self.rect_border.Draw(screen)
        for drawable in [self.txt_Score, self.txtNum_Score, self.txt_highscore, self.txtNum_highscore]:
            drawable.Draw(screen)



class PromptCard():
    class Pos(Enum):
        HIDDEN = 0
        BOTTOM = 1
        TOP = 2
        HIDDEN2 = 3
    pos = Pos.HIDDEN

    prompt : Prompt = None

    margin = 10
    width = WIDTH - 200 - 3 *margin
    height = HEIGHT //2 - 2 * margin
    size = (width, height)
    x_center = width//2 + margin
    
    _currentPos = Pos.HIDDEN

    txt_prompt_dfc = - 100
    txt_source_dfc = 100
    txt_number_dfc = 0
    btns_dfc = 50

    _positions = {
        Pos.HIDDEN: HEIGHT + height//2,
        Pos.BOTTOM: HEIGHT//4 * 3,
        Pos.TOP: HEIGHT//4,
        Pos.HIDDEN2: -height//2
    }
    positions = [
        _positions[Pos.HIDDEN],
        _positions[Pos.BOTTOM],
        _positions[Pos.TOP],
        _positions[Pos.HIDDEN2]
    ]
    poss = [
        Pos.HIDDEN,
        Pos.BOTTOM,
        Pos.TOP,
        Pos.HIDDEN2
    ]

    y_center = _positions[Pos.HIDDEN]

    rect_BG = RectBox(size, COLOR.WHITE, corner=20, x_center=x_center, y_center=y_center)
    rect_border = RectBox(size, COLOR.DARK_GRAY, border=10, corner=20, x_center=x_center, y_center=y_center)
    txt_prompt = Text(large_font, x_center, y_center + txt_prompt_dfc, COLOR.BLACK, text="Prompt")
    txt_source = Text(mini_font, margin + 40, y_center + txt_source_dfc, COLOR.BLACK, text="*Source:")
    
    txt_number = Text(huge_font, x_center, y_center + txt_number_dfc, COLOR.BLACK, str(0))
    btn_higher = Button("Higher"  , (100, 50), x_center= x_center - 70, y_center= y_center + btns_dfc, color=COLOR.GREEN, border=5)
    btn_lower = Button(  "Lower"  , (100, 50), x_center= x_center + 70, y_center= y_center + btns_dfc, color=COLOR.RED, border=5)

    def __init__(self, prompt : Prompt, pos : Pos = Pos.HIDDEN) -> None:
        self.pos_i = 0
        self.pos = pos
        self.y_center = self._positions[pos]
        self.prompt = prompt
        self.UpdatePrompt(prompt)

    def UpdatePrompt(self, prompt : Prompt):
        self.txt_prompt.UpdateText(prompt.prompt)
        self.txt_number.UpdateText(str(prompt.answer))
        self.txt_source.UpdateText("*Source: " + prompt.source)

    def MoveTo(self, y):
        self.rect_BG.Position(y)
        self.rect_border.Position(y)
        self.txt_number.Position(y + self.txt_number_dfc)
        self.txt_prompt.Position(y + self.txt_prompt_dfc)
        self.txt_source.Position(y + self.txt_source_dfc)
        self.btn_higher.Position(y + self.btns_dfc)
        self.btn_lower.Position(y + self.btns_dfc)
        return self

    def Draw(self, screen):
        self.MoveTo(self.y_center)
        self.rect_BG.Draw(screen)
        self.rect_border.Draw(screen)
        self.txt_prompt.Draw(screen)
        self.txt_source.Draw(screen)

        if self.pos == self.Pos.BOTTOM or self.pos == self.Pos.HIDDEN:
            self.btn_higher.Draw(screen)
            self.btn_lower.Draw(screen)
        else:
            self.txt_number.Draw(screen)

    def AnimateTo(self, y_pos, time = 1, anim= 'easeInOutCubic'):
        return tween.to(self, 'y_center', y_pos, time, anim)
    
    def setPosition(self, pos):
        self._currentPos = pos
    
    def NextPos(self):
        self.pos_i += 1 if self.pos_i < len(self.positions) else 0
        y_pos = self.positions[self.pos_i]
        self.pos = self.poss[self.pos_i]
        
        
        self.AnimateTo(y_pos, 1, 'easeInOutCubic')




class Components:
    gameOverBox = GameOverMenu()
    pauseMeny = PauseMeny()
    promptCard = PromptCard(examplePrompt)
    # promptCard2 = PromptCard(1)
    scoreTable = ScoreTable()
    def SpawnPromptCard(self):
        return PromptCard()

    def DrawAll(self, screen):
        self.gameOverBox.Draw(screen)
        self.pauseMeny.Draw(screen)

        # self.PromptPanel.Draw(screen)