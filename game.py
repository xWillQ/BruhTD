import pygame
import os
from Map.map import Turn
from Enemies.enemies import Enemy
from GUI.main_menu import main_menu
from Map.tower import Tower
from Map.level import Level
from GUI.button import Button
from GUI.button import isInside
from Map.level import Level


def draw(condition, number, wave_trigger):
    if condition <= 9:

        menu = main_menu(condition, win)
        menu.draw()

    if condition >= 10:

        level = Level(win, number, pygame.mouse.get_pos(), wave_trigger)
        level.draw()


pygame.init()
win = pygame.display.set_mode((1120, 1080))  # pygame.FULLSCREEN)
condition = 0
number = 0
run = True
wave_trigger = True

while run:

    pygame.time.delay(200)
    
    #print(pygame.mouse.get_pos())
    #print(condition)
    for event in pygame.event.get():

        if event.type is pygame.QUIT:
            run = False

        if event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if condition == 0:
                if mouse_pos[1] <= 475 and mouse_pos[0] >= 565 and mouse_pos[1] >= 275 and mouse_pos[0] <= 765:
                    condition = 1
            if condition == 1:
                if mouse_pos[1] <= 210 and mouse_pos[0] >= 985 and mouse_pos[1] >= 160 and mouse_pos[0] <= 1035:
                    condition = 0
                if mouse_pos[1] <= 350 and mouse_pos[0] >= 420 and mouse_pos[1] >= 250 and mouse_pos[0] <= 510:
                    number = 1
                    condition = 10
            if condition == 10:
                if isInside(mouse_pos[0], mouse_pos[1], 15, 325, 40) == True:
                    wave_trigger = False

    draw(condition, number, wave_trigger)
    pygame.display.update()