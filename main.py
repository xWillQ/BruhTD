import pygame
from Enemies.enemies import Enemy
from Map.map import Turn
from Map.tower import Tower
from time import time
from logicLoop import logicLoop


pygame.init()
mobs = []   # Массив с мобами
turns = []  # Массив с поворотами
towers = [] # Массив с башнями
t1 = time()
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 0.1):
        t1 = time()

        logicLoop(mobs, towers, turns)

        for mob in mobs:
            mob.draw()
        for turn in turns:
            turn.draw()
        for tower in towers:
            tower.draw()

        pygame.display.flip()
