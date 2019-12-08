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

# def loadTypes(transformation, level):
#     if (level != "forest" and level != "desert"):
#         level = "other"
#     for t in towerType:
#         tower = pygame.image.load("Assets/Towers/" + t + "/lvl1_" + level + "_tower.png")
#         tower = pygame.transform.scale(tower, (int(transformation * tower.get_width()), int(transformation * tower.get_height())))
#         top = pygame.image.load("Assets/Towers/" + t + "/lvl1_forest_top.png")
#         top = pygame.transform.scale(top, (int(transformation * top.get_width()), int(transformation * top.get_height())))
#         archers = []
#         for frame in range(0, 6):
#             archer = pygame.image.load("Assets/Towers/" + t + "/lvl1_" + level + "_.png")

#     tower = pygame.image.load("Assets/Towers/archer/lvl1_" + level + "_tower.png")
#     tower = pygame.transform.scale(tower, (int(transformation * tower.get_width()), int(transformation * tower.get_height())))
#     maxHeight = 0
#     archers = []
#     for i in range(0, 6):
#         archer = pygame.image.load("Assets/Towers/archer/lvl1_" + level + "_archer_" + str(i) + ".png")
#         archers.append(pygame.transform.scale(tower, (int(transformation * tower.get_width()), int(transformation * tower.get_height()))))
#         if (int(transformation * tower.get_height()) > maxHeight):
#             maxHeight = int(transformation * tower.get_height())

#     top = pygame.image.load("Assets/Towers/archer/lvl1_forest_top.png")
#     top = pygame.transform.scale(top, (int(transformation * top.get_width()), int(transformation * top.get_height())))

#     towerType["archer"]["assets"] = []
#     for i in range(0, 6):
#         asset = pygame.Surface((int(transformation * tower.get_width()), maxHeight))

#     assetExample = pygame.image.load("Assets/Towers/archer/lvl" + str(lvl) + "_tower.png")
#     towerDimensions = (int(assetExample.get_width() * transformation), int(assetExample.get_height() * transformation))
#     assetExample = pygame.image.load("Assets/Towers/archer/lvl" + str(lvl) + "_top.png")
#     topDimensions = (int(assetExample.get_width() * transformation), int(assetExample.get_height() * transformation))
#     assetExample = pygame.image.load("Assets/Towers/archer/lvl" + str(lvl) + "_archer_0.png")
#     archerDimensions = (int(assetExample.get_width() * transformation), int(assetExample.get_height() * transformation))

#     self.shifts["tower"] = (int(-towerDimensions[0] / 2 + towerDimensions[0] * 0.055), int(-towerDimensions[1] + towerDimensions[1] * 0.19))
#     self.shifts["top"] = (int(self.shifts["tower"][0] + topDimensions[0] * 0.07), int(self.shifts["tower"][1] - topDimensions[1] * 0.75))
#     self.shifts["archer"] = (int(self.shifts["tower"][0] + archerDimensions[0] * 1.2), int(self.shifts["tower"][1] - archerDimensions[1] * 0.9))
#     self.shifts[0] = self.shifts["tower"][0]
#     self.shifts[1] = self.shifts["archer"][1]
#     self.width = towerDimensions[0]
#     self.height = towerDimensions[1] + archerDimensions[1]

#     self.assets = []
#     self.assets.append(pygame.transform.scale(pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_tower.png"), (towerDimensions[0], towerDimensions[1])))
#     self.assets.append([])
#     self.assets.append(pygame.transform.scale(pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_top.png"), (topDimensions[0], topDimensions[1])))
#     for i in range(0, 6):
#         asset = pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_archer_" + str(i) + ".png")
#         width = int(asset.get_width() * self.transformation)
#         height = int(asset.get_height() * self.transformation)
#         self.assets[1].append(pygame.transform.scale(asset, (width, height)))


