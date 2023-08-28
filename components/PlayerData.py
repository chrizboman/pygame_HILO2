import json
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Player:
    playerName : str
    highscore : int
    tries : int
    lastTry : datetime




# class HighScores:
#     path = 'data/highscores.json'
#     playerHighScores : list[Player] = None

#     def __init__(self) -> None:
#         try:
#             self.Load()
#         except:
#             self.playerHighScores = []
        
#     def Load(self):
#         with open(self.path) as json_file:
#             self.playerHighScores = json.load(json_file)

#     def Save(self):
#         with open(self.path, "w") as outfile:
#             json.dump(self.playerHighScores, outfile)
        
#     def Add(self, playerName, score):
#         if playerName in self.playerHighScores:
#             if score > self.playerHighScores[playerName]:
#                 self.playerHighScores[playerName] = score
#         else:
#             self.playerHighScores[playerName] = score        
        
#         self.Sort()
#         self.Save()

#     def Sort(self):
#         self.playerHighScores = dict(sorted(self.playerHighScores.items(), key=lambda item: item[1], reverse=True))







class HighScores:
    path = 'data/highscores.json'
    playerHighScores = {}

    def __init__(self) -> None:
        try:
            self.Load()
        except:
            self.playerHighScores = {}
    def Load(self):
        with open(self.path) as json_file:
            self.playerHighScores = json.load(json_file)

    def Save(self):
        with open(self.path, "w") as outfile:
            json.dump(self.playerHighScores, outfile)
        
    def Add(self, playerName, score):
        if playerName in self.playerHighScores:
            if score > self.playerHighScores[playerName]:
                self.playerHighScores[playerName] = score
        else:
            self.playerHighScores[playerName] = score        
        
        self.Sort()
        self.Save()

    def Sort(self):
        self.playerHighScores = dict(sorted(self.playerHighScores.items(), key=lambda item: item[1], reverse=True))
        
