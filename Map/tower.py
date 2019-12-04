from math import sqrt

towerType = {"archer": {"damage": 5, "cooldown": 10, "radius": 100, "assetFolder": ""}}


class Tower():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 0
        self.radius = 0
        self.cooldown = 0
        self.type = ""

    def isInside(self, x, y):
        return (sqrt((x - self.x)**2 + (y - self.y)**2) <= self.radius)

    def attack(self, mob):
        mob.hp = mob.hp - self.damage
        self.cooldown = towerType[self.type]["cooldown"]

    def setType(self, typeName):
        self.type = typeName
        self.damage = towerType[self.type]["damage"]
        self.radius = towerType[self.type]["radius"]
