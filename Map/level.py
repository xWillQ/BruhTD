import pygame
import os
from Map.map import loadLevel
from GUI.button import Button
from GUI.button import isInside
import Mobs.enemies as enemies
from Map.tower import Tower as Tower
import G

towers = [Tower(680, 300), Tower(1090, 400)]

death_button = Button(15, 325, 40, pygame.image.load(os.path.join('Assets/GUI/interface_game/skull.png')))
lvl1 = "rurddrruurrddrr"
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
                if isInside(mouse_pos[0] - 20, mouse_pos[1] - 20, 15, 325, 40) is True:
                    G.wave_trigger = True
        if G.wave_trigger is False:
            death_button.draw(win)
