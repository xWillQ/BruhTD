import pygame
import os

table = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/table.png'))), (684, 360))
empty_bt = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/btton_empty.png'))), (100, 100))
num1 = pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/num_1.png'))
rope = pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/rope_big.png'))
close = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/button_close.png')), (60, 60))
bg_tile = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/42.png')), (100, 100))
turn = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/1.png')), (150, 150))
st_p = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/6.png')), (150, 150))
tower_pl = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/22.png')), (250, 250))

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
            for i in range (0,8):
                for k in range (0,14):
                    self.win.blit(bg_tile, (k * 100, i * 100))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (0, 150))
            self.win.blit(pygame.transform.rotate(st_p,(90)), (150, 150))
            self.win.blit(pygame.transform.rotate(turn, (180)), (300, 150))
            self.win.blit(pygame.transform.rotate(turn, (0)), (300, 0))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (450, 0))
            self.win.blit(pygame.transform.rotate(st_p, (0)), (600, 150))
            self.win.blit(pygame.transform.rotate(st_p, (0)), (600, 300))
            self.win.blit(pygame.transform.rotate(turn, (270)), (600, 0))
            self.win.blit(pygame.transform.rotate(turn, (90)), (600, 450))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (750, 450))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (900, 450))
            self.win.blit(pygame.transform.rotate(turn, (270)), (1050, 450))
            self.win.blit(pygame.transform.rotate(st_p, (0)), (1050, 600))
            self.win.blit(tower_pl, (395, 75))
            self.win.blit(tower_pl, (700, 285))

        pygame.display.update()
