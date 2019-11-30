from math import sqrt


def loadMap(directions, transformation, level):
    pass  # TODO: сделать загрузку карты из массива


class Path():
    def __init__(self, x, y, transformation, asset):
        self.x = x
        self.y = y
        self.asset = asset  # TODO: установить размер transformation по x и y

    def draw(self):
        pass  # TODO: сделать отрисовку текстуры asset на координатах x, y (!!ВАЖНО: не добавлять метод draw в объект Turn!!)


class Turn(Path):
    def __init__(self, x, y, transformation, clockwise, section, asset):
        self.x = x
        self.y = y
        self.asset = asset  # TODO: установить размер transformation по x и y
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
