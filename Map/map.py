from math import sqrt


def loadMap(directions, start, transformation, level):
    path = []
    turns = []
    x = start[0]
    y = start[1]
    if (start[0] == 0):
        if (directions[0] == "r"):
            asset =  # TODO: Переменной asset присвоить путь к горизонтальному прямому пути
            path.append(Path(x, y, transformation, asset))
            x += transformation
        elif (directions[0] == "u"):
            asset =  # TODO: Переменной asset присвоить путь к повороту 4 секции
            turns.append(Turn(x, y, transformation, False, 4, asset))
            y -= transformation
        elif (directions[0] == "d"):
            asset =  # TODO: Переменной asset присвоить путь к повороту 1 секции
            turns.append(Turn(x, y, transformation, True, 1, asset))
            y += transformation
    elif (start[1] == 0):
        if (directions[0] == "d"):
            asset =   # TODO: Переменной asset присвоить путь к вертикальному прямому пути
            path.append(Path(x, y, transformation, asset))
            y += transformation
        elif (directions[0] == "r"):
            asset =   # TODO: Переменной asset присвоить путь к повороту 3 секции
            turns.append(Turn(x, y, transformation, False, 3, asset))
            x += transformation
        elif (directions[0] == "l"):
            asset =   # TODO: Переменной asset присвоить путь к повороту 4 секции
            turns.append(Turn(x, y, transformation, True, 4, asset))
            x -= transformation
    
    for i in range(1, len(directions)):
        if (directions[i] == directions[i - 1]):
            if (directions[i] == "u"):
                asset =   # TODO: Переменной asset присвоить путь к вертикальному прямому пути
                path.append(Path(x, y, transformation, asset))
                y -= transformation
            if (directions[i] == "d"):
                asset =   # TODO: Переменной asset присвоить путь к вертикальному прямому пути
                path.append(Path(x, y, transformation, asset))
                y += transformation
            if (directions[i] == "l"):
                asset =   # TODO: Переменной asset присвоить путь к горизонтальному прямому пути
                path.append(Path(x, y, transformation, asset))
                x -= transformation
            if (directions[i] == "r"):
                asset =   # TODO: Переменной asset присвоить путь к горизонтальному прямому пути
                path.append(Path(x, y, transformation, asset))
                x += transformation
        else:
            if (directions[i - 1] == "u"):
                if (directions[i] == "l"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 1 секции
                    turns.append(Turn(x, y, transformation, False, 1, asset))
                elif (directions[i] == "r"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 2 секции
                    turns.append(Turn(x, y, transformation, True, 2, asset))
            elif (directions[i - 1] == "d"):
                if (directions[i] == "l"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 4 секции
                    turns.append(Turn(x, y, transformation, True, 4, asset))
                elif (directions[i] == "r"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 3 секции
                    turns.append(Turn(x, y, transformation, False, 3, asset))
            elif (directions[i - 1] == "l"):
                if (directions[i] == "u"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 3 секции
                    turns.append(Turn(x, y, transformation, True, 3, asset))
                elif (directions[i] == "d"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 2 секции
                    turns.append(Turn(x, y, transformation, False, 2, asset))
            elif (directions[i - 1] == "r"):
                if (directions[i] == "u"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 4 секции
                    turns.append(Turn(x, y, transformation, False, 4, asset))
                elif (directions[i] == "d"):
                    asset =   # TODO: Переменной asset присвоить путь к повороту 1 секции
                    turns.append(Turn(x, y, transformation, True, 1, asset))
    
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
