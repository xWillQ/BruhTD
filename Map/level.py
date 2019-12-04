import pygame
import os
from Map.tile import Tile
from Map.map import loadMap

bg_tile = pygame.transform.scale(pygame.image.load(os.path.join('Assets/tiles/forest/42.png')), (120, 120))
lvl1 = ["r", "r", "u", "r", "r", "d", "d", "r", "r", "r", "d", "d", "r", "r", "r"]


class Level():
    def __init__(self, win, number):

        self.path, self.turns = loadMap(lvl1, (0, 250), 200, 1)
        self.win = win
        self.number = number

    def draw(self):

        if self.number == 1:
            for y in range(0, 9):
                for x in range(0, 16):
                    Tile(self.win, bg_tile, x * 120, y * 120).draw()

            for i in range(0, len(self.path)):
                self.path[i].draw(self.win)

            for i in range(0, len(self.turns)):
                self.turns[i].draw(self.win)
            
            
