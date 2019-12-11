import pygame
from Map import level
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
    if (t2 - t1 >= 1 / 144):
        t1 = time()

        if G.condition <= 9:
            main_menu.draw()

        if G.condition >= 10:
            level.draw()

    pygame.display.update()
