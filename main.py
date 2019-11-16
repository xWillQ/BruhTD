import pygame
from Enemies.enemies import Enemy
from Map.map import Turn
from time import time

pygame.init()
screen = pygame.display.set_mode([1000, 1000])
mob = Enemy(300, 250)
mob.velX = 4
turn = Turn(500, 300, 100, True, 90, 0)
t1 = time()
f = True
while f:
    t2 = time()
    if (t2 - t1 >= 0.1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = False
        screen.fill((255, 255, 255))
        #print(chr(27) + "[2J")

        if (turn.isInside(mob.posX, mob.posY)):
            mob.turn(turn.x, turn.y, turn.clockwise)
        else:
            mob.move()
        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(turn.x - 5, turn.y - 5, 10, 10))
        pygame.draw.circle(screen, (0, 255, 255), (turn.x, turn.y),
                           turn.radius, 1)
        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(mob.posX, mob.posY, 2, 2))
        print(mob.posX, mob.posY)
        t1 = time()
        pygame.display.flip()
