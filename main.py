import pygame
import Mobs.enemies as enemies
import Map.map as map
from time import time
from logicLoop import logicLoop


pygame.init()
win = pygame.display.set_mode((1280, 720))
mobs = [enemies.Enemy(0, 170, 50, "Assets/Mobs/1/1_enemies_1_walk_000.png", "goblin")]
mobs[0].direction = "r"
path, turns = map.loadMap("rrrddlldrrrrruurrrdddrr", (0, 100), 120, 1)
t1 = time()
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 100):
        t1 = time()
        win.fill((255, 255, 255))
        logicLoop(mobs, turns)

        for i in range(0, len(path)):
            path[i].draw(win)
        for i in range(0, len(turns)):
            turns[i].draw(win)
            pygame.draw.circle(win, (255, 0, 0), (turns[i].circleX, turns[i].circleY), turns[i].radius, 1)
        for i in range(0, len(mobs)):
            mobs[i].draw(win)

        pygame.display.flip()