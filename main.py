import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy
from laser import Laser

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

# create player
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

# enemies
enemies = pygame.sprite.Group()
for i in range(5):
    enemies.add(Enemy())

# lasers
lasers = pygame.sprite.Group()

font = pygame.font.SysFont(None, 36)

score = 0
running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                laser = Laser(player.rect.centerx, player.rect.top)
                lasers.add(laser)

    # update objects
    player_group.update()
    enemies.update()
    lasers.update()

    # collision
    hits = pygame.sprite.groupcollide(enemies, lasers, True, True)

    for hit in hits:
        score += 10
        enemies.add(Enemy())

    # draw screen
    screen.fill((20,20,40))

    player_group.draw(screen)
    enemies.draw(screen)
    lasers.draw(screen)

    score_text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_text, (10,10))

    pygame.display.update()

pygame.quit()
sys.exit()