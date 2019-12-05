from math import sqrt
import pygame
from PIL import Image


def loadMap(directions, start, transformation, level, width, height):

    horiz = (Image.open("Assets/Tiles/" + level + "/6.png")).resize((transformation, transformation))
    verti = (Image.open("Assets/Tiles/" + level + "/5.png")).resize((transformation, transformation))
    turn1 = (Image.open("Assets/Tiles/" + level + "/1.png")).resize((transformation, transformation))
    turn2 = (Image.open("Assets/Tiles/" + level + "/2.png")).resize((transformation, transformation))
    turn3 = (Image.open("Assets/Tiles/" + level + "/3.png")).resize((transformation, transformation))
    turn4 = (Image.open("Assets/Tiles/" + level + "/4.png")).resize((transformation, transformation))

    mapIm = Image.new('RGB', (width, height))
    turns = []
    x = start[0]
    y = start[1]

    for i in range(0, width // 256 + 1):
        for j in range(0, height // 256 + 1):
            mapIm.paste(Image.open("Assets/Tiles/" + level + "/42.png"), (i * 256, j * 256))

    if (start[0] == 0):
        if (directions[0] == "r"):
            mapIm.paste(horiz, (x, y), horiz)
            x += transformation
        elif (directions[0] == "u"):
            mapIm.paste(turn4, (x, y), turn4)
            turns.append(Turn(x, y, transformation, False, 4))
            y -= transformation
        elif (directions[0] == "d"):
            mapIm.paste(turn1, (x, y), turn1)
            turns.append(Turn(x, y, transformation, True, 1))
            y += transformation
    elif (start[1] == 0):
        if (directions[0] == "d"):
            mapIm.paste(verti, (x, y), verti)
            y += transformation
        elif (directions[0] == "r"):
            mapIm.paste(turn3, (x, y), turn3)
            turns.append(Turn(x, y, transformation, False, 3))
            x += transformation
        elif (directions[0] == "l"):
            mapIm.paste(turn4, (x, y), turn4)
            turns.append(Turn(x, y, transformation, True, 4))
            x -= transformation

    for i in range(1, len(directions)):
        if (directions[i] == directions[i - 1]):
            if (directions[i] == "u"):
                mapIm.paste(verti, (x, y), verti)
                y -= transformation
            if (directions[i] == "d"):
                mapIm.paste(verti, (x, y), verti)
                y += transformation
            if (directions[i] == "l"):
                mapIm.paste(horiz, (x, y), horiz)
                x -= transformation
            if (directions[i] == "r"):
                mapIm.paste(horiz, (x, y), horiz)
                x += transformation
        else:
            if (directions[i - 1] == "u"):
                if (directions[i] == "l"):
                    mapIm.paste(turn1, (x, y), turn1)
                    turns.append(Turn(x, y, transformation, False, 1))
                    x -= transformation
                elif (directions[i] == "r"):
                    mapIm.paste(turn2, (x, y), turn2)
                    turns.append(Turn(x, y, transformation, True, 2))
                    x += transformation
            elif (directions[i - 1] == "d"):
                if (directions[i] == "l"):
                    mapIm.paste(turn4, (x, y), turn4)
                    turns.append(Turn(x, y, transformation, True, 4))
                    x -= transformation
                elif (directions[i] == "r"):
                    mapIm.paste(turn3, (x, y), turn3)
                    turns.append(Turn(x, y, transformation, False, 3))
                    x += transformation
            elif (directions[i - 1] == "l"):
                if (directions[i] == "u"):
                    mapIm.paste(turn3, (x, y), turn3)
                    turns.append(Turn(x, y, transformation, True, 3))
                    y -= transformation
                elif (directions[i] == "d"):
                    mapIm.paste(turn2, (x, y), turn2)
                    turns.append(Turn(x, y, transformation, False, 2))
                    y += transformation
            elif (directions[i - 1] == "r"):
                if (directions[i] == "u"):
                    mapIm.paste(turn4, (x, y), turn4)
                    turns.append(Turn(x, y, transformation, False, 4))
                    y -= transformation
                elif (directions[i] == "d"):
                    mapIm.paste(turn1, (x, y), turn1)
                    turns.append(Turn(x, y, transformation, True, 1))
                    y += transformation
    mapIm.save("Map/temp.png")
    return turns


class Path():
    def __init__(self, x, y, transformation, asset):
        self.x = x
        self.y = y
        self.asset = pygame.transform.scale(asset, (transformation, transformation))

    def draw(self, win):
        win.blit(self.asset, (self.x, self.y))


class Turn(Path):
    def __init__(self, x, y, transformation, clockwise, section):
        self.x = x
        self.y = y
        #self.asset = pygame.transform.scale(asset, (transformation, transformation))
        self.radius = round(transformation * 75 / 100)
        self.clockwise = clockwise
        self.section = section
        if (section == 1):
            self.circleX = x
            self.circleY = y + transformation
        elif (section == 2):
            self.circleX = x + transformation
            self.circleY = y + transformation
        elif (section == 3):
            self.circleX = x + transformation
            self.circleY = y
        else:
            self.circleX = x
            self.circleY = y

    def isInside(self, x, y):
        if (sqrt((x - self.circleX)**2 + (y - self.circleY)**2) > self.radius):
            return False
        if (self.section == 1 and (x >= self.circleX and y <= self.circleY)):
            return True
        if (self.section == 2 and (x <= self.circleX and y <= self.circleY)):
            return True
        if (self.section == 3 and (x <= self.circleX and y >= self.circleY)):
            return True
        if (self.section == 4 and (x >= self.circleX and y >= self.circleY)):
            return True

        return False
