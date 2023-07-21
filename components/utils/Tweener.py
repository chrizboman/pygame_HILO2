from pygame.math import Vector2
import pytweening
from typing import List, Callable

class Tween:
    tposition : Vector2
    tstartPos : Vector2
    ttargetPos : Vector2
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
            # print('life ', self.life, ' duration ', self.duration, 'is higher ', self.life >= self.duration  )
            if self.life >= self.duration:
                self.done = True
                self.__onComplete()
            tween_value = self.distanceVector * pytweening.easeInOutQuad(min(1, self.life / self.duration))
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
            
    
    def TweenTo(self, pos: Vector2 = None, duration: float = 1, scale : float = None, number : float = None):
        
        # animate scale
        if scale is not None:
            self.__onStart()
            pass

        # animate number
        elif number is not None:
            self.__onStart()
            pass

        # animate position, x,y or Vector2
        elif pos is not None:
            try:
                pos = Vector2(pos)
            except:
                raise Exception('TweenTo: invalid pos arguments')
            
            print('moving to pos ', pos)
            self.__onStart()
            self.done = False
            self.tstartPos = self.tposition
            self.ttargetPos = pos
            self.duration = duration
            if type(pos) == float:
                self.ttargetPos = Vector2(pos, pos)
            self.distanceVector = Vector2(self.ttargetPos) - Vector2(self.tstartPos)
            self.life = 0
            return self
        else:
            raise Exception('TweenTo: invalid arguments')
    


    
    def OnTweenStart(self, func: Callable):
        self.on_Start.append(func)
        return self
    
    def OnTweenUpdate(self, func: Callable):
        self.on_Update.append(func)
        return self

    def OnTweenComplete(self, func: Callable):
        self.on_Complete.append(func)
        return self