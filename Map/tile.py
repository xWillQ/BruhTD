import pygame
import os

class Tile():

    def __init__(self, win, texture, X, Y):

        self.win = win
        self.texture = texture
        self.X = X
        self.Y = Y
        self.T_C = 150

    def draw(self):

        self.win.blit(pygame.transform.scale(self.texture, (self.T_C, self.T_C)), (self.X, self.Y))
        
