from math import sqrt, ceil
import pygame


def loadMap(directions, start, transformation, level, width, height):

    horiz = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/6.png"), (transformation, transformation))
    verti = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/5.png"), (transformation, transformation))
    turn1 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/1.png"), (transformation, transformation))
    turn2 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/2.png"), (transformation, transformation))
    turn3 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/3.png"), (transformation, transformation))
    turn4 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/4.png"), (transformation, transformation))
    back = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/42.png"), (transformation, transformation))

    background = pygame.Surface((width, height))
    turns = []
    x = start[0]
    y = start[1]
    margin = 0.02  # Определяет на каком расстоянии от края дороги будут идти мобы, в процентах от размера дороги

    for i in range(0, ceil(width / transformation)):
        for j in range(0, ceil(height / transformation)):
            background.blit(back, (i * transformation, j * transformation))

    if (start[0] == 0):
        start = (ceil(start[1] + transformation * (0.3085 + margin)), int(start[1] + transformation * (0.6992 - margin)), "y")
        if (directions[0] == "r"):
            background.blit(horiz, (x, y))
            x += transformation
        elif (directions[0] == "u"):
            background.blit(turn4, (x, y))
            turns.append(Turn(x, y, transformation, False, 4))
            y -= transformation
        elif (directions[0] == "d"):
            background.blit(turn1, (x, y))
            turns.append(Turn(x, y, transformation, True, 1))
            y += transformation
    elif (start[1] == 0):
        start = (ceil(start[0] + transformation * (0.3085 + margin)), int(start[0] + transformation * (0.6992 - margin)), "x")
        if (directions[0] == "d"):
            background.blit(verti, (x, y))
            y += transformation
        elif (directions[0] == "r"):
            background.blit(turn3, (x, y))
            turns.append(Turn(x, y, transformation, False, 3))
            x += transformation
        elif (directions[0] == "l"):
            background.blit(turn4, (x, y))
            turns.append(Turn(x, y, transformation, True, 4))
            x -= transformation

    for i in range(1, len(directions)):
        if (directions[i] == directions[i - 1]):
            if (directions[i] == "u"):
                background.blit(verti, (x, y))
                y -= transformation
            if (directions[i] == "d"):
                background.blit(verti, (x, y))
                y += transformation
            if (directions[i] == "l"):
                background.blit(horiz, (x, y))
                x -= transformation
            if (directions[i] == "r"):
                background.blit(horiz, (x, y))
                x += transformation
        else:
            if (directions[i - 1] == "u"):
                if (directions[i] == "l"):
                    background.blit(turn1, (x, y))
                    turns.append(Turn(x, y, transformation, False, 1))
                    x -= transformation
                elif (directions[i] == "r"):
                    background.blit(turn2, (x, y))
                    turns.append(Turn(x, y, transformation, True, 2))
                    x += transformation
            elif (directions[i - 1] == "d"):
                if (directions[i] == "l"):
                    background.blit(turn4, (x, y))
                    turns.append(Turn(x, y, transformation, True, 4))
                    x -= transformation
                elif (directions[i] == "r"):
                    background.blit(turn3, (x, y))
                    turns.append(Turn(x, y, transformation, False, 3))
                    x += transformation
            elif (directions[i - 1] == "l"):
                if (directions[i] == "u"):
                    background.blit(turn3, (x, y))
                    turns.append(Turn(x, y, transformation, True, 3))
                    y -= transformation
                elif (directions[i] == "d"):
                    background.blit(turn2, (x, y))
                    turns.append(Turn(x, y, transformation, False, 2))
                    y += transformation
            elif (directions[i - 1] == "r"):
                if (directions[i] == "u"):
                    background.blit(turn4, (x, y))
                    turns.append(Turn(x, y, transformation, False, 4))
                    y -= transformation
                elif (directions[i] == "d"):
                    background.blit(turn1, (x, y))
                    turns.append(Turn(x, y, transformation, True, 1))
                    y += transformation

    return (turns, background, start)


class Turn():
    def __init__(self, x, y, transformation, clockwise, section):
        self.x = x
        self.y = y
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
