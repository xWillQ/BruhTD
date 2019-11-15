class Enemy():
    def __init__(self, startX, startY):
        self.posX = startX
        self.posY = startY
        self.velX = 0
        self.velY = 0

    def move(self):
        self.posX += self.velX
        self.posY += self.velY

    def turn(self, direction):
        velocity = abs(self.velX + self.velY)
        if (direction == 0):
            self.velX = velocity
            self.velY = 0
        elif (direction == 90):
            self.velX = 0
            self.velY = -velocity
        elif (direction == 180):
            self.velX = -velocity
            self.velY = 0
        elif (direction == 270):
            self.velX = 0
            self.velY = velocity
