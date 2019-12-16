from GUI.player import Player
import Mobs.enemies as enemies
import random
from Map.map import loadLevel
from Map.tower import Tower as Tower
import Map.tower as tower
import pygame
import G

enemies.loadTypes(0.2)


def wave_create(start, Idirection):
    x = 50
    y = 50
    mobs = []
    for i in range(0, 20):
        t = ""
        if (random.randint(0, 1) == 0):
            t = "scorpio"
        else:
            t = "wizard"
        if (start[2] == "x"):
            x = random.randint(start[0], start[1])
            y -= 60
        else:
            x -= 80
            y = random.randint(start[0], start[1])
        mobs.append(enemies.Enemy(x, y, Idirection, t))
        mobs[len(mobs) - 1].distance = x

    return mobs


def level_init(level_num):

    deco_bg = pygame.image.load("Assets/level_decos/level_" + str(level_num) + ".png")
    level = open("Map/level.txt", "r")
    level_num -= 1
    lines = level.read().splitlines()

    level_map = lines[0 + 6 * (level_num)]
    player_hp = int(lines[1 + 6 * (level_num)])
    player_gold = int(lines[2 + 6 * (level_num)])
    level_theme = str(lines[3 + 6 * (level_num)])
    SposX = int(lines[4 + 6 * (level_num)])
    SposY = int(lines[5 + 6 * (level_num)])

    Spos = [SposX, SposY]
    level_num += 1
    towers = []
    tower_positions = open("tower_codes/towers" + str(level_num) + ".txt", "r")
    tower_pos_arr = tower_positions.readlines()
    i = 0
    while i <= len(tower_pos_arr) - 2:
        towers.append(Tower(int(tower_pos_arr[i]), int(tower_pos_arr[i + 1])))
        i += 2

    player = Player(int(player_hp), int(player_gold))
    tower.loadTypes(1 * 0.8, level_theme)
    turns, background, start, Idirection = loadLevel(level_map, (Spos), towers, 0.75, level_theme, 1920, 1080, deco_bg)
    mobs = wave_create(start, Idirection)
    G.win.blit(background, (0, 0))
    G.wave_trigger = False
    return turns, background, start, Idirection, mobs, player, towers, deco_bg