def loadTypes(transformation, level):
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
            height = towerHeight + int(archer.get_height() * 1.2)
            towerShiftY = 0.37
            towerType["archer"][lvl]["assets"].append(pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha())

            if (level == "forest"):
                top = pygame.image.load("Assets/Towers/archer/lvl" + str(lvl + 1) + "_" + level + "_top.png")
                top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
                archerShiftX = 0.32
                if (i == 0):
                    archerShiftY = 0.08  # TODO: подобрать значения. Чем больше, тем ниже спрайт, в процентах от высоты финального спрайта. Для уровня Forest
                    topShiftY = 0.165
                elif (i == 1):
                    archerShiftY = 0.08
                    topShiftY = 0.165
                elif (i == 2):
                    archerShiftY = 0.08
                    topShiftY = 0.165
                elif (i == 3):
                    archerShiftY = 0.08
                    topShiftY = 0.165
                elif (i == 4):
                    archerShiftY = 0.08
                    topShiftY = 0.165
                elif (i == 5):
                    archerShiftY = 0.08
                    topShiftY = 0.165
                topShiftX = 0.045
                towerType["archer"][lvl]["assets"][i].blit(top, (width * topShiftX, height * topShiftY))
                towerType["archer"][lvl]["assets"][i].blit(archer, (width * archerShiftX, height * archerShiftY))
                towerType["archer"][lvl]["assets"][i].blit(tower, (0, width * towerShiftY))
            else:
                archerShiftX = 0.327
                if (i == 0):
                    archerShiftY = 0.195  # TODO: подобрать значения. Чем больше, тем ниже спрайт, в процентах от высоты финального спрайта. Для уровней Desert и Other
                elif (i == 1):
                    archerShiftY = 0.195
                elif (i == 2):
                    archerShiftY = 0.195
                elif (i == 3):
                    archerShiftY = 0.195
                elif (i == 4):
                    archerShiftY = 0.195
                elif (i == 5):
                    archerShiftY = 0.195
                towerType["archer"][lvl]["assets"][i].blit(tower, (0, width * towerShiftY))
                towerType["archer"][lvl]["assets"][i].blit(archer, (width * archerShiftX, height * archerShiftY))

        towerType["archer"][lvl]["shiftX"] = int(-width / 2 + width * towerType["archer"][lvl]["shiftX"])
        towerType["archer"][lvl]["shiftY"] = int(-height + height * towerType["archer"][lvl]["shiftY"])

        #  Magic

        tower = pygame.image.load("Assets/Towers/magic/lvl" + str(lvl + 1) + "_" + level + "_tower.png")
        width = int(tower.get_width() * transformation)
        height = int(tower.get_height() * transformation)
        tower = pygame.transform.scale(tower, (width, height))
        top = True
        towerShiftY = 0
        topShiftX = 0
        topShiftY = 0

        if (level != "other"):
            top = pygame.image.load("Assets/Towers/magic/" + level + "_tower_top.png")
            top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
            if (level == "forest"):
                height += int(top.get_height() * 0.8)
                towerShiftY = 0.2
                topShiftX = 0.34
                topShiftY = 0.0
            elif (level == "desert"):
                height += int(top.get_height() * 0.4)
                towerShiftY = 0.11
                topShiftX = 0.36
                topShiftY = 0.0
        else:
            top = pygame.image.load("Assets/Towers/magic/other_tower_top_lvl1.png")
            top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
            height += int(top.get_height() * 0.1)
            towerShiftY = 0.018
            topShiftX = 0.315
            topShiftY = 0.0

        towerType["magic"][lvl]["asset"] = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        towerType["magic"][lvl]["asset"].blit(tower, (0, height * towerShiftY))
        towerType["magic"][lvl]["asset"].blit(top, (width * topShiftX, height * topShiftY))

        towerType["magic"][lvl]["shiftX"] = int(-width / 2 + width * towerType["magic"][lvl]["shiftX"])
        towerType["magic"][lvl]["shiftY"] = int(-height + height * towerType["magic"][lvl]["shiftY"])

        #  Support

        tower = pygame.image.load("Assets/Towers/support/lvl" + str(lvl + 1) + "_" + level + "_tower.png")
        width = int(tower.get_width() * transformation)
        height = int(tower.get_height() * transformation)
        tower = pygame.transform.scale(tower, (width, height))

        towerType["support"][lvl]["asset"] = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        towerType["support"][lvl]["asset"].blit(tower, (0, 0))
        towerType["support"][lvl]["shiftX"] = int(-width / 2 + width * towerType["support"][lvl]["shiftX"])
        towerType["support"][lvl]["shiftY"] = int(-height + height * towerType["support"][lvl]["shiftY"])


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

    def attack(self):
        self.cooldown = towerType[self.type][self.level - 1]["cooldown"]
        self.frame = 1

    def setType(self, typeName):
        self.type = typeName
        self.level = 1
        self.damage = towerType[self.type][self.level - 1]["damage"]
        self.radius = towerType[self.type][self.level - 1]["radius"]
        #self.loadAssets()

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
            asset = pygame.image.load("Assets/Towers/" + self.type + "/lvl" + str(self.level) + "_archer_" + str(i) + ".png")
            width = int(asset.get_width() * self.transformation)
            height = int(asset.get_height() * self.transformation)
            self.assets[1].append(pygame.transform.scale(asset, (width, height)))

    def draw(self, win):
        if (self.type == "archer"):
            win.blit(towerType[self.type][self.level - 1]["assets"][self.frame], (self.x + towerType[self.type][self.level - 1]["shiftX"], self.y + towerType[self.type][self.level - 1]["shiftY"]))
            self.frame += 1
            if (self.frame >= 6):
                self.frame = 0
        else:
            win.blit(towerType[self.type][self.level - 1]["asset"], (self.x + towerType[self.type][self.level - 1]["shiftX"], self.y + towerType[self.type][self.level - 1]["shiftY"]))
