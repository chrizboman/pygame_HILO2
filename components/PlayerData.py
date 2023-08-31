import json
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Player:
    playerName : str
    highscore : int
    tries : int
    lastTry : datetime




class HighScoresNew:
    path = 'data/highscores_New.json'
    playerHighScores : list[Player] = None

    def __init__(self) -> None:
        try:
            self.Load()
        except:
            self.playerHighScores = []
        
    def Load(self):
        with open(self.path) as json_file:
            self.playerHighScores = json.load(json_file)

    def Save(self):
        with open(self.path, "w") as outfile:
            json.dump(self.playerHighScores, outfile)
        
    def Add(self, playerClass):
        playerName = playerClass.playerName
        score = playerClass.highscore

        for existing_player in self.playerHighScores:
            if existing_player.playerName == playerClass.playerName:
                if score > player.highscore:
                    player.highscore = score
                player.tries += 1
                player.lastTry = datetime.now()
                self.Sort()
                self.Save()
                return
        # if not in list
        self.playerHighScores.append(Player(playerName, score, 1, datetime.now()))

    def Sort(self):
        pass

    
    # def __iter__(self):
    #     self.n = 0
    #     return self

    # def __next__(self):
    #     if self.n <= self.max:
    #         result = 2 ** self.n
    #         self.n += 1
    #         return result
    #     else:
    #         raise StopIteration







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
        
