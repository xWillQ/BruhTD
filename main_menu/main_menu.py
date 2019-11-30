import pygame
import os
from game_objects.tower import Tower
from game_objects.enemies import Enemy
from Map.map import Turn
from game_objects.tile import Tile

bg = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/menu/bg.png'))),(1920, 1080))
playBTN = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/menu/button_play.png'))), (200, 200))

table = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/table.png'))), (960, 540))
empty_bt = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/btton_empty.png'))),(100, 100))
num1 = pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/num_1.png'))
rope = pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/rope_big.png'))
close = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/button_close.png')),(60, 60))

class main_menu:

    def __init__(self, condition, win, bg=bg, playBTN=playBTN):
        
        self.win = win
        self.bg = bg
        self.playBTN = playBTN
        self.condition = condition

    def draw(self):

        if self.condition == 0:
            self.win.blit(self.bg, (0, 0))
            self.win.blit(self.playBTN, (565, 275))

        if self.condition == 1:
            self.win.blit(self.bg, (0, 0))
            self.win.blit(table, (350, 175))
            self.win.blit(empty_bt, (415, 250))
            self.win.blit(num1, (450, 270))
            self.win.blit(rope, (450, -225))
            self.win.blit(rope, (890, -225))
            self.win.blit(close, (985, 160))

        #if self.condition == 2:
        
