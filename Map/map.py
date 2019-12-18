from math import sqrt, ceil
import pygame


def loadLevel(directions, start, towers, transformation, level, width, height, deco_bg):

    transformation = round(transformation * 256)
    horiz = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/horizontal.png"), (transformation, transformation))
    verti = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/vertical.png"), (transformation, transformation))
    turn1 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/turn1.png"), (transformation, transformation))
    turn2 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/turn2.png"), (transformation, transformation))
    turn3 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/turn3.png"), (transformation, transformation))
    turn4 = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/turn4.png"), (transformation, transformation))
    back = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/background.png"), (transformation, transformation))
    towerPlace = pygame.transform.scale(pygame.image.load("Assets/Tiles/" + level + "/towerPlace.png"), (transformation, transformation))
    GUI = pygame.image.load("Assets/level_decos/interface.png")

    background = pygame.Surface((width, height))
    turns = [Turn(-100, -100, 1, True, 1)]
    x = start[0]
    y = start[1]
    margin = 0.10  # Определяет на каком расстоянии от края дороги будут идти мобы, в процентах от размера дороги
    initialDirection = ""

    for i in range(0, ceil(width / transformation)):
        for j in range(0, ceil(height / transformation)):
            background.blit(back, (i * transformation, j * transformation))

    if (start[0] == 0):
        start = (ceil(start[1] + transformation * (0.3085 + margin)), int(start[1] + transformation * (0.6992 - margin)), "y")
        initialDirection = "r"
        if (directions[0] == "r"):
            background.blit(horiz, (x, y))
            x += transformation
        elif (directions[0] == "u"):
            background.blit(turn4, (x, y))
            turns.append(Turn(x, y, ceil(transformation * 0.75), False, 4))
            y -= transformation
        elif (directions[0] == "d"):
            background.blit(turn1, (x, y))
            turns.append(Turn(x, y + transformation, ceil(transformation * 0.75), True, 1))
            y += transformation
    elif (start[1] == 0):
        start = (ceil(start[0] + transformation * (0.3085 + margin)), int(start[0] + transformation * (0.6992 - margin)), "x")
        initialDirection = "d"
        if (directions[0] == "d"):
            background.blit(verti, (x, y))
            y += transformation
        elif (directions[0] == "r"):
            background.blit(turn3, (x, y))
            turns.append(Turn(x + transformation, y, ceil(transformation * 0.75), False, 3))
            x += transformation
        elif (directions[0] == "l"):
            background.blit(turn4, (x, y))
            turns.append(Turn(x, y, ceil(transformation * 0.75), True, 4))
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
                    if ((turns[len(turns) - 1].x != x) or (turns[len(turns) - 1].y != y + transformation)):
                        turns.append(Turn(x, y + transformation, ceil(transformation * 0.75), False, 1))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 1
                    x -= transformation
                elif (directions[i] == "r"):
                    background.blit(turn2, (x, y))
                    if ((turns[len(turns) - 1].x != x + transformation) or (turns[len(turns) - 1].y != y + transformation)):
                        turns.append(Turn(x + transformation, y + transformation, ceil(transformation * 0.75), True, 2))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 2
                    x += transformation
            elif (directions[i - 1] == "d"):
                if (directions[i] == "l"):
                    background.blit(turn4, (x, y))
                    if ((turns[len(turns) - 1].x != x) or (turns[len(turns) - 1].y != y)):
                        turns.append(Turn(x, y, ceil(transformation * 0.75), True, 4))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 4
                    x -= transformation
                elif (directions[i] == "r"):
                    background.blit(turn3, (x, y))
                    if ((turns[len(turns) - 1].x != x + transformation) or (turns[len(turns) - 1].y != y)):
                        turns.append(Turn(x + transformation, y, ceil(transformation * 0.75), False, 3))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 3
                    x += transformation
            elif (directions[i - 1] == "l"):
                if (directions[i] == "u"):
                    background.blit(turn3, (x, y))
                    if ((turns[len(turns) - 1].x != x + transformation) or (turns[len(turns) - 1].y != y)):
                        turns.append(Turn(x + transformation, y, ceil(transformation * 0.75), True, 3))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 3
                    y -= transformation
                elif (directions[i] == "d"):
                    background.blit(turn2, (x, y))
                    if ((turns[len(turns) - 1].x != x + transformation) or (turns[len(turns) - 1].y != y + transformation)):
                        turns.append(Turn(x + transformation, y + transformation, ceil(transformation * 0.75), False, 2))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 2
                    y += transformation
            elif (directions[i - 1] == "r"):
                if (directions[i] == "u"):
                    background.blit(turn4, (x, y))
                    if ((turns[len(turns) - 1].x != x) or (turns[len(turns) - 1].y != y)):
                        turns.append(Turn(x, y, ceil(transformation * 0.75), False, 4))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 4
                    y -= transformation
                elif (directions[i] == "d"):
                    background.blit(turn1, (x, y))
                    if ((turns[len(turns) - 1].x != x) or (turns[len(turns) - 1].y != y + transformation)):
                        turns.append(Turn(x, y + transformation, ceil(transformation * 0.75), True, 1))
                    else:
                        turns[len(turns) - 1].section = turns[len(turns) - 1].section * 10 + 1
                    y += transformation

    turns.pop(0)

    for tower in towers:
        background.blit(towerPlace, (tower.x - int(transformation / 2), tower.y - int(transformation / 2)))

    background.blit(deco_bg, (0, 0))
    background.blit(GUI, (0, 0))
    return (turns, background, start, initialDirection)


class Turn():
    def __init__(self, x, y, radius, clockwise, section):
        self.x = x
        self.y = y
        self.radius = radius
        self.clockwise = clockwise
        self.section = section

    def isInside(self, x, y):
        if (sqrt((x - self.x)**2 + (y - self.y)**2) > self.radius):
            return False

        if (self.section % 10 == 1 and (x >= self.x and y <= self.y)):
            return True
        if (self.section % 10 == 2 and (x <= self.x and y <= self.y)):
            return True
        if (self.section % 10 == 3 and (x <= self.x and y >= self.y)):
            return True
        if (self.section % 10 == 4 and (x >= self.x and y >= self.y)):
            return True

        if (self.section / 10 == 0):
            return False

        if (self.section // 10 == 1 and (x >= self.x and y <= self.y)):
            return True
        if (self.section // 10 == 2 and (x <= self.x and y <= self.y)):
            return True
        if (self.section // 10 == 3 and (x <= self.x and y >= self.y)):
            return True
        if (self.section // 10 == 4 and (x >= self.x and y >= self.y)):
            return True
        return False
