from math import sqrt
import pygame
import G
from GUI.button import isInside

archer_icon = pygame.transform.scale(pygame.image.load('Assets/Towers/archer/lvl1_archer_icon.png'), (40, 40))
support_icon = pygame.transform.scale(pygame.image.load('Assets/Towers/support/lvl1_support_icon.png'), (40, 40))
magic_icon = pygame.transform.scale(pygame.image.load('Assets/Towers/magic/lvl1_magic_icon.png'), (40, 55))

build_gui = pygame.transform.scale(pygame.image.load('Assets/Towers/archer/build_gui.png'), (180, 180))

towerType = {"archer": [{"damage": 10, "cooldown": 50, "radius": 160},  # TODO: подобрать значения shiftX и shiftY. В процентах от финального спрайта, чем больше, тем правее/ниже
                        {"damage": 10, "cooldown": 50, "radius": 160},
                        {"damage": 10, "cooldown": 50, "radius": 160}],
             "magic": [{"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.05, "shiftY": 0.3},
                       {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.05, "shiftY": 0.3},
                       {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.05, "shiftY": 0.3}],
             "support": [{"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.0, "shiftY": 0.19},
                         {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.0, "shiftY": 0.19},
                         {"damage": 10, "cooldown": 50, "radius": 160, "shiftX": 0.0, "shiftY": 0.19}]}


def loadTypes(transformation, level):
    """Загружает текстуры соответствующие карте level, умножает каждую на коэффициент transformation"""
    archerShifts = {"forest": [{"towerShiftX": 0.035, "towerShiftY": 0.22, "topShiftX": 0.07, "topShiftY": -0.76, "archerShiftX": 0.29, "archerShiftY": -0.85},
                               {"towerShiftX": 0.035, "towerShiftY": 0.22, "topShiftX": 0.07, "topShiftY": -0.73, "archerShiftX": 0.35, "archerShiftY": -0.85},
                               {"towerShiftX": 0.0, "towerShiftY": 0.2, "topShiftX": 0.14, "topShiftY": -0.73, "archerShiftX": 1.06, "archerShiftY": -0.79, "archer2ShiftX": 0.99, "archer2ShiftY": -0.79}],
                    "desert": [{"towerShiftX": 0.03, "towerShiftY": 0.2, "archerShiftX": 0.29, "archerShiftY": -0.45},
                               {"towerShiftX": 0.03, "towerShiftY": 0.2, "archerShiftX": 0.39, "archerShiftY": -0.45},
                               {"towerShiftX": 0.0, "towerShiftY": 0.2, "archerShiftX": 0.90, "archerShiftY": -0.47, "archer2ShiftX": 0.80, "archer2ShiftY": -0.47}],
                    "other":  [{"towerShiftX": 0.035, "towerShiftY": 0.22, "archerShiftX": 0.35, "archerShiftY": -0.335},   # noqa
                               {"towerShiftX": 0.035, "towerShiftY": 0.22, "archerShiftX": 0.35, "archerShiftY": -0.335},
                               {"towerShiftX": 0.0, "towerShiftY": 0.2, "archerShiftX": 0.90, "archerShiftY": -0.35, "archer2ShiftX": 0.80, "archer2ShiftY": -0.34}]}
    # TODO: подобрать все значения
    magic = {"forest": [{"finalHeight": 0.8, "towerShiftY": 0.2, "topShiftX": 0.34, "topShiftY": 0.0},
                        {"finalHeight": 0.8, "towerShiftY": 0.2, "topShiftX": 0.34, "topShiftY": 0.0},
                        {"finalHeight": 0.8, "towerShiftY": 0.2, "topShiftX": 0.34, "topShiftY": 0.0}],
             "desert": [{"finalHeight": 0.4, "towerShiftY": 0.11, "topShiftX": 0.36, "topShiftY": 0.0},
                        {"finalHeight": 0.4, "towerShiftY": 0.11, "topShiftX": 0.36, "topShiftY": 0.0},
                        {"finalHeight": 0.4, "towerShiftY": 0.11, "topShiftX": 0.36, "topShiftY": 0.0}],
             "other":  [{"finalHeight": 0.1, "towerShiftY": 0.018, "topShiftX": 0.315, "topShiftY": 0.0},   # noqa
                        {"finalHeight": 0.1, "towerShiftY": 0.018, "topShiftX": 0.315, "topShiftY": 0.0},
                        {"finalHeight": 0.1, "towerShiftY": 0.018, "topShiftX": 0.315, "topShiftY": 0.0}]}
    if (level != "forest" and level != "desert"):
        level = "other"
    for lvl in range(0, 3):
        #  Archer

        towerType["archer"][lvl]["assets"] = {}
        tower = pygame.image.load("Assets/Towers/Archer/lvl" + str(lvl + 1) + "_" + level + "_tower.png")
        width = int(tower.get_width() * transformation)
        height = int(tower.get_height() * transformation)
        tower = pygame.transform.scale(tower, (int(width), int(height)))
        towerType["archer"][lvl]["assets"]["tower"] = tower
        towerType["archer"][lvl]["towerShiftX"] = int(-width / 2 + width * archerShifts[level][lvl]["towerShiftX"])
        towerType["archer"][lvl]["towerShiftY"] = int(-height + height * archerShifts[level][lvl]["towerShiftY"])

        towerType["archer"][lvl]["assets"]["archer"] = []
        for i in range(0, 6):
            archer = pygame.image.load("Assets/Towers/Archer/" + level + "_archer_" + str(i) + ".png")
            archer = pygame.transform.scale(archer, (int(archer.get_width() * transformation), int(archer.get_height() * transformation)))
            towerType["archer"][lvl]["assets"]["archer"].append(archer)

        if (level == "forest"):
            top = pygame.image.load("Assets/Towers/archer/lvl" + str(lvl + 1) + "_" + level + "_top.png")
            top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
            towerType["archer"][lvl]["assets"]["top"] = top
            towerType["archer"][lvl]["topShiftX"] = int(towerType["archer"][lvl]["towerShiftX"] + int(top.get_width() * transformation) * archerShifts["forest"][lvl]["topShiftX"])
            towerType["archer"][lvl]["topShiftY"] = int(towerType["archer"][lvl]["towerShiftY"] + int(top.get_height() * transformation) * archerShifts["forest"][lvl]["topShiftY"])

        width = towerType["archer"][lvl]["assets"]["archer"][0].get_width()
        height = towerType["archer"][lvl]["assets"]["archer"][0].get_height()
        towerType["archer"][lvl]["archerShiftX"] = int(towerType["archer"][lvl]["towerShiftX"] / 2 + width * archerShifts[level][lvl]["archerShiftX"])
        towerType["archer"][lvl]["archerShiftY"] = int(towerType["archer"][lvl]["towerShiftY"] + height * archerShifts[level][lvl]["archerShiftY"])
        if (lvl == 2):
            towerType["archer"][lvl]["archer2ShiftX"] = int(towerType["archer"][lvl]["towerShiftX"] / 2 + width * archerShifts[level][lvl]["archer2ShiftX"])
            towerType["archer"][lvl]["archer2ShiftY"] = int(towerType["archer"][lvl]["towerShiftY"] + height * archerShifts[level][lvl]["archer2ShiftY"])

        towerType["archer"][lvl]["height"] = towerType["archer"][lvl]["assets"]["tower"].get_height() + towerType["archer"][lvl]["assets"]["archer"][0].get_height()
        towerType["archer"][lvl]["clearShiftY"] = towerType["archer"][lvl]["archerShiftY"]
        if (lvl == 2):
            towerType["archer"][lvl]["width"] = towerType["archer"][2]["assets"]["archer"][3].get_width() * 2.04
            towerType["archer"][lvl]["clearShiftX"] = towerType["archer"][2]["archer2ShiftX"] - towerType["archer"][2]["assets"]["archer"][3].get_width()
        else:
            towerType["archer"][lvl]["width"] = towerType["archer"][lvl]["assets"]["tower"].get_width()
            towerType["archer"][lvl]["clearShiftX"] = towerType["archer"][lvl]["towerShiftX"]

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
                height += int(top.get_height() * magic[level][lvl]["finalHeight"])
            elif (level == "desert"):
                height += int(top.get_height() * magic[level][lvl]["finalHeight"])
        else:
            top = pygame.image.load("Assets/Towers/magic/other_tower_top_lvl1.png")
            top = pygame.transform.scale(top, (int(top.get_width() * transformation), int(top.get_height() * transformation)))
            height += int(top.get_height() * magic[level][lvl]["finalHeight"])

        towerType["magic"][lvl]["asset"] = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        towerType["magic"][lvl]["asset"].blit(tower, (0, height * magic[level][lvl]["towerShiftY"]))
        towerType["magic"][lvl]["asset"].blit(top, (width * magic[level][lvl]["topShiftX"], height * magic[level][lvl]["topShiftY"]))

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


def clearAll(towers, win, background):
    """Стирает все башни из массива towers с поверхности win, заменяя соответствующей частью изображения background"""
    cleared = []
    for tower in towers:
        if tower.level != 0:
            currX = tower.x + towerType[tower.typeName][tower.level - 1]["clearShiftX"]
            currY = tower.y + towerType[tower.typeName][tower.level - 1]["clearShiftY"]
            cleared.append(pygame.Rect(int(currX), int(currY), towerType[tower.typeName][tower.level - 1]["width"], towerType[tower.typeName][tower.level - 1]["height"]))
            win.blit(background, (currX, currY), cleared[len(cleared) - 1])
    return cleared


class Tower():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gui_opened = False
        self.level = 0

    def isInside(self, x, y):
        return (sqrt((x - self.x)**2 + (y - self.y)**2) <= self.radius)

    def attack(self):
        """Устанавливает кулдаун и начинает анимацию атаки"""
        if (self.typeName == "archer" and self.level == 3):
            if (self.cooldown == 0):
                self.cooldown = towerType[self.typeName][self.level - 1]["cooldown"]
                self.frame = 1
            else:
                self.cooldown2 = towerType[self.typeName][self.level - 1]["cooldown"]
                self.frame2 = 1
        else:
            self.cooldown = towerType[self.typeName][self.level - 1]["cooldown"]
            self.frame = 1

    def isReady(self):
        """Возвращает True, если башня может стрелять"""
        if (self.cooldown == 0):
            return True
        if (self.typeName == "archer" and self.level == 3):
            if (self.cooldown2 == 0):
                return True
        return False

    def setType(self, typeName):
        """Устанавливает уровень на 1. Заполняет атрибуты башни согласно towerType"""
        self.typeName = typeName
        self.level = 1
        self.damage = towerType[self.typeName][self.level - 1]["damage"]
        self.radius = towerType[self.typeName][self.level - 1]["radius"]
        self.frame = 0
        self.cooldown = 0

    def upgrade(self):
        """Увеличивает уровень на 1, но не выше 3. Обновляет атрибуты башни согласно towerType"""
        if (self.level == 3):
            return
        self.level += 1
        self.damage = towerType[self.typeName][self.level - 1]["damage"]
        self.radius = towerType[self.typeName][self.level - 1]["radius"]
        if (self.typeName == "archer" and self.level == 3):
            self.frame2 = 0
            self.cooldown2 = 0

    def draw(self, win, level):
        """Выводит башню на поверхность win и переходит на следующий кадр"""
        if (self.typeName == "archer"):
            if (level == "forest"):
                win.blit(towerType[self.typeName][self.level - 1]["assets"]["top"], (self.x + towerType[self.typeName][self.level - 1]["topShiftX"], self.y + towerType[self.typeName][self.level - 1]["topShiftY"]))
            else:
                win.blit(towerType[self.typeName][self.level - 1]["assets"]["tower"], (self.x + towerType[self.typeName][self.level - 1]["towerShiftX"], self.y + towerType[self.typeName][self.level - 1]["towerShiftY"]))
            win.blit(towerType[self.typeName][self.level - 1]["assets"]["archer"][self.frame], (self.x + towerType[self.typeName][self.level - 1]["archerShiftX"], self.y + towerType[self.typeName][self.level - 1]["archerShiftY"]))
            if (self.frame != 0):
                self.frame += 1
                if (self.frame >= 6):
                    self.frame = 0
            if (self.level == 3):
                width = towerType[self.typeName][self.level - 1]["assets"]["archer"][self.frame2].get_width()
                win.blit(pygame.transform.flip(towerType[self.typeName][self.level - 1]["assets"]["archer"][self.frame2], True, False), (self.x + towerType[self.typeName][self.level - 1]["archer2ShiftX"] - width, self.y + towerType[self.typeName][self.level - 1]["archer2ShiftY"]))
                if (self.frame2 != 0):
                    self.frame2 += 1
                    if (self.frame2 >= 6):
                        self.frame2 = 0
            if (level == "forest"):
                win.blit(towerType[self.typeName][self.level - 1]["assets"]["tower"], (self.x + towerType[self.typeName][self.level - 1]["towerShiftX"], self.y + towerType[self.typeName][self.level - 1]["towerShiftY"]))
        else:
            win.blit(towerType[self.typeName][self.level - 1]["asset"], (self.x + towerType[self.typeName][self.level - 1]["shiftX"], self.y + towerType[self.typeName][self.level - 1]["shiftY"]))
        # pygame.draw.circle(win, (255, 0, 0), (round(self.x), round(self.y)), 2)

    def draw_gui(tower):

        if tower.level == 0:
            G.win.blit(build_gui, (tower.x - 90, tower.y - 90))

            G.win.blit(archer_icon, (tower.x - 75, tower.y - 75))
            G.win.blit(support_icon, (tower.x - 78, tower.y + 30))
            G.win.blit(magic_icon, (tower.x + 37, tower.y - 83))

        if tower.level != 0:
            G.win.blit(build_gui, (tower.x - 90, tower.y - 90))

    def gui_level_up(tower, mouse_pos):

        if tower.level != 0:
            if isInside(mouse_pos[0], mouse_pos[1], tower.x - 60, tower.y - 50, 70):
                tower.upgrade()

    def gui_close(towers, exc):

        for i in range(len(towers)):
            if i != exc:
                towers[i].gui_opened = False

    def gui_type_change(tower, mouse_pos):

        if tower.level == 0:
            if isInside(mouse_pos[0], mouse_pos[1], tower.x - 60, tower.y - 50, 70):
                tower.setType("archer")
                tower.gui_opened = False
            if isInside(mouse_pos[0], mouse_pos[1], tower.x + 60, tower.y - 50, 70):
                tower.setType("magic")
                tower.gui_opened = False
            if isInside(mouse_pos[0], mouse_pos[1], tower.x - 60, tower.y + 60, 70):
                tower.setType("support")
                tower.gui_opened = False
