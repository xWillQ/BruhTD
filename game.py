import pygame
import os
from Map.map import Turn
from game_objects.enemies import Enemy
from main_menu.main_menu import main_menu
from game_objects.tower import Tower
from levels.level import Level

def draw(condition, number):
    if condition <= 9:

        menu = main_menu(condition, win)
        menu.draw()

    if condition >= 10:

        level = Level(win, number)
        level.draw()



pygame.init()
win = pygame.display.set_mode((1920, 1080))  #pygame.FULLSCREEN)
condition = 0
number = 0
run = True

while run:

    pygame.time.delay(20)
    print(pygame.mouse.get_pos())
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

    draw(condition, number)
    pygame.display.update()