from math import sqrt
import pygame
import os

towerType = {"archer": {"damage": 5, "cooldown": 10, "radius": 100, "assetFolder": ""}}
tower_place = pygame.transform.scale(pygame.image.load(os.path.join('Assets/Assets_All/tiles/forest/22.png')), (120, 120))


class Tower():
    def __init__(self, x, y, transformation):
        self.x = x
        self.y = y
        self.tr = transformation
        self.shiftX = transformation / 2
        self.shiftY = transformation / 2
        self.damage = 50
        self.radius = 300
        self.cooldown = 0
        self.type = ""

    def isInside(self, x, y):

        return (sqrt((x - self.x)**2 + (y - self.y)**2) <= self.radius)

    def attack(self, mob):

        if self.cooldown == 0:
            mob.hp = mob.hp - self.damage
            self.cooldown = 30

        if self.cooldown > 0:
            self.cooldown -= 1
        # self.cooldown = towerType[self.type]["cooldown"]

    def setType(self, typeName):

        self.type = typeName
        self.damage = towerType[self.type]["damage"]
        self.radius = towerType[self.type]["radius"]

    def draw(self, win):

        win.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets/towers/archer/1.png')), (self.tr - 28, 37)), (self.x - self.shiftX + 5, self.y - self.shiftY - 27))
        win.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets/towers/archer/37.png')), (40, 40)), (self.x - self.shiftX + 32, self.y - self.shiftY - 30))
        win.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets/towers/archer/2.png')), (self.tr, self.tr)), (self.x - self.shiftX, self.y - self.shiftY))