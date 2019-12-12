import pygame
from GUI.button import isInside
import G


class Player():
    def __init__(self, hp, gold):
        self.hp = hp
        self.gold = gold
        self.mana = 40
        self.frame = 0
        self.casting = False

    def hp_loss(self, mob):
        self.hp -= mob.damage

    def gold_add(self, mob):
        self.gold += mob.reward

    def spell(self, pos, mobs, player, transformation=0.15):
        asset = pygame.image.load("Assets/Assets_All/magic-effects-game-sprite/PNG/fire/1_effect_fire_" + (3 - len(str(self.frame))) * "0" + str(self.frame) + ".png")
        asset = pygame.transform.scale(asset, (int(asset.get_width() * transformation), int(asset.get_height() * transformation)))
        for mob in mobs:
            if self.mana - 20 >= 0 and isInside(pos[0], pos[1], mob.x, mob.y, 150):
                mob.hurt(100)
                player.mana -= 20
                G.win.blit(asset, (pos[0] - asset.get_width() / 2 * 0.8, pos[1] - asset.get_height() * 0.855))
                if self.frame < 18:
                    self.frame += 1
                else:
                    self.frame = 0
                    self.casting = False
