import pygame
import G
from math import sqrt

fireball = []
for i in (0, 19):
    fireball.append("Assets/Spells/fireball/" + str(i) + ".png")


class Spell():
    def __init__(self, x, y):
        self.posX = x
        self.posY = y
        self.damage = 100
        self.radius = 50
        self.anim_c = 0
        self.casted = False
        self.cooldown = 60

    def deal_dmg(self, mob):
        self.casted = True
        self.radius = self.radius * 0.97 / 2
        pygame.draw.circle(G.win, (0, 55, 255), (self.posX, self.posY), round(self.radius), 1)
        return (sqrt((mob.x - self.posX) ** 2 + (mob.y - self.posY) ** 2) + 2 <= self.radius)

    def draw(self):

        if self.anim_c != 19:
            self.casted = True
            G.win.blit(pygame.transform.scale(pygame.image.load(fireball[self.anim_c]), (100, 263)), (self.posX - 50, self.posY - 131))
            self.anim_c += 1
        else:
            self.casted = False
