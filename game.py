import pygame
import os
from Map.map import Turn
from Mobs.enemies import Enemy
from GUI.main_menu import main_menu
from Map.tower import Tower
from Map.level import Level
from GUI.button import Button
from GUI.button import isInside
from Map.level import Level
from Map.tile import Tile

def draw(condition, number, wave_trigger):
    if condition <= 9:

        menu = main_menu(condition, win)
        menu.draw()

    if condition >= 10:

        level = Level(win, number, pygame.mouse.get_pos(), wave_trigger)
        level.draw()


pygame.init()
win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
condition = 0
number = 0
run = True
wave_trigger = True

while run:

    pygame.time.delay(0)

    #print(pygame.mouse.get_pos())
    #print(condition)
    for event in pygame.event.get():

        if event.type is pygame.QUIT:
            run = False

        if event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if condition == 0:
                if mouse_pos[1] <= 635 and mouse_pos[0] >= 840 and mouse_pos[1] >= 435 and mouse_pos[0] <= 1040:
                    condition = 1
            if condition == 1:
                if mouse_pos[1] <= 230 and mouse_pos[0] >= 1580 and mouse_pos[1] >= 150 and mouse_pos[0] <= 1640:
                    condition = 0
                if mouse_pos[1] <= 350 and mouse_pos[0] >= 420 and mouse_pos[1] >= 250 and mouse_pos[0] <= 510:
                    number = 1
                    condition = 10
            if condition == 10:
                if isInside(mouse_pos[0] - 20, mouse_pos[1] - 20, 15, 325, 40) == True:
                    wave_trigger = False


    draw(condition, number, wave_trigger)
    pygame.display.flip()