from components.utils.PData import Prompt, ImportCalories
from datetime import datetime, timedelta


from components.utils import PData
from components.PlayerData import HighScoresNew, Player



player1 = Player('test', 10, 1, datetime.now() - timedelta(days=1))
player2 = Player('test', 10, 1, datetime.now())

highscores = HighScoresNew()

highscores.Add(player1)




