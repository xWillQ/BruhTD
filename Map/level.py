import pygame
import os
from Map.map import loadLevel
from GUI.button import Button
from GUI.button import isInside
import Mobs.enemies as enemies
from Map.tower import Tower as Tower
import Map.tower as tower
# import level_func
import G

tower.loadTypes(0.75 * 0.8, 'forest')

towers = [Tower(470, 300), Tower(865, 410), Tower(1250, 300), Tower(1600, 410), Tower(1650, 660), Tower(1650, 800)]

death_button = Button(15, 325, 40, pygame.image.load(os.path.join('Assets/GUI/interface_game/skull.png')))
lvl1 = "rurrddrruurrddrrddllllllldd"
turns, background, start, Idirection = loadLevel(lvl1, (0, 250), towers, 0.75, "forest", 1920, 1080)

scorpio_anim = [
    'Assets/Mobs/scorpio/walk_000.png', 'Assets/Mobs/scorpio/walk_001.png', 'Assets/Mobs/scorpio/walk_002.png', 'Assets/Mobs/scorpio/walk_003.png', 'Assets/Mobs/scorpio/walk_004.png',
    'Assets/Mobs/scorpio/walk_005.png', 'Assets/Mobs/scorpio/walk_006.png', 'Assets/Mobs/scorpio/walk_007.png', 'Assets/Mobs/scorpio/walk_008.png', 'Assets/Mobs/scorpio/walk_009.png',
    'Assets/Mobs/scorpio/walk_010.png', 'Assets/Mobs/scorpio/walk_011.png', 'Assets/Mobs/scorpio/walk_012.png', 'Assets/Mobs/scorpio/walk_013.png', 'Assets/Mobs/scorpio/walk_014.png',
    'Assets/Mobs/scorpio/walk_015.png', 'Assets/Mobs/scorpio/walk_016.png', 'Assets/Mobs/scorpio/walk_017.png', 'Assets/Mobs/scorpio/walk_018.png', 'Assets/Mobs/scorpio/walk_018.png'
]

Mobs = [
    enemies.Enemy(-40, 360, "r", "scorpio"),
    enemies.Enemy(-100, 360, "r", "scorpio"),
    enemies.Enemy(-160, 360, "r", "scorpio"),
]
G.wave_trigger = False


def draw(win):

    if G.level_number == 1:

        win.blit(background, (0, 0))
        if G.event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if G.condition == 10:
                if isInside(mouse_pos[0], mouse_pos[1], 15 + 20, 325 + 20, 50) is True:
                    G.wave_trigger = True
        if G.wave_trigger is False:
            death_button.draw(win)

        if G.event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(towers)):
                if isInside(mouse_pos[0], mouse_pos[1], towers[i].x, towers[i].y, 120):
                    if towers[i].level == 0:
                        towers[i].gui_opened = True
                        Tower.gui_close(towers, i)
                if towers[i].gui_opened:
                    Tower.gui_type_change(towers[i], mouse_pos)

        for i in range(len(towers)):
            if towers[i].level != 0:
                towers[i].draw(G.win, 'forest')
            if towers[i].level == 0 and towers[i].gui_opened is True:
                Tower.draw_gui(towers[i])

    G.event = G.event_N
