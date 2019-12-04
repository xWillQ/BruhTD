from math import sqrt
import pygame
import os


def loadMap(directions, start, transformation, level):

    horiz = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/8.png")), (transformation, transformation))
    verti = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/6.png")), (transformation, transformation))
    turn1 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/1.png")), (transformation, transformation))
    turn2 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/2.png")), (transformation, transformation))
    turn3 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/3.png")), (transformation, transformation))
    turn4 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/4.png")), (transformation, transformation))

    path = []
    turns = []
    x = start[0]
    y = start[1]

    if (start[0] == 0):
        if (directions[0] == "r"):
            asset = horiz
            path.append(Path(x, y, transformation, asset))
            x += transformation
        elif (directions[0] == "u"):
            asset = turn4
            turns.append(Turn(x, y, transformation, False, 4, asset))
            y -= transformation
        elif (directions[0] == "d"):
            asset = turn1
            turns.append(Turn(x, y, transformation, True, 1, asset))
            y += transformation
    elif (start[1] == 0):
        if (directions[0] == "d"):
            asset = verti
            path.append(Path(x, y, transformation, asset))
            y += transformation
        elif (directions[0] == "r"):
            asset = turn3
            turns.append(Turn(x, y, transformation, False, 3, asset))
            x += transformation
        elif (directions[0] == "l"):
            asset = turn4
            turns.append(Turn(x, y, transformation, True, 4, asset))
            x -= transformation

    for i in range(1, len(directions)):
        if (directions[i] == directions[i - 1]):
            if (directions[i] == "u"):
                asset = verti
                path.append(Path(x, y, transformation, asset))
                y -= transformation
            if (directions[i] == "d"):
                asset = verti
                path.append(Path(x, y, transformation, asset))
                y += transformation
            if (directions[i] == "l"):
                asset = horiz
                path.append(Path(x, y, transformation, asset))
                x -= transformation
            if (directions[i] == "r"):
                asset = horiz
                path.append(Path(x, y, transformation, asset))
                x += transformation
        else:
            if (directions[i - 1] == "u"):
                if (directions[i] == "l"):
                    asset = turn1
                    turns.append(Turn(x, y, transformation, False, 1, asset))
                    x -= transformation
                elif (directions[i] == "r"):
                    asset = turn2
                    turns.append(Turn(x, y, transformation, True, 2, asset))
                    x += transformation
            elif (directions[i - 1] == "d"):
                if (directions[i] == "l"):
                    asset = turn4
                    turns.append(Turn(x, y, transformation, True, 4, asset))
                    x -= transformation
                elif (directions[i] == "r"):
                    asset = turn3
                    turns.append(Turn(x, y, transformation, False, 3, asset))
                    x += transformation
            elif (directions[i - 1] == "l"):
                if (directions[i] == "u"):
                    asset = turn3
                    turns.append(Turn(x, y, transformation, True, 3, asset))
                    y -= transformation
                elif (directions[i] == "d"):
                    asset = turn2
                    turns.append(Turn(x, y, transformation, False, 2, asset))
                    y += transformation
            elif (directions[i - 1] == "r"):
                if (directions[i] == "u"):
                    asset = turn4
                    turns.append(Turn(x, y, transformation, False, 4, asset))
                    y -= transformation
                elif (directions[i] == "d"):
                    asset = turn1
                    turns.append(Turn(x, y, transformation, True, 1, asset))
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
        if section == 1:
            self.circleX = x
            self.circleY = y + transformation
        elif section == 2:
            self.circleX = x + transformation
            self.circleY = y + transformation
        elif section == 3:
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