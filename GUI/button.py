from math import sqrt
import pygame
import G


def isInside(MPx, MPy, butt_x, butt_y, butt_radius):
    butt_radius = butt_radius * 0.97 / 2
    pygame.draw.circle(G.win, (0, 55, 255), (round(butt_x), round(butt_y)), round(butt_radius), 1)
    return (sqrt((MPx - butt_x)**2 + (MPy - butt_y)**2) + 2 <= butt_radius)


class Button():
    def __init__(self, x, y, transformation, asset):
        self.x = x
        self.y = y
        self.asset = pygame.transform.scale(asset, (transformation, transformation))
        self.circleX = x + round(transformation / 2)
        self.circleY = y + round(transformation / 2)
        self.radius = round(transformation * 0.97 / 2)

    def isInside(self, x, y):
        return (sqrt((x - self.x)**2 + (y - self.y)**2) + 2 <= self.radius)

    def draw(self, win):
        win.blit(self.asset, (self.x, self.y))
