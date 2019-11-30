import pygame
import os
from .Mapi.tower import Tower
from .Enemies.enemies import Enemy
from .Mapi.map import Turn
form .levels.lvl1 import lvl1


table = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/table.png'))), (684, 360))
empty_bt = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/btton_empty.png'))), (100, 100))
num1 = pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/num_1.png'))
rope = pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/rope_big.png'))
close = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/button_close.png')), (60, 60))
bg_tile = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/42.png')), (100, 100))
turn_p = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/1.png')), (150, 150))
st_p = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/6.png')), (150, 150))
tower_pl = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/22.png')), (250, 250))
mob1 = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/2d-monster-sprites/PNG/1/1_enemies_1_attack_000.png')), (60, 60))
tower_archer = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/archer-tower-game-assets/PNG/8.png')), (90, 90))



class main_menu:

    def __init__(self, win, bg, playBTN, condition):
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

        if self.condition == 2:

        pygame.display.update()
