import pygame
import Mobs.enemies as enemies
import Map.map as map
from time import time
import functions
import random
from Map.tower import Tower


def getY(obj):
    return obj.y


width = 1280
height = 720
pygame.init()
win = pygame.display.set_mode((width, height))
run = True

towers = [
    Tower(100, 280, 0.5),
    Tower(100, 460, 0.5),
    Tower(300, 280, 0.5),
    Tower(300, 460, 0.5),
    Tower(500, 280, 0.5),
    Tower(500, 460, 0.5),
    Tower(700, 280, 0.5),
    Tower(700, 460, 0.5),
    Tower(900, 280, 0.5),
    Tower(900, 460, 0.5),
    Tower(1100, 280, 0.5),
    Tower(1100, 460, 0.5)
]
turns, background, start, initialDirection = map.loadLevel("rrrrrrrrrrrrrrrrr", (0, 300), towers, 0.5, "forest", width, height)
mobs = []
t1 = time()

win.blit(background, (0, 0))
for tower in towers:
    tower.setType("archer")
pygame.display.update()
enemies.loadTypes(0.20)
x = 50
y = 50
for i in range(0, 100):
    t = ""
    transform = 0
    if (random.randint(0, 1) == 0):
        t = "scorpio"
    else:
        t = "wizard"
    if (start[2] == "x"):
        x = random.randint(start[0], start[1])
        y -= 60
    else:
        x -= 60
        y = random.randint(start[0], start[1])
    mobs.append(enemies.Enemy(x, y, initialDirection, t))
    mobs[len(mobs) - 1].distance = x
# ===========================================================================================================
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 20000):
        t1 = time()

        # ===================================   Логика вывода
        #updates = functions.clear(mobs, win, background)  # Очистка экрана от мобов
        updates = functions.clear(towers, win, background)
        #mobsSorted = mobs.copy()
        #mobsSorted.sort(key=getY)

        for i in range(0, len(mobs)):
            updates.append(mobs[i].clear(win, background))
            mobs[i].updatePosition(turns)
            if ((mobs[i].x + enemies.enemyType[mobs[i].typeName]["shiftX"] >= width) or (mobs[i].y + enemies.enemyType[mobs[i].typeName]["shiftX"] >= height)):
                mobs.pop(i)
            elif ((i > 0) and (mobs[i - 1].y > mobs[i].y)):
                mobs[i - 1], mobs[i] = (mobs[i], mobs[i - 1])

        functions.logicLoop(mobs, towers)

        for mob in mobs:
            mob.draw(win)
            if (mob.state == "dead"):
                updates.append(mob.clear(win, background))
                mobs.remove(mob)

        for tower in towers:
            tower.draw(win)

        pygame.display.update(updates)
