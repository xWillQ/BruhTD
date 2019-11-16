from Enemies.enemies import Enemy
from Map.map import Turn
from time import time
from math import sqrt


mob = Enemy(300, 250)
mob.velX = 10
turn = Turn(500, 300, 100, True)
t1 = time()
while True:
    t2 = time()
    if (t2 - t1 >= 0.25):
        #print(chr(27) + "[2J")
        
        if (sqrt((mob.posX - turn.x)**2 + (mob.posY - turn.y)**2) <= turn.radius):
            mob.turn(turn.x, turn.y, turn.clockwise)
        else:
            mob.move()
        
        print(mob.posX, mob.posY)
        t1 = time()
