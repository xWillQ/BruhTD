import pygame
import os

bg = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/menu/bg.png'))), (1920, 1080))
playBTN = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/menu/button_play.png'))), (200, 200))

table = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/levels/table.png'))), (1360, 740))
empty_bt = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/levels/btton_empty.png'))), (100, 100))
num1 = pygame.image.load(os.path.join('Assets/GUI/levels/num_1.png'))
rope = pygame.image.load(os.path.join('Assets/GUI/settings/rope_big.png'))
close = pygame.transform.scale(pygame.image.load(os.path.join('Assets/GUI/settings/button_close.png')), (80, 80))


class main_menu:

    def __init__(self, condition, win, bg=bg, playBTN=playBTN):

        self.win = win
        self.bg = bg
        self.playBTN = playBTN
        self.condition = condition

    def draw(self):

        if self.condition == 0:
            self.win.blit(self.bg, (0, 0))
            self.win.blit(self.playBTN, (840, 435))

        if self.condition == 1:
            self.win.blit(self.bg, (0, 0))
            self.win.blit(table, (300, 175))
            self.win.blit(empty_bt, (415, 250))
            self.win.blit(num1, (450, 270))
            self.win.blit(rope, (450, -225))
            self.win.blit(rope, (1470, -225))
            self.win.blit(close, (1580, 150))
