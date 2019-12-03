from math import sqrt
import pygame


class Enemy():
    def __init__(self, startX, startY, transformation, asset):
        self.posX = startX
        self.posY = startY
        self.velX = 0
        self.velY = 0
        self.hp = 100
        self.asset = pygame.transform.scale(asset, (transformation, transformation))
        self.shiftX = round(transformation / 2)
        self.shiftY = transformation

    def move(self):
        self.posX += self.velX
        self.posY += self.velY

    def turn(self, turn):
        velocity = sqrt(self.velX**2 + self.velY**2)
        d = sqrt((self.posX - turn.circleX)**2 + (self.posY - turn.circleY)**2)
        a = (2 * (d**2) - velocity**2) / (2 * d)
        h = sqrt(d**2 - a**2)
        x2 = turn.circleX + a * (self.posX - turn.circleX) / d
        y2 = turn.circleY + a * (self.posY - turn.circleY) / d
        newX1 = x2 + h * (self.posY - turn.circleY) / d
        newY1 = y2 - h * (self.posX - turn.circleX) / d
        newX2 = x2 - h * (self.posY - turn.circleY) / d
        newY2 = y2 + h * (self.posX - turn.circleX) / d
        if turn.clockwise:
            if (self.posX >= turn.circleX) and (self.posY < turn.circleY):
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX < turn.circleX) and (self.posY <= turn.circleY):
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX <= turn.circleX) and (self.posY > turn.circleY):
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX > turn.circleX) and (self.posY >= turn.circleY):
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        else:
            if (self.posX > turn.circleX) and (self.posY <= turn.circleY):
                if newY1 < newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX <= turn.circleX) and (self.posY < turn.circleY):
                if newX1 < newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX < turn.circleX) and (self.posY >= turn.circleY):
                if newY1 > newY2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
            elif (self.posX >= turn.circleX) and (self.posY > turn.circleY):
                if newX1 > newX2:
                    self.posX = newX1
                    self.posY = newY1
                else:
                    self.posX = newX2
                    self.posY = newY2
        self.posX = round(self.posX)
        self.posY = round(self.posY)
        if turn.clockwise:
            if turn.section == 1:
                self.velX = 0
                self.velY = velocity
            elif turn.section == 2:
                self.velX = velocity
                self.velY = 0
            elif turn.section == 3:
                self.velX = 0
                self.velY = -velocity
            elif turn.section == 4:
                self.velX = -velocity
                self.velY = 0
        else:
            if turn.section == 1:
                self.velX = -velocity
                self.velY = 0
            elif turn.section == 2:
                self.velX = 0
                self.velY = velocity
            elif turn.section == 3:
                self.velX = velocity
                self.velY = 0
            elif turn.section == 4:
                self.velX = 0
                self.velY = -velocity

    def draw(self, win):
        win.blit(self.asset, ((self.posX - self.shiftX), (self.posY - self.shiftY)))
