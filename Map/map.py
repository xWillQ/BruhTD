from math import sqrt


class Turn():
    """Структура для хранения данных о повороте"""
    def __init__(self, x, y, radius, clockwise, startDeg, lengthDeg):
        self.x = x
        self.y = y
        self.radius = radius
        self.clockwise = clockwise
        self.startDeg = startDeg
        self.lengthDeg = lengthDeg

    def isInside(self, x, y):
        if (sqrt((x - self.x)**2 + (y - self.y)**2) > self.radius):
            return False
                
        return True
