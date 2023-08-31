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

    def FormatWhenDone(self):
        if self.playerName == '':
            self.playerName = 'Guest'
        #remove spaces at the end and beginning
        self.playerName = self.playerName.strip()
        self.playerName = self.playerName.replace(' ', '·')
        
        return self.playerName

    
    def __Remove(self):
        self.playerName = self.playerName[:-1]
    
    def __Add(self, char):
        if len(self.playerName) < self.maxChars:
            self.playerName += char
    
    def __Empty(self):
        self.playerName = ''