from GUI.player import Player
import Mobs.enemies as enemies
import random
from Map.map import loadLevel
from Map.tower import Tower as Tower
import Map.tower as tower


def level_init(level_num):

    level = open("Map/level.txt", "r")
    level_num -= 1
    lines = level.read().splitlines()

    level_map = lines[0 + 4 * (level_num)]
    player_hp = int(lines[1 + 4 * (level_num)])
    player_gold = int(lines[2 + 4 * (level_num)])
    level_theme = str(lines[3 + 4 * (level_num)])

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
    turns, background, start, Idirection = loadLevel(level_map, (0, 250), towers, 0.75, level_theme, 1920, 1080)
    enemies.loadTypes(0.2)
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

    return turns, background, start, Idirection, mobs, player, towers
