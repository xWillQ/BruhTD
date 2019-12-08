import pygame
import os
from Map.map import loadLevel
from GUI.button import Button
import Mobs.enemies as enemies
from Map.tower import Tower as Tower

towers = [Tower(680, 300, 120), Tower(1090, 400, 120)]

death_button = Button(15, 325, 40, pygame.image.load(os.path.join('Assets/GUI/interface_game/skull.png')))
lvl1 = ["rrdurduurrrr"]
turns, background, start, Idirection = loadLevel(lvl1, (0, 250), towers, 0.7, "forest", 1920, 1080)

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

bg = background
tower_place = pygame.transform.scale(pygame.image.load(os.path.join('Assets/tiles/forest/22.png')), (180, 180))


def draw(self, win):

    win.blit(bg, (0, 0))
    if globals.level_number == 1:

        if globals.wave_trigger is True:
            death_button.draw(win)
