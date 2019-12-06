import pygame
import Mobs.enemies as enemies
import Map.map as map
from time import time
import functions
import random


width = 1280
height = 720
pygame.init()
win = pygame.display.set_mode((width, height))
run = True

# ===================================   Инициализация переменных, необходимых для обработки уровня
turns, background, start = map.loadMap("drrrddlldrrdruuurrrdddrrruuulluurrrrrr", (1, 0), 120, "forest", width, height)
mobs = []  # Заполняется в ручную или рандомно
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
        for mob in mobs:
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
            mobs.append(enemies.Enemy(x, y, "d", transform, t))
            mobCountdown = 200
        mobCountdown -= 1
        # ================================================

        pygame.display.update(updates)
