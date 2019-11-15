from Enemies.enemies import Enemy
from Map.map import Turn
from time import time

mob = Enemy(0, 0)
mob.velX = 2
turns = [
    Turn(50, 0, 10, 10, 270),
    Turn(50, 45, 10, 10, 0),
    Turn(150, 45, 10, 10, 90),
    Turn(150, 0, 10, 10, 180)
]
t1 = time()
while True:
    t2 = time()
    if (t2 - t1 >= 0.5):
        #print(chr(27) + "[2J")
        for turn in turns:
            if ((mob.posX >= turn.x and mob.posX <= turn.x + turn.lengthX) and (mob.posY >= turn.y and mob.posY <= turn.y + turn.lengthY)):
                mob.turn(turn.direction)

        mob.move()
        print(mob.posX, mob.posY)
        t1 = time()
