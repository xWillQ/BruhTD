from math import sqrt
import pygame
import os


def loadMap(directions, start, transformation, level):

    horiz = pygame.transform.scale(pygame.image.load(os.path.join("Assets/tiles/forest/8.png")), (transformation, transformation))
    verti = pygame.transform.scale(pygame.image.load(os.path.join("Assets/tiles/forest/6.png")), (transformation, transformation))
    turn1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/tiles/forest/1.png")), (transformation, transformation))
    turn2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/tiles/forest/2.png")), (transformation, transformation))
    turn3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/tiles/forest/3.png")), (transformation, transformation))
    turn4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/tiles/forest/4.png")), (transformation, transformation))

    path = []
    turns = []
    x = start[0]
    y = start[1]

    if (start[0] == 0):
        if (directions[0] == "r"):
            path.append(Path(x, y, transformation, horiz))
            x += transformation
        elif (directions[0] == "u"):
            turns.append(Turn(x, y, transformation, False, 4, turn4))
            y -= transformation
        elif (directions[0] == "d"):
            turns.append(Turn(x, y, transformation, True, 1, turn1))
            y += transformation
    elif (start[1] == 0):
        if (directions[0] == "d"):
            path.append(Path(x, y, transformation, verti))
            y += transformation
        elif (directions[0] == "r"):
            turns.append(Turn(x, y, transformation, False, 3, turn3))
            x += transformation
        elif (directions[0] == "l"):
            turns.append(Turn(x, y, transformation, True, 4, turn4))
            x -= transformation

    for i in range(1, len(directions)):
        if (directions[i] == directions[i - 1]):
            if (directions[i] == "u"):
                path.append(Path(x, y, transformation, verti))
                y -= transformation
            if (directions[i] == "d"):
                path.append(Path(x, y, transformation, verti))
                y += transformation
            if (directions[i] == "l"):
                path.append(Path(x, y, transformation, horiz))
                x -= transformation
            if (directions[i] == "r"):
                path.append(Path(x, y, transformation, horiz))
                x += transformation
        else:
            if (directions[i - 1] == "u"):
                if (directions[i] == "l"):
                    turns.append(Turn(x, y, transformation, False, 1, turn1))
                    x -= transformation
                elif (directions[i] == "r"):
                    turns.append(Turn(x, y, transformation, True, 2, turn2))
                    x += transformation
            elif (directions[i - 1] == "d"):
                if (directions[i] == "l"):
                    turns.append(Turn(x, y, transformation, True, 4, turn4))
                    x -= transformation
                elif (directions[i] == "r"):
                    turns.append(Turn(x, y, transformation, False, 3, turn3))
                    x += transformation
            elif (directions[i - 1] == "l"):
                if (directions[i] == "u"):
                    turns.append(Turn(x, y, transformation, True, 3, turn3))
                    y -= transformation
                elif (directions[i] == "d"):
                    turns.append(Turn(x, y, transformation, False, 2, turn2))
                    y += transformation
            elif (directions[i - 1] == "r"):
                if (directions[i] == "u"):
                    turns.append(Turn(x, y, transformation, False, 4, turn4))
                    y -= transformation
                elif (directions[i] == "d"):
                    turns.append(Turn(x, y, transformation, True, 1, turn1))
                    y += transformation

    return (path, turns)


class Path():
    def __init__(self, x, y, transformation, asset):
        self.x = x
        self.y = y
        self.asset = pygame.transform.scale(asset, (transformation, transformation))

    def draw(self, win):
        win.blit(self.asset, (self.x, self.y))


class Turn(Path):
    def __init__(self, x, y, transformation, clockwise, section, asset):
        self.x = x
        self.y = y
        self.asset = pygame.transform.scale(asset, (transformation, transformation))
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
