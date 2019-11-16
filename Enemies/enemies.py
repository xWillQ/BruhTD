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
            if (self.posX >= turnX) and (self.posY > turnY):
                currentSection = 1
            elif (self.posX < turnX) and (self.posY >= turnY):
                currentSection = 2
            elif (self.posX <= turnX) and (self.posY < turnY):
                currentSection = 3
            elif (self.posX > turnX) and (self.posY <= turnY):
                currentSection = 4
            if currentSection == 1:
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif currentSection == 2:
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif currentSection == 3:
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif currentSection == 4:
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        else:
            if (self.posX > turnX) and (self.posY >= turnY):
                currentSection = 1
            elif (self.posX <= turnX) and (self.posY > turnY):
                currentSection = 2
            elif (self.posX < turnX) and (self.posY <= turnY):
                currentSection = 3
            elif (self.posX >= turnX) and (self.posY < turnY):
                currentSection = 4
            if currentSection == 1:
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif currentSection == 2:
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif currentSection == 3:
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif currentSection == 4:
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        self.posX = int(self.posX)
        self.posY = int(self.posY)
        