import pygame
import Mobs.enemies as enemies
import Map.map as map
from time import time
import functions


width = 1280
height = 720
pygame.init()
win = pygame.display.set_mode((width, height))
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
turns = map.loadMap("rrrddlldrrdruuurrrdddrr", (0, 90), 120, "forest", width, height)
background = pygame.image.load("Map/temp.png")
t1 = time()
run = True
win.blit(background, (0, 0))
pygame.display.update()
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 60):
        t1 = time()
        functions.logicLoop(mobs, turns)
        updates = functions.clear(mobs, win, background)
        for mob in mobs:
            mob.draw(win)
        
        pygame.display.update(updates)
