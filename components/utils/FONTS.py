import pygame

pygame.font.init()

mini_font = pygame.font.Font(None, 30)
small_font = pygame.font.Font(None, 40)
medium_font = pygame.font.Font(None, 50)
large_font = pygame.font.Font(None, 80)
huge_font = pygame.font.Font(None, 200)

prompt_font = pygame.font.SysFont('franklingothicdemicond', 40)
question_mark = pygame.font.Font(None, 200)

# playername_Scoreboard = pygame.font.SysFont('franklingothicdemicond', 30)
playername_Scoreboard = pygame.font.SysFont('bernardcondensed', 30)
# playername_Scoreboard = pygame.font.SysFont('bauhaus93', 30)
# Question_font = 

introfont_mono = pygame.font.SysFont("FreeMono, Monospace", 100, bold=True)
small_font_mono = pygame.font.SysFont("FreeMono, Monospace", 20, bold=True)


if False:
    fonts = pygame.font.get_fonts()
    [print(font) for font in fonts]