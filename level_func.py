import pygame
from GUI.button import isInside
import Mobs.enemies as enemies
from Map.tower import Tower


def level_controller(Mobs, turns, towers):
    for i in range(0, len(Mobs)):
        turned = False
        for turn in turns:
            if (turn.isInside(Mobs[i].x, Mobs[i].y)):
                Mobs[i].turn(turn)
                turned = True
            if (not turned):
                Mobs[i].move()

            if ((i > 0) and (Mobs[i - 1].distance > Mobs[i].distance)):
                t = Mobs[i - 1]
                Mobs[i - 1] = Mobs[i]
                Mobs[i] = t

        if Mobs[i].hp < 0:
            Mobs.pop(i)
