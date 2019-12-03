import pygame
import os
from game_objects.tile import Tile
from Map.map import loadMap

bg_tile = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/42.png')), (120, 120))

lvl1 = ["r", "r", "u", "r", "r"]

class Level():
    def __init__(self, win, number):

        self.win = win
        self.number = number

    def draw(self):

        for y in range (0,9):
            for x in range (0,16):
                tile = Tile(self.win, bg_tile, x * 120, y * 120)
                tile.draw()

        path, turns = loadMap(lvl1, (0, 600), 120, 1)

        for i in range (0,len(path)):
            route = path[i]
            route.draw(self.win)

        for i in range(0, len(turns)):
            kek = turns[i]
            kek.draw(self.win)
