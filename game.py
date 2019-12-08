import pygame
from Map import level
from GUI import main_menu
from GUI.button import isInside
import globals

for event in pygame.event.get():
    globals.G_event = event


def draw():

    if globals.condition <= 9:

        main_menu.draw(globals.win)

    if globals.condition >= 10:

        level.draw(globals.win)


pygame.init()
run = True

while run:

    pygame.time.delay(10)

    # print(pygame.mouse.get_pos())
    # print(globals.condition)
    for event in pygame.event.get():
        globals.G_event = event
        if event.type is pygame.QUIT:
            run = False

        if event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            if globals.condition == 10:
                if isInside(mouse_pos[0] - 20, mouse_pos[1] - 20, 15, 325, 40) is True:
                    globals.wave_trigger = False

        globals.G_event = event

    draw()
    pygame.display.update()
