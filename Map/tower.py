from math import sqrt
import pygame

towerType = {"archer": [{"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.055, "shiftY": 0.17},  # TODO: подобрать значения shiftX и shiftY. В процентах от финального спрайта, чем больше, тем правее/ниже
                        {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.055, "shiftY": 0.17},
                        {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.055, "shiftY": 0.17}],
             "magic": [{"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.05, "shiftY": 0.3},
                       {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.05, "shiftY": 0.3},
                       {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.05, "shiftY": 0.3}],
             "support": [{"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.0, "shiftY": 0.19},
                         {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.0, "shiftY": 0.19},
                         {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.0, "shiftY": 0.19}]}


def loadTypes(transformation, level):
    # TODO: подобрать все значения
    coeficients = {"archer": {"forest":[{"finalHeight": [0.95, 1.01, 1.01, 1.01, 0.967, 0.95], "towerShiftY": 0.305, "archerShiftX": [0.32, 0.32, 0.32, 0.32, 0.32, 0.32], "archerShiftY": [0.003, 0.021, 0.021, 0.021, 0.0281, 0.0016], "topShiftX": 0.048, "topShiftY": 0.12},     # noqa
                                        {"finalHeight": [0.95, 0.99, 0.99, 0.99, 0.94, 0.95], "towerShiftY": 0.302, "archerShiftX": [0.32, 0.32, 0.32, 0.32, 0.32, 0.32], "archerShiftY": [0.003, 0.021, 0.021, 0.021, 0.0281, 0.0016], "topShiftX": 0.05, "topShiftY": 0.128},
                                        {"finalHeight": [0.93, 0.985, 0.985, 0.985, 0.947, 0.93], "towerShiftY": 0.29, "archerShiftX": [0.32, 0.32, 0.32, 0.32, 0.32, 0.32], "archerShiftY": [0.003, 0.021, 0.021, 0.021, 0.0281, 0.0016], "topShiftX": 0.101, "topShiftY": 0.107}],
                              "desert":[{"finalHeight": [1.2, 1.2, 1.2, 1.2, 1.2, 1.2], "towerShiftY": 0.32, "archerShiftX": [0.327, 0.327, 0.327, 0.327, 0.327, 0.327], "archerShiftY": [0.195, 0.195, 0.195, 0.195, 0.195, 0.195]},  # noqa
                                        {"finalHeight": [1.2, 1.2, 1.2, 1.2, 1.2, 1.2], "towerShiftY": 0.32, "archerShiftX": [0.327, 0.327, 0.327, 0.327, 0.327, 0.327], "archerShiftY": [0.195, 0.195, 0.195, 0.195, 0.195, 0.195]},
                                        {"finalHeight": [1.2, 1.2, 1.2, 1.2, 1.2, 1.2], "towerShiftY": 0.32, "archerShiftX": [0.327, 0.327, 0.327, 0.327, 0.327, 0.327], "archerShiftY": [0.195, 0.195, 0.195, 0.195, 0.195, 0.195]}],
                              "other": [{"finalHeight": [1.2, 1.2, 1.2, 1.2, 1.2, 1.2], "towerShiftY": 0.32, "archerShiftX": [0.327, 0.327, 0.327, 0.327, 0.327, 0.327], "archerShiftY": [0.195, 0.195, 0.195, 0.195, 0.195, 0.195]},
                                        {"finalHeight": [1.2, 1.2, 1.2, 1.2, 1.2, 1.2], "towerShiftY": 0.32, "archerShiftX": [0.327, 0.327, 0.327, 0.327, 0.327, 0.327], "archerShiftY": [0.195, 0.195, 0.195, 0.195, 0.195, 0.195]},
                                        {"finalHeight": [1.2, 1.2, 1.2, 1.2, 1.2, 1.2], "towerShiftY": 0.32, "archerShiftX": [0.327, 0.327, 0.327, 0.327, 0.327, 0.327], "archerShiftY": [0.195, 0.195, 0.195, 0.195, 0.195, 0.195]}]},
                   "magic": {"forest": [{"finalHeight": 0.8, "towerShiftY": 0.2, "topShiftX": 0.34, "topShiftY": 0.0},
                                        {"finalHeight": 0.8, "towerShiftY": 0.2, "topShiftX": 0.34, "topShiftY": 0.0},
                                        {"finalHeight": 0.8, "towerShiftY": 0.2, "topShiftX": 0.34, "topShiftY": 0.0}],
                             "desert": [{"finalHeight": 0.4, "towerShiftY": 0.11, "topShiftX": 0.36, "topShiftY": 0.0},
                                        {"finalHeight": 0.4, "towerShiftY": 0.11, "topShiftX": 0.36, "topShiftY": 0.0},
                                        {"finalHeight": 0.4, "towerShiftY": 0.11, "topShiftX": 0.36, "topShiftY": 0.0}],
                             "other":  [{"finalHeight": 0.1, "towerShiftY": 0.018, "topShiftX": 0.315, "topShiftY": 0.0},   # noqa
                                        {"finalHeight": 0.1, "towerShiftY": 0.018, "topShiftX": 0.315, "topShiftY": 0.0},
                                        {"finalHeight": 0.1, "towerShiftY": 0.018, "topShiftX": 0.315, "topShiftY": 0.0}]}}

    for lvl in range(0, 3):
        #  Archer

        tower = pygame.image.load("Assets/Towers/Archer/lvl" + str(lvl + 1) + "_" + level + "_tower.png")
        width = int(tower.get_width() * transformation)
        towerHeight = int(tower.get_height() * transformation)
        tower = pygame.transform.scale(tower, (width, towerHeight))
        towerType["archer"][lvl]["assets"] = []

        for i in range(0, 6):
            archer = pygame.image.load("Assets/Towers/Archer/" + level + "_archer_" + str(i) + ".png")
            archer = pygame.transform.scale(archer, (int(archer.get_width() * transformation), int(archer.get_height() * transformation)))
            height = towerHeight + int(archer.get_height() * coeficients["archer"][level][lvl]["finalHeight"][i])
            towerType["archer"][lvl]["assets"].append(pygame.Surface((width, height)))  # , pygame.SRCALPHA, 32).convert_alpha())

            if (level == "forest"):
                top = pygame.image.load("Assets/Towers/archer/lvl" + str(lvl + 1) + "_" + level + "_top.png")
                top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
                towerType["archer"][lvl]["assets"][i].blit(top, (width * coeficients["archer"][level][lvl]["topShiftX"], height * coeficients["archer"][level][lvl]["topShiftY"]))
                towerType["archer"][lvl]["assets"][i].blit(archer, (width * coeficients["archer"][level][lvl]["archerShiftX"][i], height * coeficients["archer"][level][lvl]["archerShiftY"][i]))
                towerType["archer"][lvl]["assets"][i].blit(tower, (0, width * coeficients["archer"][level][lvl]["towerShiftY"]))
            else:
                towerType["archer"][lvl]["assets"][i].blit(tower, (0, width * coeficients["archer"][level][lvl]["towerShiftY"]))
                towerType["archer"][lvl]["assets"][i].blit(archer, (width * coeficients["archer"][level][lvl]["archerShiftX"][i], height * coeficients["archer"][level][lvl]["archerShiftY"][i]))

        towerType["archer"][lvl]["shiftX"] = int(-width / 2 + width * towerType["archer"][lvl]["shiftX"])
        towerType["archer"][lvl]["shiftY"] = int(-height + height * towerType["archer"][lvl]["shiftY"])

        #  Magic

        tower = pygame.image.load("Assets/Towers/magic/lvl" + str(lvl + 1) + "_" + level + "_tower.png")
        width = int(tower.get_width() * transformation)
        height = int(tower.get_height() * transformation)
        tower = pygame.transform.scale(tower, (width, height))
        top = True

        if (level != "other"):
            top = pygame.image.load("Assets/Towers/magic/" + level + "_tower_top.png")
            top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
            if (level == "forest"):
                height += int(top.get_height() * coeficients["magic"][level][lvl]["finalHeight"])
            elif (level == "desert"):
                height += int(top.get_height() * coeficients["magic"][level][lvl]["finalHeight"])
        else:
            top = pygame.image.load("Assets/Towers/magic/other_tower_top_lvl1.png")
            top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
            height += int(top.get_height() * coeficients["magic"][level][lvl]["finalHeight"])

        towerType["magic"][lvl]["asset"] = pygame.Surface((width, height))  # , pygame.SRCALPHA, 32).convert_alpha()
        towerType["magic"][lvl]["asset"].blit(tower, (0, height * coeficients["magic"][level][lvl]["towerShiftY"]))
        towerType["magic"][lvl]["asset"].blit(top, (width * coeficients["magic"][level][lvl]["topShiftX"], height * coeficients["magic"][level][lvl]["topShiftY"]))

        towerType["magic"][lvl]["shiftX"] = int(-width / 2 + width * towerType["magic"][lvl]["shiftX"])
        towerType["magic"][lvl]["shiftY"] = int(-height + height * towerType["magic"][lvl]["shiftY"])

        #  Support

        tower = pygame.image.load("Assets/Towers/support/lvl" + str(lvl + 1) + "_" + level + "_tower.png")
        width = int(tower.get_width() * transformation)
        height = int(tower.get_height() * transformation)
        tower = pygame.transform.scale(tower, (width, height))

        towerType["support"][lvl]["asset"] = pygame.Surface((width, height))  # , pygame.SRCALPHA, 32).convert_alpha()
        towerType["support"][lvl]["asset"].blit(tower, (0, 0))
        towerType["support"][lvl]["shiftX"] = int(-width / 2 + width * towerType["support"][lvl]["shiftX"])
        towerType["support"][lvl]["shiftY"] = int(-height + height * towerType["support"][lvl]["shiftY"])


class Tower():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 0
        self.radius = 0
        self.cooldown = 0
        self.type = ""
        self.level = 0
        self.frame = 0

    def isInside(self, x, y):
        return (sqrt((x - self.x)**2 + (y - self.y)**2) <= self.radius)

    def attack(self):
        self.cooldown = towerType[self.type][self.level - 1]["cooldown"]
        self.frame = 1

    def setType(self, typeName):
        self.type = typeName
        self.level = 1
        self.damage = towerType[self.type][self.level - 1]["damage"]
        self.radius = towerType[self.type][self.level - 1]["radius"]

    def draw(self, win):
        if (self.level != 0):
            if (self.type == "archer"):
                win.blit(towerType[self.type][self.level - 1]["assets"][self.frame], (self.x + towerType[self.type][self.level - 1]["shiftX"], self.y + towerType[self.type][self.level - 1]["shiftY"]))
                self.frame += 1
                if (self.frame >= 6):
                    self.frame = 0
            else:
                win.blit(towerType[self.type][self.level - 1]["asset"], (self.x + towerType[self.type][self.level - 1]["shiftX"], self.y + towerType[self.type][self.level - 1]["shiftY"]))
