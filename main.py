import pygame
import Mobs.enemies as enemies
import Map.map as map
from time import time
from logicLoop import logicLoop


pygame.init()
win = pygame.display.set_mode((1280, 720))
mobs = [
    enemies.Enemy(-2, 139, "r", 50, "wizard"),
    enemies.Enemy(-78, 170, "r", 35, "scorpio"),
    enemies.Enemy(-102, 150, "r", 35, "scorpio"),
    enemies.Enemy(-130, 135, "r", 35, "scorpio"),
    enemies.Enemy(-160, 140, "r", 35, "scorpio"),
    enemies.Enemy(-196, 166, "r", 35, "scorpio"),
    enemies.Enemy(-241, 130, "r", 35, "scorpio"),
    enemies.Enemy(-302, 155, "r", 35, "scorpio")
]
path, turns = map.loadMap("rrrddlldrrrrruurrrdddrr", (0, 90), 120, 1)
t1 = time()
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 200):
        t1 = time()
        win.fill((255, 255, 255))
        logicLoop(mobs, turns)

        for i in range(0, len(path)):
            path[i].draw(win)
        for i in range(0, len(turns)):
            turns[i].draw(win)
            #pygame.draw.circle(win, (255, 0, 0), (turns[i].circleX, turns[i].circleY), turns[i].radius, 1)
        for i in range(0, len(mobs)):
            mobs[i].draw(win)

        pygame.display.flip()
