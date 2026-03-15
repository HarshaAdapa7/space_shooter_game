import pygame
from settings import *

class Laser(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface((5,20))
        self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):

        self.rect.y -= LASER_SPEED

        if self.rect.bottom < 0:
            self.kill()