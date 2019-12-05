import pygame
import os
from Map.tile import Tile
from Map.map import loadMap
from GUI.button import Button
import Mobs.enemies as enemies
import random

death_button = Button(15, 325, 40, pygame.image.load(os.path.join('Assets/GUI/interface_game/skull.png')))
lvl1 = ["r", "r", "u", "r", "r", "d", "d", "r", "r", "r", "d", "d", "r", "r", "r"]
path, turns = loadMap(lvl1, (0, 250), 200, 1)

scorpio_anim = [
    'Assets/mobs/1/1_enemies_1_walk_000.png',
    'Assets/mobs/1/1_enemies_1_walk_001.png',
    'Assets/mobs/1/1_enemies_1_walk_002.png',
    'Assets/mobs/1/1_enemies_1_walk_003.png',
    'Assets/mobs/1/1_enemies_1_walk_004.png',
    'Assets/mobs/1/1_enemies_1_walk_005.png',
    'Assets/mobs/1/1_enemies_1_walk_006.png',
    'Assets/mobs/1/1_enemies_1_walk_007.png',
    'Assets/mobs/1/1_enemies_1_walk_008.png',
    'Assets/mobs/1/1_enemies_1_walk_009.png',
    'Assets/mobs/1/1_enemies_1_walk_010.png',
    'Assets/mobs/1/1_enemies_1_walk_011.png',
    'Assets/mobs/1/1_enemies_1_walk_012.png',
    'Assets/mobs/1/1_enemies_1_walk_013.png',
    'Assets/mobs/1/1_enemies_1_walk_014.png',
    'Assets/mobs/1/1_enemies_1_walk_015.png',
    'Assets/mobs/1/1_enemies_1_walk_016.png',
    'Assets/mobs/1/1_enemies_1_walk_017.png',
    'Assets/mobs/1/1_enemies_1_walk_018.png',
    'Assets/mobs/1/1_enemies_1_walk_018.png'
]

mobs = [
    enemies.Enemy(-40, 360, 60, scorpio_anim, "goblin"),
    enemies.Enemy(-100, 360, 60, scorpio_anim, "goblin"),
    enemies.Enemy(-160, 360, 60, scorpio_anim, "goblin"),
]
for i in range (0,len(mobs)):
    mobs[i].direction = "r"
    mobs[i].anim_c += i*2 + 3

bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets/bg_forest.png')), (1920, 1080))


class Level():
    def __init__(self, win, number, mpos, WT, path = path, turns = turns):

        self.path = path
        self.turns = turns
        self.win = win
        self.number = number
        self.Mpos = mpos
        self.wave_trigger = WT

    def draw(self):

        self.win.blit(bg, (0, 0))
        if self.number == 1:

            for i in range(0, len(self.path)):
                self.path[i].draw(self.win)

            for i in range(0, len(self.turns)):
                self.turns[i].draw(self.win)

            if self.wave_trigger == True:
                death_button.draw(self.win)

            if self.wave_trigger == False:
                for i in range(0, len(mobs)):
                    turned = False
                    for turn in self.turns:
                        if (turn.isInside(mobs[i].x, mobs[i].y)):
                            mobs[i].turn(turn)
                            turned = True
                    if (not turned):
                        mobs[i].move()

                    if ((i > 0) and (mobs[i - 1].distance > mobs[i].distance)):
                        t = mobs[i - 1]
                        mobs[i - 1] = mobs[i]
                        mobs[i] = t


                for i in range(0, len(mobs)):
                    mobs[i].draw(self.win)
