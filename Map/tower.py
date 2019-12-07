from math import sqrt
import pygame

towerType = {"archer": {"damage": 5, "cooldown": 10, "radius": 100}}


class Tower():
    def __init__(self, x, y, transformation):
        self.x = x
        self.y = y
        self.damage = 0
        self.radius = 0
        self.cooldown = 0
        self.type = ""
        self.level = 0
        self.transformation = transformation
        self.frame = 0
        self.shifts = {0: 0, 1: 0}
        self.width = 0
        self.height = 0

    def isInside(self, x, y):
        return (sqrt((x - self.x)**2 + (y - self.y)**2) <= self.radius)

    def attack(self, mob):
        mob.hp = mob.hp - self.damage
        self.cooldown = towerType[self.type]["cooldown"]

    def setType(self, typeName):
        self.type = typeName
        self.level = 1
        self.damage = towerType[self.type]["damage"]
        self.radius = towerType[self.type]["radius"]
        self.loadAssets()

    def loadAssets(self):
        assetExample = pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_tower.png")
        towerDimensions = (int(assetExample.get_width() * self.transformation), int(assetExample.get_height() * self.transformation))
        assetExample = pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_top.png")
        topDimensions = (int(assetExample.get_width() * self.transformation), int(assetExample.get_height() * self.transformation))
        assetExample = pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_archer_0.png")
        archerDimensions = (int(assetExample.get_width() * self.transformation), int(assetExample.get_height() * self.transformation))

        self.shifts["tower"] = (int(-towerDimensions[0] / 2 + towerDimensions[0] * 0.055), int(-towerDimensions[1] + towerDimensions[1] * 0.19))
        self.shifts["top"] = (int(self.shifts["tower"][0] + topDimensions[0] * 0.07), int(self.shifts["tower"][1] - topDimensions[1] * 0.75))
        self.shifts["archer"] = (int(self.shifts["tower"][0] + archerDimensions[0] * 1.2), int(self.shifts["tower"][1] - archerDimensions[1] * 0.9))
        self.shifts[0] = self.shifts["tower"][0]
        self.shifts[1] = self.shifts["archer"][1]
        self.width = towerDimensions[0]
        self.height = towerDimensions[1] + archerDimensions[1]

        self.assets = []
        self.assets.append(pygame.transform.scale(pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_tower.png"), (towerDimensions[0], towerDimensions[1])))
        self.assets.append([])
        self.assets.append(pygame.transform.scale(pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_top.png"), (topDimensions[0], topDimensions[1])))
        for i in range(0, 6):
            self.assets[1].append(pygame.transform.scale(pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_archer_" + str(i) + ".png"), (archerDimensions[0], archerDimensions[1])))

    def draw(self, win):
        if (self.type != ""):
            win.blit(self.assets[2], (self.x + self.shifts["top"][0], self.y + self.shifts["top"][1]))
            win.blit(self.assets[1][0], (self.x + self.shifts["archer"][0], self.y + self.shifts["archer"][1]))
            win.blit(self.assets[0], (self.x + self.shifts["tower"][0], self.y + self.shifts["tower"][1]))
