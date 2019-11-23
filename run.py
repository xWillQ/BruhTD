import pygame
from game import game

pygame.init()
win = pygame.display.set_mode((1368, 720))
gamewindow = game(win)
gamewindow.run()