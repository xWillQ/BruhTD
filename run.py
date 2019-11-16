import pygame
from main_menu.main_menu import MainMenu

pygame.init()
win = pygame.display.set_mode((1368, 720))
mainmenu = MainMenu(win)
mainmenu.run()