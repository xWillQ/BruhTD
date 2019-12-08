import pygame
from Map.level import Level
from GUI.main_menu import main_menu
from GUI.button import isInside
import globals


def draw():

    if globals.condition <= 9:

        menu = main_menu(globals.condition, globals.win)
        menu.draw()

    if globals.condition >= 10:

        level = Level(globals.win, globals.number, pygame.mouse.get_pos(), globals.wave_trigger)
        level.draw(tower_placed, tower1_placed)


pygame.init()
globals.condition = 0
globals.number = 0
run = True
globals.wave_trigger = True
tower_placed = False
tower1_placed = False

while run:

    pygame.time.delay(0)

    # print(pygame.mouse.get_pos())
    # print(globals.condition)
    for event in pygame.event.get():

        if event.type is pygame.QUIT:
            run = False

        if event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if globals.condition == 0:
                if mouse_pos[1] <= 635 and mouse_pos[0] >= 840 and mouse_pos[1] >= 435 and mouse_pos[0] <= 1040:
                    globals.condition = 1
            if globals.condition == 1:
                if mouse_pos[1] <= 230 and mouse_pos[0] >= 1580 and mouse_pos[1] >= 150 and mouse_pos[0] <= 1640:
                    globals.condition = 0
                if mouse_pos[1] <= 350 and mouse_pos[0] >= 420 and mouse_pos[1] >= 250 and mouse_pos[0] <= 510:
                    number = 1
                    globals.condition = 10
            if globals.condition == 10:
                if isInside(mouse_pos[0] - 20, mouse_pos[1] - 20, 15, 325, 40) is True:
                    globals.wave_trigger = False
                if number == 1:
                    if isInside(mouse_pos[0], mouse_pos[1], 680, 300, 120):
                        tower_placed = True
                    if isInside(mouse_pos[0], mouse_pos[1], 1090, 400, 120):
                        tower1_placed = True

    draw()
    pygame.display.flip()