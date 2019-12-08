import pygame
import os
import globals

bg = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/menu/bg.png'))), (1920, 1080))
playBTN = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/menu/button_play.png'))), (200, 200))

table = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/levels/table.png'))), (1360, 740))
empty_bt = pygame.transform.scale((pygame.image.load(os.path.join('Assets/GUI/levels/btton_empty.png'))), (100, 100))
num1 = pygame.image.load(os.path.join('Assets/GUI/levels/num_1.png'))
rope = pygame.image.load(os.path.join('Assets/GUI/settings/rope_big.png'))
close = pygame.transform.scale(pygame.image.load(os.path.join('Assets/GUI/settings/button_close.png')), (80, 80))


def draw(win):

    event = globals.G_event

    if globals.condition == 0:
        if event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[1] <= 635 and mouse_pos[0] >= 840 and mouse_pos[1] >= 435 and mouse_pos[0] <= 1040:
                globals.condition = 1
        win.blit(bg, (0, 0))
        win.blit(playBTN, (840, 435))

    if globals.condition == 1:
        if event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[1] <= 230 and mouse_pos[0] >= 1580 and mouse_pos[1] >= 150 and mouse_pos[0] <= 1640:
                globals.condition = 0
                if mouse_pos[1] <= 350 and mouse_pos[0] >= 420 and mouse_pos[1] >= 250 and mouse_pos[0] <= 510:
                    globals.level_number = 1
                    globals.condition = 10
        win.blit(bg, (0, 0))
        win.blit(table, (300, 175))
        win.blit(empty_bt, (415, 250))
        win.blit(num1, (450, 270))
        win.blit(rope, (450, -225))
        win.blit(rope, (1470, -225))
        win.blit(close, (1580, 150))
