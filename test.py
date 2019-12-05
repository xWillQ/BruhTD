import pygame
import os

from Enemies.enemies import Enemy
from Map.map import Turn
win = pygame.display.set_mode((1368, 720))
mob_ass = pygame.image.load(os.path.join('game_assets/2d-monster-sprites/PNG/1/1_enemies_1_attack_000.png'))
mob = Enemy(150, 150, 60, mob_ass)

run = True
while run:
    print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    mob.draw(win)

    pygame.display.flip()