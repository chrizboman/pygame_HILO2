from pygame.math import Vector2
import pytweening
from typing import List, Callable

class Tween:
    tposition : Vector2
    tscale : float
    tvalue : int

    tstartPos : Vector2 | float
    ttargetPos : Vector2 | float

    life : float = 0
    duration : float = 0
    done = True

    on_Start : List[Callable] = []
    on_Update : List[Callable] = []
    on_Complete : List[Callable] = []
    

    def __init__(self, position : Vector2):
        self.tposition = position

    def _TweenUpdate(self, dt):
        self.__onUpdate()
        if not self.done:
            self.life += dt
            if self.life >= self.duration:
                self.done = True
                self.__onComplete()
            # this should work for both Vector2 and float?
            tween_value = self.totalTravel * pytweening.easeInOutQuad(min(1, self.life / self.duration))
            self.tposition = tween_value + self.tstartPos
            return self.tposition
        
    def __onComplete(self):
        for func in self.on_Complete:
            func()
            self.on_Complete.remove(func)
            self.on_Start.clear()
            self.on_Update.clear()

    def __onStart(self):
        for func in self.on_Start:
            func()

    def __onUpdate(self):
        for func in self.on_Update:
            func()
            
    
    def TweenTo(self, pos: Vector2, duration: float = 1):
        try:
            pos = Vector2(pos)
        except:
            raise TypeError('pos must be a Vector2 or a float')
        
        print('moving to pos ', pos)
        self.__onStart()
        self.done = False
        self.tstartPos = self.tposition
        self.duration = duration
        self.totalTravel = pos - self.tstartPos
        self.life = 0
        return self

    def TweenScale(self, scale: float, duration: float = 1):
        self.__onStart()
        self.done = False
        self.tstartPos = self.tposition
        self.ttargetPos = scale
        self.duration = duration
        self.totalTravel = self.ttargetPos - self.tstartPos
        self.life = 0
        return self
    


    
    def OnTweenStart(self, func: Callable):
        self.on_Start.append(func)
        return self
    
    def OnTweenUpdate(self, func: Callable):
        self.on_Update.append(func)
        return self

    def OnTweenComplete(self, func: Callable):
        self.on_Complete.append(func)
        return self