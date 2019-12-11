import pygame
from Map import level1
# from Map import level2
from GUI import main_menu
import G
from time import time


for event in pygame.event.get():
    G.event_N = event
    G.event = event

pygame.init()
run = True
t1 = time()
pygame.display.set_caption("BruhTD")

while run:

    # print(pygame.mouse.get_pos())
    # print(G.condition)
    for event in pygame.event.get():
        G.event = event
        if event.type is pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 60):
        t1 = time()

        if G.condition <= 9:
            main_menu.draw()

        if G.condition >= 10:
            if G.level_number == 1:
                level1.draw()
            # if G.level_number == 2:
                # level2.draw()

    pygame.display.update()
