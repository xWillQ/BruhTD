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
towers = [Tower(200, 100, 120)]
turns, background, start, initialDirection = map.loadLevel("drrrddlldrrdruuurrrdddrrruuulluurrrrrr", (10, 0), towers, 120, "forest", width, height)
mobs = []  # Заполняется вручную или рандомно
t1 = time()
mobCountdown = 0  # Обратный отсчёт до спавна моба
# ================================================================================================

win.blit(background, (0, 0))
pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2 = time()
    if (t2 - t1 >= 1 / 200):
        t1 = time()

        # ===================================   Логика вывода
        functions.logicLoop(mobs, turns)  # Перемещение мобов, позже сюда надо добавить получение урона и смэрт
        updates = functions.clear(mobs, win, background)  # Очистка экрана от мобов
        mobsSorted = mobs.copy()
        mobsSorted.sort(key=getY)
        for mob in mobsSorted:
            if ((mob.x + mob.shiftX >= width) or (mob.y + mob.shiftY >= height)):  # Удаление моба, если он за пределами экрана
                mobs.remove(mob)
            else:
                mob.draw(win)

        # ==================================   Спаун мобов
        if (mobCountdown == 0):
            t = ""
            x = 0
            y = 0
            transform = 0
            if (random.randint(0, 1) == 0):
                t = "scorpio"
                transform = 30
            else:
                t = "wizard"
                transform = 60
            if (start[2] == "x"):
                x = random.randint(start[0], start[1])
                y = -15
            else:
                x = -15
                y = random.randint(start[0], start[1])
            mobs.append(enemies.Enemy(x, y, initialDirection, transform, t))
            mobCountdown = 200
        mobCountdown -= 1
        # ================================================
        for turn in turns:
            pygame.draw.circle(win, (255, 0, 0), (turn.x, turn.y), turn.radius, 1)
        pygame.display.update()
