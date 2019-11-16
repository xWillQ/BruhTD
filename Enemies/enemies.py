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

    def turn(self, turnX, turnY, clockwise):
        velocity = sqrt(self.velX**2 + self.velY**2)
        d = sqrt((self.posX - turnX)**2 + (self.posY - turnY)**2)
        a = (2 * (d**2) - velocity**2) / (2 * d)
        h = sqrt(d**2 - a**2)
        x2 = turnX + a * (self.posX - turnX) / d
        y2 = turnY + a * (self.posY - turnY) / d
        newX1 = x2 + h * (self.posY - turnY) / d
        newY1 = y2 - h * (self.posX - turnX) / d
        newX2 = x2 - h * (self.posY - turnY) / d
        newY2 = y2 + h * (self.posX - turnX) / d
        if clockwise:
            if (self.posX >= turnX) and (self.posY < turnY):
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX < turnX) and (self.posY <= turnY):
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX <= turnX) and (self.posY > turnY):
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX > turnX) and (self.posY >= turnY):
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        else:
            if (self.posX > turnX) and (self.posY <= turnY):
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX <= turnX) and (self.posY < turnY):
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX < turnX) and (self.posY >= turnY):
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX >= turnX) and (self.posY > turnY):
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        self.posX = round(self.posX)
        self.posY = round(self.posY)
