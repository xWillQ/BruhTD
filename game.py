import pygame
from Map import level
from GUI import main_menu
import G

for event in pygame.event.get():
    G.event_N = event
    G.event = event


def draw():

    if G.condition <= 9:

        main_menu.draw(G.win)

    if G.condition >= 10:

        level.draw(G.win)


pygame.init()
run = True

while run:

    pygame.time.delay(0)
    # print(pygame.mouse.get_pos())
    # print(G.condition)
    for event in pygame.event.get():
        G.event = event
        if event.type is pygame.QUIT:
            run = False

    draw()
    pygame.display.update()
