import pygame
import Mobs.enemies as enemies
import Map.map as map
from time import time
import random
import Map.tower as tower


width = 1280
height = 720
pygame.init()
win = pygame.display.set_mode((width, height))
run = True
transformation = 0.5

level = "snow"
enemies.loadTypes(0.2)
tower.loadTypes(0.7, level)
towers = [
    tower.Tower(100, 280),
    tower.Tower(100, 460),
    tower.Tower(300, 280),
    tower.Tower(300, 460),
    tower.Tower(500, 280),
    tower.Tower(500, 460),
    tower.Tower(700, 280),
    tower.Tower(700, 460)
]
turns, background, start, initialDirection = map.loadLevel("rrrrrrdddldrrrrrrr", (0, 300), towers, transformation, level, width, height)
mobs = []
t1 = time()

win.blit(background, (0, 0))
for t in towers:
    t.setType("archer")
    t.upgrade()
    t.upgrade()
pygame.display.update()
x = 50
y = 50
for i in range(0, 30):
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
    if (t2 - t1 >= 1 / 60000):
        t1 = time()

        #win.blit(background, (0, 0))
        updates = tower.clearAll(towers, win, background)
        updates += enemies.clearAll(mobs, win, background)

        enemies.updatePositions(mobs, turns, width, height)

        for t in towers:
            if (t.level == 0):
                continue
            if (t.isReady()):
                for m in mobs:
                    if (t.isInside(m.x, m.y) and m.state != "dying" and m.state != "dead"):
                        t.attack(m)
                        m.hurt(t.damage)
                        break
            else:
                t.reduceCooldown()

        for mob in mobs:
            if (mob.state == "dead"):
                mobs.remove(mob)
            else:
                mob.draw(win)

        for t in towers:
            t.draw(win)

        pygame.display.update(updates)
