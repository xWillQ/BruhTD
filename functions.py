import pygame


def logicLoop(mobs, turns):
    for i in range(0, len(mobs)):
        turned = False
        for turn in turns:
            if (turn.isInside(mobs[i].x, mobs[i].y) and not turned):
                mobs[i].turn(turn)
                turned = True
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
        currX = currX
        currY = entities[i].y + entities[i].shiftY
        currY = currY
        cleared.append(pygame.Rect(int(currX), int(currY), entities[i].transformation * 1.2, entities[i].transformation * 1.2))
        win.blit(background, (currX, currY), cleared[len(cleared) - 1])
    return cleared
