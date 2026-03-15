import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50,50))
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-50)
        self.rect.y = random.randint(-100,-40)

        self.speed = ENEMY_SPEED

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-100,-40)
            self.rect.x = random.randint(0,WIDTH-50)