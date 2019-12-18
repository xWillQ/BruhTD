import pygame
from GUI.button import isInside
import Mobs.enemies as enemies
from Map.tower import Tower as Tower
import Map.tower as tower
import G

pygame.font.init()
font = pygame.font.Font('bruh_font.ttf', 30)
death_button = pygame.transform.scale(pygame.image.load('Assets/GUI/interface_game/skull.png'), (40, 40))


def draw(turns, background, Idirection, mobs, player, towers, sposX, sposY):

    updates = tower.clearAll(towers, G.win, background)
    updates += enemies.clearAll(mobs, G.win, background)

    playerHealth = font.render(str(player.hp), True, (255, 0, 0), 0)
    playerGold = font.render(str(player.gold), True, (255, 255, 0), 0)
    playerMana = font.render(str(player.mana), True, (0, 0, 255), 0)

    G.win.blit(background, (0, 0), pygame.Rect(0, 0, 200, 150))
    if Idirection == "r":
        G.win.blit(background, (sposX + 15, sposY + 75), pygame.Rect(sposX + 15, sposY + 75, 40, 40))
    if Idirection == "d":
        G.win.blit(background, (sposX + 60, sposY + 15), pygame.Rect(sposX + 70, sposY + 15, 40, 40))

    mouse_pos = pygame.mouse.get_pos()

    if G.event.type is pygame.MOUSEBUTTONUP:
        if isInside(mouse_pos[0], mouse_pos[1], 1850, 65, 110) is True:
            G.condition = 1
            G.level_number = 0
            G.online = False
            G.wave_trigger = False

    if G.event.type is pygame.MOUSEBUTTONUP:
        if isInside(mouse_pos[0], mouse_pos[1], 1850, 195, 110) is True:
            if player.mana - 20 >= 0:
                player.mana -= 20
                player.freeze_casted = True

    if G.event.type is pygame.MOUSEBUTTONUP:
        if isInside(mouse_pos[0], mouse_pos[1], 1850, 440, 110) is True:
            if player.mana - 20 >= 0:
                player.mana -= 20
                player.pu_casted = True

    if player.freeze_casted is True:
        player.freeze_ticker()

    if player.pu_casted is True:
        player.power_up_ticker()

    if G.event.type is pygame.MOUSEBUTTONUP and G.wave_trigger is False:
        if G.condition == 10:
            if Idirection == "r":
                if isInside(mouse_pos[0], mouse_pos[1], sposX + 15 + 20, sposY + 75 + 20, 50) is True:
                    G.wave_trigger = True
            if Idirection == "d":
                if isInside(mouse_pos[0], mouse_pos[1], sposX + 60 + 20, sposY + 15 + 20, 50) is True:
                    G.wave_trigger = True

    if G.wave_trigger is False:
        if Idirection == "r":
            G.win.blit(death_button, (sposX + 15, sposY + 75))
        if Idirection == "d":
            G.win.blit(death_button, (sposX + 60, sposY + 15))

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

            if player.freeze_casted is True:
                mob.velocity = 0.0
            else:
                player.freeze_cancel(mob)

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
            if player.pu_casted is True:
                player.power_up(towers[i])
            else:
                player.pu_cancel(towers[i])

        if towers[i].level != 0:
            # pygame.draw.circle(G.win, (0, 55, 255), (towers[i].x, towers[i].y), round(towers[i].radius), 1)
            print(towers[i].damage)
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
        if isInside(mouse_pos[0], mouse_pos[1], 1850, 310, 110):
            if player.casting is False:
                player.casting = True

    if player.casting is True:
        if G.event.type is pygame.MOUSEBUTTONUP:
            player.spell(mouse_pos, mobs, player)

    G.win.blit(playerHealth, (25, 10))
    G.win.blit(playerGold, (25, 40))
    G.win.blit(playerMana, (25, 70))
    print(mouse_pos)
    pygame.display.update(updates)
    G.event = G.event_N
