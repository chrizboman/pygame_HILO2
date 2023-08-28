class NameEditor():
    maxChars = 20
    playerName = ''
    __asGuest = True
    
    def __init__(self) -> None:
        self.playerName = 'Guest'
        
    
    def InputChar(self, char: str):
        if self.__asGuest:
            self.__Empty()
            self.__asGuest = False
        
        if char == 'space':
            self.__Add(' ')
        elif char == 'backspace':
            self.__Remove()
        else:
            self.__Add(char.upper())

    
    def __Remove(self):
        self.playerName = self.playerName[:-1]
    
    def __Add(self, char):
        if len(self.playerName) < self.maxChars:
            self.playerName += char
    
    def __Empty(self):
        self.playerName = ''