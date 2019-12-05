from math import sqrt
import pygame
import os

enemyType = {"goblin": {"velocity": 0.75, "hp": 100, "assetsFolder": "", "shiftX": 11, "shiftY": 14}}


class Enemy():
    def __init__(self, startX, startY, direction, transformation, anim_array, typeName):
        self.x = startX
        self.y = startY
        self.velocity = enemyType[typeName]["velocity"]
        self.direction = direction
        self.distance = 0
        self.hp = enemyType[typeName]["hp"]
        self.shiftX = round(-transformation / 2 + (transformation * enemyType[typeName]["shiftX"] / 100))
        self.shiftY = round(-transformation + (transformation * enemyType[typeName]["shiftY"] / 100))
        self.asset = anim_array
        self.anim_c = 0
        #self.asset = pygame.transform.scale(pygame.image.load(os.path.join(asset)), (transformation, transformation))

    def move(self):
        if (self.direction == "u"):
            self.y -= self.velocity
        elif (self.direction == "d"):
            self.y += self.velocity
        elif (self.direction == "l"):
            self.x -= self.velocity
        elif (self.direction == "r"):
            self.x += self.velocity
        self.distance += self.velocity

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
        self.distance += self.velocity
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
        print(self.anim_c)
        if self.anim_c <= 18:
            self.anim_c += 1
            win.blit(pygame.transform.scale(pygame.image.load(os.path.join(self.asset[self.anim_c])), (self.shiftY, self.shiftY)), (self.x - self.shiftX, self.y - self.shiftY))
        else:
            self.anim_c = 0
            win.blit(pygame.transform.scale(pygame.image.load(os.path.join(self.asset[self.anim_c])), (self.shiftY, self.shiftY)), (self.x - self.shiftX, self.y - self.shiftY))
