import pygame


def logicLoop(mobs, turns):
    for i in range(0, len(mobs)):
        turned = False
        for turn in turns:
            if (turn.isInside(mobs[i].x, mobs[i].y) and not turned):
                mobs[i].turn(turn)
                turned = True
                break
        if (not turned):
            mobs[i].move()

        if ((i > 0) and (mobs[i - 1].distance > mobs[i].distance)):
            t = mobs[i - 1]
            mobs[i - 1] = mobs[i]
            mobs[i] = t


def clear(entities, win, background):
    cleared = []
    for i in range(0, len(entities)):
        currX = entities[i].x + entities[i].shiftX
        currY = entities[i].y + entities[i].shiftY
        cleared.append(pygame.Rect(int(currX), int(currY), entities[i].width * 1.2, entities[i].height * 1.2))
        win.blit(background, (currX, currY), cleared[len(cleared) - 1])
    return cleared
