import pygame
import G
from GUI.button import isInside
from GUI.player import Player as player


bg = pygame.transform.scale(pygame.image.load('Assets/GUI/menu/bg.png'), (1920, 1080))
playBTN = pygame.transform.scale(pygame.image.load('Assets/GUI/menu/button_play.png'), (200, 200))

table = pygame.transform.scale(pygame.image.load('Assets/GUI/levels/table.png'), (1360, 740))
empty_bt = pygame.transform.scale(pygame.image.load('Assets/GUI/levels/btton_empty.png'), (100, 100))
num1 = pygame.image.load('Assets/GUI/levels/num_1.png')
rope = pygame.image.load('Assets/GUI/settings/rope_big.png')
close = pygame.transform.scale(pygame.image.load('Assets/GUI/settings/button_close.png'), (80, 80))

dark = pygame.transform.scale(pygame.image.load('Assets/GUI/failed/dark.png'), (1920, 1080))
kek = pygame.transform.scale(pygame.image.load('Assets/GUI/failed/preview_failed.png'), (1920, 1080))
kekW = pygame.transform.scale(pygame.image.load('Assets/GUI/win/preview_win.png'), (1920, 1080))


def draw():

    if G.condition == 0:
        if G.event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[1] <= 635 and mouse_pos[0] >= 840 and mouse_pos[1] >= 435 and mouse_pos[0] <= 1040:
                G.condition = 1
        G.win.blit(bg, (0, 0))
        G.win.blit(dark, (0, 0))
        G.win.blit(playBTN, (840, 435))

    if G.condition == 1:

        G.win.blit(bg, (0, 0))
        G.win.blit(dark, (0, 0))
        G.win.blit(table, (300, 175))
        G.win.blit(empty_bt, (415, 250))
        G.win.blit(num1, (450, 270))
        G.win.blit(rope, (450, -225))
        G.win.blit(rope, (1470, -225))
        G.win.blit(close, (1580, 150))
        if G.event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[1] <= 230 and mouse_pos[0] >= 1580 and mouse_pos[1] >= 150 and mouse_pos[0] <= 1640:
                G.condition = 0
            if mouse_pos[1] <= 350 and mouse_pos[0] >= 420 and mouse_pos[1] >= 250 and mouse_pos[0] <= 510:
                G.level_number = 1
                G.condition = 10

    if G.condition == 2:

        mouse_pos = pygame.mouse.get_pos()
        G.win.blit(bg, (0, 0))
        G.win.blit(dark, (0, 0))
        G.win.blit(kek, (0, 0))
        if G.event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if isInside(mouse_pos[0], mouse_pos[1], 1087, 868, 150):
                G.condition = 1
                G.level_number = 0

        print(mouse_pos)

    if G.condition == 3:

        mouse_pos = pygame.mouse.get_pos()

        print(mouse_pos)
        G.win.blit(bg, (0, 0))
        G.win.blit(dark, (0, 0))
        G.win.blit(kekW, (0, 0))

        if G.event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if isInside(mouse_pos[0], mouse_pos[1], 820, 868, 150):
                G.condition = 1
                G.level_number = 0

    G.event = G.event_N
