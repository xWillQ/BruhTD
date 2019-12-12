import pygame
from GUI.button import Button
from GUI.button import isInside
import Mobs.enemies as enemies
from Map.tower import Tower as Tower
import Map.tower as tower
import G

pygame.font.init()
font = pygame.font.Font('bruh_font.ttf', 36)
death_button = Button(15, 325, 40, pygame.image.load('Assets/GUI/interface_game/skull.png'))


def draw(turns, background, start, Idirection, mobs, player, towers):

    playerHealth = font.render(str(player.hp), True, (255, 0, 0), 0)
    playerGold = font.render(str(player.gold), True, (255, 255, 0), 0)
    playerMana = font.render(str(player.mana), True, (0, 0, 255), 0)

    G.win.blit(background, (0, 950), pygame.Rect(0, 950, 110, 180))
    G.win.blit(background, (0, 900), pygame.Rect(0, 900, 100, 100))
    G.win.blit(background, (15, 325), pygame.Rect(15, 325, 40, 40))

    mouse_pos = pygame.mouse.get_pos()
    updates = tower.clearAll(towers, G.win, background)
    updates += enemies.clearAll(mobs, G.win, background)

    if G.event.type is pygame.MOUSEBUTTONUP and G.wave_trigger is False:
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
                player.mana += 4
            else:
                mob.draw(G.win)

    if G.event.type is pygame.MOUSEBUTTONUP:
        for i in range(len(towers)):
            if isInside(mouse_pos[0], mouse_pos[1], towers[i].x, towers[i].y, 120):
                towers[i].gui_opened = True
                Tower.gui_close(towers, i)
            if towers[i].gui_opened:
                Tower.gui_level_up(towers[i], player, mouse_pos)
                Tower.gui_type_change(towers[i], player, mouse_pos)

    for i in range(len(towers)):
        if towers[i].level != 0:
            # pygame.draw.circle(G.win, (0, 55, 255), (towers[i].x, towers[i].y), round(towers[i].radius), 1)
            towers[i].draw(G.win)
        if towers[i].gui_opened is True:
            Tower.draw_gui(towers[i])
        if player.hp <= 0 and towers[i].level != 0:
            towers[i].level = 0

    if player.hp <= 0:
        G.condition = 2
        G.level_number = 0
        G.online = False
        G.wave_trigger = False

    if len(mobs) == 0 and player.hp > 0:
        G.condition = 3
        G.level_number = 0
        G.online = False
        G.wave_trigger = False

    if G.event.type is pygame.MOUSEBUTTONUP:
        if isInside(mouse_pos[0], mouse_pos[1], 30, 900, 100):
            if player.casting is False:
                player.casting = True

    if player.casting is True:
        if G.event.type is pygame.MOUSEBUTTONUP:
            player.spell(mouse_pos, mobs, player)
            updates += player.spell(mouse_pos, mobs, player)

    G.win.blit(playerHealth, (25, 970))
    G.win.blit(playerGold, (25, 1010))
    G.win.blit(playerMana, (25, 910))

    pygame.display.update(updates)
    print(player.casting)
    G.event = G.event_N
