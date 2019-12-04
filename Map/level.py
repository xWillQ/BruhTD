import pygame
import os
from Map.tile import Tile
from Map.map import loadMap
from GUI.button import Button

bg_tile = pygame.transform.scale(pygame.image.load(os.path.join('Assets/tiles/forest/42.png')), (120, 120))
death_button = Button(15, 325, 40, pygame.image.load(os.path.join('Assets/GUI/interface_game/skull.png')))
lvl1 = ["r", "r", "u", "r", "r", "d", "d", "r", "r", "r", "d", "d", "r", "r", "r"]


class Level():
    def __init__(self, win, number, mpos, WT):

        self.path, self.turns = loadMap(lvl1, (0, 250), 200, 1)
        self.win = win
        self.number = number
        self.Mpos = mpos
        self.wave_trigger = WT

    def draw(self):

        if self.number == 1:
            for y in range(0, 9):
                for x in range(0, 16):
                    Tile(self.win, bg_tile, x * 120, y * 120).draw()

            for i in range(0, len(self.path)):
                self.path[i].draw(self.win)

            for i in range(0, len(self.turns)):
                self.turns[i].draw(self.win)
            
            if self.wave_trigger == True:
                death_button.draw(self.win)
