from math import sqrt
import pygame


enemyType = {"scorpio": {"velocity": 1.5, "hp": 70, "shiftX": 0.07, "shiftY": 0.14, "reward": 3},
             "wizard": {"velocity": 1, "hp": 150, "shiftX": 0.17, "shiftY": 0.13, "reward": 5}}

frameLength = 3


def loadTypes(transformation):
    for t in enemyType:
        exampleAsset = pygame.image.load("Assets/Mobs/" + t + "/walk_000.png")
        enemyType[t]["width"] = round(transformation * exampleAsset.get_width())
        enemyType[t]["height"] = round(transformation * exampleAsset.get_height())
        enemyType[t]["shiftX"] = round(-enemyType[t]["width"] / 2 + (enemyType[t]["width"] * enemyType[t]["shiftX"]))
        enemyType[t]["shiftY"] = round(-enemyType[t]["height"] + (enemyType[t]["height"] * enemyType[t]["shiftY"]))
        enemyType[t]["walking"] = []
        for i in range(0, 20):
            enemyType[t]["walking"].append(pygame.transform.scale(pygame.image.load("Assets/Mobs/" + t + "/walk_" + (3 - len(str(i))) * "0" + str(i) + ".png"), (enemyType[t]["width"], enemyType[t]["height"])))

        enemyType[t]["dying"] = []
        for i in range(0, 20):
            enemyType[t]["dying"].append(pygame.transform.scale(pygame.image.load("Assets/Mobs/" + t + "/die_" + (3 - len(str(i))) * "0" + str(i) + ".png"), (enemyType[t]["width"], enemyType[t]["height"])))

        enemyType[t]["hurt"] = []
        for i in range(0, 20):
            enemyType[t]["hurt"].append(pygame.transform.scale(pygame.image.load("Assets/Mobs/" + t + "/hurt_" + (3 - len(str(i))) * "0" + str(i) + ".png"), (enemyType[t]["width"], enemyType[t]["height"])))


def clearAll(mobs, win, background):
    cleared = []
    for mob in mobs:
        currX = mob.x + enemyType[mob.typeName]["shiftX"]
        currY = mob.y + enemyType[mob.typeName]["shiftY"]
        cleared.append(pygame.Rect(int(currX), int(currY), enemyType[mob.typeName]["width"] + 1, enemyType[mob.typeName]["height"] + 1))
        win.blit(background, (currX, currY), cleared[len(cleared) - 1])
    return cleared


def updatePositions(mobs, turns, width, height, player):
    length = len(mobs)
    i = 0
    while (i < length):
        if ((mobs[i].state == "walking") or (mobs[i].state == "hurt")):
            turned = False
            for turn in turns:
                if (turn.isInside(mobs[i].x, mobs[i].y)):
                    mobs[i].turn(turn)
                    turned = True
                    break
            if (not turned):
                mobs[i].move()
        if ((mobs[i].x + enemyType[mobs[i].typeName]["shiftX"] * 2 >= width) or (mobs[i].y + enemyType[mobs[i].typeName]["shiftX"] * 2 >= height)):
            mobs.pop(i)
            player.hp -= 1
            length -= 1
        elif ((i > 0) and (mobs[i - 1].y > mobs[i].y)):
            mobs[i - 1], mobs[i] = (mobs[i], mobs[i - 1])
        i += 1


class Enemy():
    def __init__(self, startX, startY, direction, typeName):
        self.x = startX
        self.y = startY
        self.velocity = enemyType[typeName]["velocity"]
        self.direction = direction
        self.distance = 0
        self.hp = enemyType[typeName]["hp"]
        self.state = "walking"
        self.typeName = typeName
        self.frame = 0
        self.reward = enemyType[typeName]["reward"]

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
        d = sqrt((self.x - turn.x)**2 + (self.y - turn.y)**2)
        a = (2 * (d**2) - self.velocity**2) / (2 * d)
        h = sqrt(d**2 - a**2)
        x2 = turn.x + a * (self.x - turn.x) / d
        y2 = turn.y + a * (self.y - turn.y) / d
        newX1 = x2 + h * (self.y - turn.y) / d
        newY1 = y2 - h * (self.x - turn.x) / d
        newX2 = x2 - h * (self.y - turn.y) / d
        newY2 = y2 + h * (self.x - turn.x) / d
        if (turn.clockwise):
            if (self.x >= turn.x) and (self.y < turn.y):
                if (newX1 > newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x < turn.x) and (self.y <= turn.y):
                if (newY1 < newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x <= turn.x) and (self.y > turn.y):
                if (newX1 < newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x > turn.x) and (self.y >= turn.y):
                if (newY1 > newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
        else:
            if (self.x > turn.x) and (self.y <= turn.y):
                if (newY1 < newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x <= turn.x) and (self.y < turn.y):
                if (newX1 < newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x < turn.x) and (self.y >= turn.y):
                if (newY1 > newY2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
            elif (self.x >= turn.x) and (self.y > turn.y):
                if (newX1 > newX2):
                    self.x = newX1
                    self.y = newY1
                else:
                    self.x = newX2
                    self.y = newY2
        self.distance += self.velocity
        if (turn.clockwise):
            if (turn.section % 10) == 1:
                self.direction = "d"
            elif (turn.section % 10) == 2:
                self.direction = "r"
            elif (turn.section % 10) == 3:
                self.direction = "u"
            elif (turn.section % 10) == 4:
                self.direction = "l"
        else:
            if (turn.section % 10) == 1:
                self.direction = "l"
            elif (turn.section % 10) == 2:
                self.direction = "d"
            elif (turn.section % 10) == 3:
                self.direction = "r"
            elif (turn.section % 10) == 4:
                self.direction = "u"

    def hurt(self, damage):
        self.hp -= damage
        if (self.hp <= 0):
            self.die()
            return
        if (self.state != "hurt"):
            self.state = "hurt"
            self.velocity *= 0.4    # Скорость при получении урона
            self.frame = 0

    def die(self):
        self.state = "dying"
        self.velocity = 0
        self.frame = 0

    def draw(self, win):
        win.blit(enemyType[self.typeName][self.state][self.frame // frameLength], (self.x + enemyType[self.typeName]["shiftX"], self.y + enemyType[self.typeName]["shiftY"]))
        self.frame += 1
        if (self.frame >= 19 * frameLength):
            if (self.state == "hurt"):
                self.state = "walking"
                self.velocity = enemyType[self.typeName]["velocity"]
            elif (self.state == "dying"):
                # self.frame -= 1
                self.state = "dead"
                return
            self.frame = 0
