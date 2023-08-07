import tween
from typing import Callable

class Animation():
    onComplete = []
    onUpdate = []
    onStart = []

    tweenObject = "not stared"

    def __init__(self, Object, toPos = None, toTextValue = None, toScale : float = None, duration = 1.0, delay = 0.0, easeType = "linear", onComplete : Callable = lambda:(), onUpdate : Callable = lambda:(), onStart : Callable = lambda:()) -> None:
        self.object = Object
        self.easeType = easeType
        self.toPos = toPos
        self.totextNum = toTextValue
        self.toScale = toScale
        self.duration = duration
        self.delay = delay
        self.onComplete.append(onComplete)
        self.onUpdate.append(onUpdate)
        self.onStart.append(onStart)

        if self.toPos is not None:
            self.key = 'position'
            self.val = self.toPos
        elif self.totextNum is not None:
            self.key = 'text'
            self.val = self.totextNum
        elif self.toScale is not None:
            self.key = 'scale'
            self.val = self.toScale
        else:
            raise Exception("No animation value given", 'type is', type(self.toPos))

    def Start(self):
        for func in self.onStart:
            func()
        self.tweenObject = tween.to(self.object, self.key, self.val, self.duration, ease_type = self.easeType, delay=self.delay)
        for func in self.onUpdate:
            self.tweenObject.on_update(func)
        for func in self.onComplete:
            self.tweenObject.on_complete(func)
        return self
    
    def OnStart(self, func : Callable):
        self.onStart.append(func)
        return self