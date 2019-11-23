import pygame
import os

class path_turn:
    def __init__(self, x, y, rotation, asset, clockwise):
        self.ass_posX = x
        self.ass_posY = y
        self.rotation = rotation
        self.asset = asset
        self.clockwise = clockwise