import pygame
import os
from game_objects.tile import Tile

bg_tile = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/42.png')), (100, 100))
turn_p = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/1.png' )), (150, 150))
st_p = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/6.png')), (150, 150))
tower_pl = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/22.png')), (250, 250))

#lvl1 = [line1[], line2[], line3[], line4[], line5[], line6[], line7[], line8[], line9[]]

class Level():
    def __init__(self, win, number):

        self.win = win
        self.number = number
        #self.map = Map

    def draw(self):
        
        for y in range (0,9):
            for x in range (0,16):
                tile = Tile(self.win, bg_tile, x * 120, y * 120)
                tile.draw()
        #for y in range lvl1:
            #for x in range lvl1:
                #tile = Tile(self.win, lvl1[x][y], x * 100, y * 100)
                #tile.draw()
