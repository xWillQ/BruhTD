from math import sqrt


class Enemy():
    def __init__(self, startX, startY):
        self.posX = startX
        self.posY = startY
        self.velX = 0
        self.velY = 0

    def move(self):
        self.posX += self.velX
        self.posY += self.velY

    def turn(self, turn):
        velocity = sqrt(self.velX**2 + self.velY**2)
        d = sqrt((self.posX - turn.x)**2 + (self.posY - turn.y)**2)
        a = (2 * (d**2) - velocity**2) / (2 * d)
        h = sqrt(d**2 - a**2)
        x2 = turn.x + a * (self.posX - turn.x) / d
        y2 = turn.y + a * (self.posY - turn.y) / d
        newX1 = x2 + h * (self.posY - turn.y) / d
        newY1 = y2 - h * (self.posX - turn.x) / d
        newX2 = x2 - h * (self.posY - turn.y) / d
        newY2 = y2 + h * (self.posX - turn.x) / d
        if turn.clockwise:
            if (self.posX >= turn.x) and (self.posY < turn.y):
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX < turn.x) and (self.posY <= turn.y):
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX <= turn.x) and (self.posY > turn.y):
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX > turn.x) and (self.posY >= turn.y):
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        else:
            if (self.posX > turn.x) and (self.posY <= turn.y):
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX <= turn.x) and (self.posY < turn.y):
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX < turn.x) and (self.posY >= turn.y):
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX >= turn.x) and (self.posY > turn.y):
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        self.posX = round(self.posX)
        self.posY = round(self.posY)
        if turn.clockwise:
            if turn.endSection == 1:
                self.velX = 0
                self.velY = velocity
            elif turn.endSection == 2:
                self.velX = velocity
                self.velY = 0
            elif turn.endSection == 3:
                self.velX = 0
                self.velY = -velocity
            elif turn.endSection == 4:
                self.velX = -velocity
                self.velY = 0
            else:
                if turn.endSection == 1:
                    self.velX = -velocity
                    self.velY = 0
                elif turn.endSection == 2:
                    self.velX = 0
                    self.velY = velocity
                elif turn.endSection == 3:
                    self.velX = velocity
                    self.velY = 0
                elif turn.endSection == 4:
                    self.velX = 0
                    self.velY = -velocity
