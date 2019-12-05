from math import sqrt
import pygame


class Enemy():
    def __init__(self, startX, startY, transformation, asset):
        self.x = startX
        self.y = startY
        self.velocity = 0
        self.direction = ""
        self.hp = 100
        self.asset = pygame.transform.scale(asset, (transformation, transformation))
        self.shiftX = round(transformation / 2)
        self.shiftY = transformation

    def move(self):
        if (self.direction == "u"):
            self.y -= self.velocity
        elif (self.direction == "d"):
            self.y += self.velocity
        elif (self.direction == "l"):
            self.x -= self.velocity
        elif (self.direction == "r"):
            self.x += self.velocity

    def turn(self, turn):
        d = sqrt((self.x - turn.circleX)**2 + (self.y - turn.circleY)**2)
        a = (2 * (d**2) - self.velocity**2) / (2 * d)
        h = sqrt(d**2 - a**2)
        x2 = turn.circleX + a * (self.x - turn.circleX) / d
        y2 = turn.circleY + a * (self.y - turn.circleY) / d
        newX1 = x2 + h * (self.y - turn.circleY) / d
        newY1 = y2 - h * (self.x - turn.circleX) / d
        newX2 = x2 - h * (self.y - turn.circleY) / d
        newY2 = y2 + h * (self.x - turn.circleX) / d
        if (turn.clockwise):
            if (self.x >= turn.circleX) and (self.y < turn.circleY):
                if (newX1 > newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x < turn.circleX) and (self.y <= turn.circleY):
                if (newY1 < newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x <= turn.circleX) and (self.y > turn.circleY):
                if (newX1 < newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x > turn.circleX) and (self.y >= turn.circleY):
                if (newY1 > newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
        else:
            if (self.x > turn.circleX) and (self.y <= turn.circleY):
                if (newY1 < newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x <= turn.circleX) and (self.y < turn.circleY):
                if (newX1 < newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x < turn.circleX) and (self.y >= turn.circleY):
                if (newY1 > newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x >= turn.circleX) and (self.y > turn.circleY):
                if (newX1 > newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
        self.x = round(self.x)
        self.y = round(self.y)
        if (turn.clockwise):
            if (turn.section) == 1:
                self.direction = "d"
            elif (turn.section) == 2:
                self.direction = "r"
            elif (turn.section) == 3:
                self.direction = "u"
            elif (turn.section) == 4:
                self.direction = "l"
        else:
            if (turn.section) == 1:
                self.direction = "l"
            elif (turn.section) == 2:
                self.direction = "d"
            elif (turn.section) == 3:
                self.direction = "r"
            elif (turn.section) == 4:
                self.direction = "u"

    def draw(self, win):
        win.blit(self.asset, ((self.x - self.shiftX), (self.y - self.shiftY)))
