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

enemies.loadTypes(0.2)
tower.loadTypes(0.7, "forest")
towers = [
    tower.Tower(100, 280),
    tower.Tower(100, 460),
    tower.Tower(300, 280),
    tower.Tower(300, 460),
    tower.Tower(500, 280),
    tower.Tower(500, 460),
    tower.Tower(700, 280),
    tower.Tower(700, 460),
    # Tower(900, 280),
    # Tower(900, 460),
    # Tower(1100, 280),
    # Tower(1100, 460)
]
turns, background, start, initialDirection = map.loadLevel("rrrrrrdddldrrrrrrr", (0, 300), towers, transformation, "forest", width, height)
mobs = []
t1 = time()

win.blit(background, (0, 0))
for t in towers:
    t.setType("archer")
towers[3].upgrade()
towers[3].upgrade()
towers[2].upgrade()
pygame.display.update()
x = 50
y = 50
for i in range(0, 50):
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
    if (t2 - t1 >= 1 / 2000):
        t1 = time()

        updates = tower.clearAll(towers, win, background)
        updates += enemies.clearAll(mobs, win, background)

        enemies.updatePositions(mobs, turns, width, height)

        for t in towers:
            if (t.level == 0):
                continue
            if (t.isReady()):
                for m in mobs:
                    if (t.isInside(m.x, m.y) and m.state != "dying" and m.state != "dead"):
                        t.attack()
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
            t.draw(win, "forest")

        pygame.display.update(updates)
