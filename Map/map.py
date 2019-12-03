from math import sqrt


def loadMap(directions, start, transformation, level):
    path = []
    turns = []
    x = start[0]
    y = start[1]
    if (start[0] == 0):
        if (directions[0] == "r"):
            path.append(Path(x, y, transformation, True))  # TODO: Заменить True на ассет прямого пути вправо
            x += transformation
        elif (directions[0] == "u"):
            turns.append(Turn(x, y, transformation, False, 4, True))  # TODO: Заменить True на ассет поворота в 4 секции
            y -= transformation
        elif (directions[0] == "d"):
            turns.append(Turn(x, y, transformation, True, 1, True))  # TODO: Заменить второй True на ассет поворота в 1 секции
            y += transformation
    elif (start[1] == 0):
        if (directions[0] == "d"):
            path.append(Path(x, y, transformation, True))  # TODO: Заменить True на ассет прямого пути вниз
            y += transformation
        elif (directions[0] == "r"):
            turns.append(Turn(x, y, transformation, False, 3, True))  # TODO: Заменить True на ассет поворота в 3 секции
            x += transformation
        elif (directions[0] == "l"):
            turns.append(Turn(x, y, transformation, True, 4, True))  # TODO: Заменить второй True на ассет поворота в 4 секции
            x -= transformation
    
    for i in range(1, len(directions)):
        if (directions[i] == directions[i - 1]):
            if (directions[i] == "u"):
                path.append(Path(x, y, transformation, True))  # TODO: Заменить True на ассет прямого пути вниз
                y -= transformation
            if (directions[i] == "d"):
                path.append(Path(x, y, transformation, True))  # TODO: Заменить True на ассет прямого пути вниз
                y += transformation
            if (directions[i] == "l"):
                path.append(Path(x, y, transformation, True))  # TODO: Заменить True на ассет прямого пути вправо
                x -= transformation
            if (directions[i] == "r"):
                path.append(Path(x, y, transformation, True))  # TODO: Заменить True на ассет прямого пути вправо
                x += transformation
        else:
            if (directions[i - 1] == "u"):
                if (directions[i] == "l"):
                    turns.append(Turn(x, y, transformation, False, 1, True))  # TODO: Заменить True на ассет поворота в 1 секции
                elif (directions[i] == "r"):
                    turns.append(Turn(x, y, transformation, True, 2, True))  # TODO: Заменить второй True на ассет поворота в 2 секции
            elif (directions[i - 1] == "d"):
                if (directions[i] == "l"):
                    turns.append(Turn(x, y, transformation, True, 4, True))  # TODO: Заменить второй True на ассет поворота в 4 секции
                elif (directions[i] == "r"):
                    turns.append(Turn(x, y, transformation, False, 3, True))  # TODO: Заменить True на ассет поворота в 3 секции
            elif (directions[i - 1] == "l"):
                if (directions[i] == "u"):
                    turns.append(Turn(x, y, transformation, True, 3, True))  # TODO: Заменить второй True на ассет поворота в 3 секции
                elif (directions[i] == "d"):
                    turns.append(Turn(x, y, transformation, False, 2, True))  # TODO: Заменить True на ассет поворота в 2 секции
            elif (directions[i - 1] == "r"):
                if (directions[i] == "u"):
                    turns.append(Turn(x, y, transformation, False, 4, True))  # TODO: Заменить True на ассет поворота в 4 секции
                elif (directions[i] == "d"):
                    turns.append(Turn(x, y, transformation, True, 1, True))  # TODO: Заменить второй True на ассет поворота в 1 секции


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
