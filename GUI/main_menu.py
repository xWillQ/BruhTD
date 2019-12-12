import pygame
import G
from GUI.button import isInside

playBTN = pygame.transform.scale(pygame.image.load('Assets/level_decos/PLAY_VTN.png'), (1920, 1082))

level_ch = pygame.transform.scale(pygame.image.load('Assets/level_decos/levels_menu.png'), (1920, 1082))
lose_window = pygame.transform.scale(pygame.image.load('Assets/GUI/failed/preview_failed.png'), (1920, 1080))
win_window = pygame.transform.scale(pygame.image.load('Assets/GUI/win/preview_win.png'), (1920, 1080))


def draw():

    mouse_pos = pygame.mouse.get_pos()
    if G.condition == 0:
        G.win.blit(playBTN, (0, -2))  # starting window
        if G.event.type is pygame.MOUSEBUTTONUP:
            if isInside(mouse_pos[0], mouse_pos[1], 946, 550, 310):
                G.condition = 1

    if G.condition == 1:  # level choice menu

        G.win.blit(level_ch, (0, -2))
        if G.event.type is pygame.MOUSEBUTTONUP:
            if isInside(mouse_pos[0], mouse_pos[1], 1400, 307, 108):
                G.condition = 0
            if isInside(mouse_pos[0], mouse_pos[1], 670, 540, 150):
                G.level_number = 1
                G.condition = 10
            if isInside(mouse_pos[0], mouse_pos[1], 867, 540, 150):
                G.level_number = 2
                G.condition = 10

    if G.condition == 2:  # win window

        G.win.blit(lose_window, (0, 0))
        if G.event.type is pygame.MOUSEBUTTONUP:
            if isInside(mouse_pos[0], mouse_pos[1], 1087, 868, 150):
                G.condition = 1
                G.level_number = 0

    if G.condition == 3:  # lose window

        G.win.blit(win_window, (0, 0))
        if G.event.type is pygame.MOUSEBUTTONUP:
            if isInside(mouse_pos[0], mouse_pos[1], 820, 868, 150):
                G.condition = 1
                G.level_number = 0

    print(mouse_pos)
    G.event = G.event_N
