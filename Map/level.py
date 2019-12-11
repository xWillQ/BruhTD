import pygame
import os
from Map.map import loadLevel
from GUI.button import Button
from GUI.button import isInside
import Mobs.enemies as enemies
from Map.tower import Tower as Tower
import Map.tower as tower
import random
import G
from GUI.player import Player as player

player = player(20, 1000)
player.alive = True

pygame.font.init()
font = pygame.font.Font('bruh_font.otf', 32)

tower.loadTypes(1 * 0.8, 'forest')
towers = [Tower(470, 300), Tower(865, 410), Tower(1250, 300), Tower(1600, 410), Tower(1650, 660), Tower(1650, 800)]

death_button = Button(15, 325, 40, pygame.image.load(os.path.join('Assets/GUI/interface_game/skull.png')))
lvl1 = "rurrddrruurrddrrddllllllldd"
turns, background, start, Idirection = loadLevel(lvl1, (0, 250), towers, 0.75, "forest", 1920, 1080)


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


def draw():

    if G.level_number == 1:

        playerHealth = font.render(str(player.hp), True, (255, 0, 0), 0)
        playerGold = font.render(str(player.gold), True, (255, 255, 0), 0)

        updates = tower.clearAll(towers, G.win, background)
        updates += enemies.clearAll(mobs, G.win, background)

        G.win.blit(background, (0, 0))

        if G.event.type is pygame.MOUSEBUTTONUP and G.wave_trigger is False:
            mouse_pos = pygame.mouse.get_pos()
            if G.condition == 10:
                if isInside(mouse_pos[0], mouse_pos[1], 15 + 20, 325 + 20, 50) is True:
                    G.wave_trigger = True

        if G.wave_trigger is False:
            death_button.draw(G.win)

        if G.wave_trigger is True:

            enemies.updatePositions(mobs, turns, 1920, 1080, player)

            for i in range(len(towers)):
                if towers[i].level == 0:
                    continue
                if towers[i].isReady():
                    for j in range(len(mobs)):
                        if (towers[i].isInside(mobs[j].x, mobs[j].y) and mobs[j].state != "dying" and mobs[j].state != "dead"):
                            towers[i].attack(mobs[j])
                            mobs[j].hurt(towers[i].damage)
                            break
                else:
                    towers[i].reduceCooldown()

            for mob in mobs:
                if (mob.state == "dead"):
                    mobs.remove(mob)
                    player.gold_add(mob)
                else:
                    mob.draw(G.win)

        if G.event.type is pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(towers)):
                if isInside(mouse_pos[0], mouse_pos[1], towers[i].x, towers[i].y, 120):
                    towers[i].gui_opened = True
                    Tower.gui_close(towers, i)

                if towers[i].gui_opened:
                    Tower.gui_level_up(towers[i], player, mouse_pos)
                    Tower.gui_type_change(towers[i], player, mouse_pos)

        for i in range(len(towers)):
            if towers[i].level != 0:
                pygame.draw.circle(G.win, (0, 55, 255), (towers[i].x, towers[i].y), round(towers[i].radius), 1)
                towers[i].draw(G.win)
            if towers[i].gui_opened is True:
                Tower.draw_gui(towers[i])

        if player.hp <= 0:
            player.alive = False
            G.condition = 2
            G.level_number = 0

        if len(mobs) == 0 and player.hp > 0:
            player.alive = False
            G.condition = 3
            G.level_number = 0

        G.win.blit(playerHealth, (15, 1000))
        G.win.blit(playerGold, (15, 1030))
        pygame.display.update(updates)

    print("yes")
    G.event = G.event_N
    # print(player.gold)
    print(len(mobs))
