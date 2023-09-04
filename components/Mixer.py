import pygame.mixer as mixer


class Mixer:

    def __init__(self):
        mixer.init()
        self.correct = mixer.Sound('assets/sounds/bell.wav')
        self.wrong = mixer.Sound('assets/sounds/failure.wav')
        self.gameOver = mixer.Sound('assets/sounds/gameOver.mp3')
        self.click = mixer.Sound('assets/sounds/click.mp3')
        self.start = mixer.Sound('assets/sounds/explosion.wav')
        self.ticking = mixer.Sound('assets/sounds/ticking.mp3')

        self.allSounds = [self.correct, self.wrong, self.gameOver, self.click, self.start, self.ticking]

    def PlayMusic(self, music : str):
        self.playing = music
        if music == 'menu':
            mixer.music.load('assets/music/menu.mp3')
            mixer.music.play(-1)
        elif music == 'playing':
            mixer.music.load('assets/music/play.mp3')
            mixer.music.play(-1)
        elif music == 'ticking':
            mixer.music.load('assets/music/ticking.mp3')
            mixer.music.play()

    def PlaySound(self, sound : str):
        if sound == 'correct':
            self.correct.play()
        elif sound == 'wrong':
            self.wrong.play()
        elif sound == 'gameOver':
            self.gameOver.play()
        elif sound == 'click':
            self.click.play()
        elif sound == 'start':
            self.start.play()
        elif sound == 'ticking':
            self.ticking.play()
                                 
    def Stop(self):
        mixer.music.fadeout(1000)
    
    def StopMusic(self):
        mixer.music.stop()
    
    def Volume(self, volume : float):
        mixer.music.set_volume(volume)
        [mixer.Sound.set_volume(sound, volume) for sound in self.allSounds]