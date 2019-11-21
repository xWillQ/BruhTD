from math import sqrt


class Turn():
    def __init__(self, x, y, radius, clockwise, startSection, endSection):
        self.x = x
        self.y = y
        self.radius = radius
        self.clockwise = clockwise
        self.startSection = startSection
        self.endSection = endSection

    def isInside(self, x, y):
        if (sqrt((x - self.x)**2 + (y - self.y)**2) > self.radius):
            return False
        if (self.startSection == 1 and (x >= self.x and y <= self.y)):
            return True
        if (self.startSection == 2 and (x <= self.x and y <= self.y)):
            return True
        if (self.startSection == 3 and (x <= self.x and y >= self.y)):
            return True
        if (self.startSection == 4 and (x >= self.x and y >= self.y)):
            return True
        
        if (self.endSection == 1 and (x >= self.x and y <= self.y)):
            return True
        if (self.endSection == 2 and (x <= self.x and y <= self.y)):
            return True
        if (self.endSection == 3 and (x <= self.x and y >= self.y)):
            return True
        if (self.endSection == 4 and (x >= self.x and y >= self.y)):
            return True

        return False
