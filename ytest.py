import pytweening

import pygame
from pygame.math import Vector2 
from GameObjects import GameObject, Text
import random



pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

def AnimateTo(pos : Vector2, duration:float = 1.0 ):

    pass




class Tween:
    position : Vector2
    startPos : Vector2
    targetPos : Vector2
    life : float = 0
    duration : float = 0
    moving = False

    def __init__(self, position : Vector2):
        self.position = position

    def _update(self, dt):
        if self.moving:
            self.life += dt
            tween_value = self.distanceVector * pytweening.easeInOutQuad(min(1, self.life / self.duration))
            if self.life >= self.duration:
                moving = False
            self.position = tween_value + self.startPos
            anim_pos = tween_value + self.startPos
            # print('anim_pos ', anim_pos)
            return anim_pos
    
    def To(self, pos: Vector2, duration: float):
        print('moving to pos ', pos)
        self.moving = True
        self.startPos = self.position
        self.targetPos = pos
        self.duration = duration
        self.distanceVector = self.targetPos - self.startPos
        self.life = 0

    

class Object:
    position : Vector2 = Vector2(random.randint(0,500), random.randint(0,500))
    tween : Tween = Tween(position)
    
    def Draw(self):
        self.position = Vector2(self.tween.position)
        pygame.draw.circle(screen, (255, 0, 0), self.position,  5)
    
    def TweenTo(self, pos : Vector2, duration : float):
        self.tween.To(pos, duration)
    


# tween = Tweener( Vector2(100, 100), 3.0)
object = Object()

while True:
    clock.tick(60)
    dt = clock.tick(60)/1000

    object.tween._update(dt)


    screen.fill((0, 0, 0))

    object.Draw()
    
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                AnimateTo(pygame.mouse.get_pos())
                print('space')
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_e:
                print('e')
                object.TweenTo(pygame.mouse.get_pos(), 1.0)

                


