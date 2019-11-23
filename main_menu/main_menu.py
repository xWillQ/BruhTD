import pygame
import os

table = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/table.png'))), (684, 360))
empty_bt = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/btton_empty.png'))), (100, 100))

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
            self.win.blit(empty_bt, (375, 200))

        pygame.display.update()

