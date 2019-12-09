import pygame
from Map import level
from GUI import main_menu
from GUI.button import isInside
import G

for event in pygame.event.get():
    G.event = event


def draw():

    if G.condition <= 9:

        main_menu.draw(G.win)

    if G.condition >= 10:

        level.draw(G.win)


pygame.init()
run = True

while run:

    pygame.time.delay(10)

    # print(pygame.mouse.get_pos())
    # print(G.condition)
    for event in pygame.event.get():
        G.event = event
        if event.type is pygame.QUIT:
            run = False

        if event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            if G.condition == 10:
                if isInside(mouse_pos[0] - 20, mouse_pos[1] - 20, 15, 325, 40) is True:
                    G.wave_trigger = False

        G.event = event

    draw()
    pygame.display.update()
