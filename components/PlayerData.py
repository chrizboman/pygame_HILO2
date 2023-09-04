import json
from dataclasses import dataclass
from collections import OrderedDict
from datetime import datetime
import pickle 



class PlayerData:
    path = 'data/playerData.json'
    players = {}

    def __init__(self) -> None:
        try:
            self.Load()
        except:
            self.players = {}
            self.Save()
    
    def Load(self):
        with open(self.path) as json_file:
            self.players = json.load(json_file)
        
    def Save(self):
        with open(self.path, "w") as outfile:
            json.dump(self.players, outfile)
    
    def AddPlayerScore(self, playerName : str, score : int):
        if playerName in self.players:
            score = max(score, self.players[playerName]['score'])
            self.players[playerName] = {
                'score' : score,
                'tries' : self.players[playerName]['tries'] + 1,
                'lastTry' : datetime.now().isoformat()
            }
        else:
            self.players[playerName] = {
                'score' : score,
                'tries' : 1,
                'lastTry' : datetime.now().isoformat()
            }
        self.Save()


    def HighScores(self, limit = 10):
        sorted_data = sorted(self.players.items(), key=lambda x: (-x[1]['score'], x[1]['lastTry']), reverse=False)
        return [(p[0], p[1]['score']) for p in sorted_data[:limit]]


