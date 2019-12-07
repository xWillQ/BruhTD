import pygame


def logicLoop(mobs, towers):
    for tower in towers:
        if ((tower.level != 0) and (tower.cooldown == 0)):
            for mob in mobs:
                if (tower.isInside(mob.x, mob.y) and (mob.state != "dying")):
                    tower.attack()
                    mob.hurt(tower.damage)
                    break
        elif (tower.cooldown != 0):
            tower.cooldown -= 1


def clear(entities, win, background):
    cleared = []
    for i in range(0, len(entities)):
        currX = entities[i].x + entities[i].shifts[0]
        currY = entities[i].y + entities[i].shifts[1]
        cleared.append(pygame.Rect(int(currX), int(currY), entities[i].width + 1, entities[i].height + 1))
        win.blit(background, (currX, currY), cleared[len(cleared) - 1])
    return cleared
