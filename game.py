import pygame
from Map import level
# from Map import level2
from GUI import main_menu
import G
from time import time
from level_initiator import level_init

for event in pygame.event.get():
    G.event_N = event
    G.event = event

pygame.init()
run = True
t1 = time()
pygame.display.set_caption("BruhTD")

while run:

    print(pygame.mouse.get_pos())
    # print(G.condition)
    for event in pygame.event.get():
        G.event = event
        if event.type is pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 75):
        t1 = time()

        if G.condition <= 9:
            main_menu.draw()

        if G.condition >= 10:
            if G.level_number != 0 and G.online is False:
                turns, background, start, Idirection, mobs, player, towers, deco_bg = level_init(G.level_number)
                G.online = True
            level.draw(turns, background, start, Idirection, mobs, player, towers)

    pygame.display.update()
