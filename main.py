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

# ===================================   Инициализация переменных, необходимых для обработки уровня
towers = []
turns, background, start, initialDirection = map.loadLevel("drrrdlldrrdruurrrddrruuur", (10, 0), towers, 0.5, "forest", width, height)
mobs = []  # Заполняется вручную или рандомно
t1 = time()
mobCountdown = 0  # Обратный отсчёт до спавна моба
# ================================================================================================

win.blit(background, (0, 0))
pygame.display.update()
#towers[0].setType("archer")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 100000):
        t1 = time()

        # ===================================   Логика вывода
        functions.logicLoop(mobs, turns)  # Перемещение мобов, позже сюда надо добавить получение урона и смэрт
        updates = functions.clear(mobs, win, background)  # Очистка экрана от мобов
        #mobsSorted = mobs.copy()
        #mobsSorted.sort(key=getY)
        for mob in mobs:
            if ((mob.x + mob.shiftX >= width) or (mob.y + mob.shiftY >= height)):  # Удаление моба, если он за пределами экрана
                mobs.remove(mob)
            else:
                mob.draw(win)
                #pygame.draw.circle(win, (255, 0, 0), (round(mob.x), round(mob.y)), 1)

        #for tower in towers:
        #    tower.draw(win)

        # ==================================   Спаун мобов
        if (mobCountdown == 0):
            t = ""
            x = 0
            y = 0
            transform = 0
            if (random.randint(0, 1) == 0):
                t = "scorpio"
                transform = 0.1327
            else:
                t = "wizard"
                transform = 0.20
            if (start[2] == "x"):
                x = random.randint(start[0], start[1])
                y = 0
            else:
                x = -15
                y = random.randint(start[0], start[1])
            mobs.append(enemies.Enemy(x, y, initialDirection, transform, t))
            mobCountdown = 100
        mobCountdown -= 1
        # ================================================
        #for turn in turns:
        #    pygame.draw.circle(win, (255, 0, 0), (turn.x, turn.y), turn.radius, 1)
        pygame.display.update(updates)
