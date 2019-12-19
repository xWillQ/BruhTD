import pygame
from GUI.button import isInside
import G

enemyType = {"scorpio": {"velocity": 1.5, "hp": 70, "shiftX": 0.07, "shiftY": 0.14, "reward": 3},
             "wizard": {"velocity": 1.0, "hp": 150, "shiftX": 0.17, "shiftY": 0.13, "reward": 5}}
towerType = {"archer": {"damage": [5, 10, 7]},
             "magic": {"damage": [15, 20, 25]},
             "support": {"damage": [10, 10, 10]}}


class Player():
    def __init__(self, hp, gold):
        self.hp = hp
        self.gold = gold
        self.mana = 40
        self.frame = 0
        self.casting = False
        self.freeze_casted = False
        self.F_tick = 0
        self.pu_tick = 0
        self.pu_casted = False

    def power_up(self, tower):
        tower.damage = towerType[tower.typeName]["damage"][tower.level - 1] + 15

    def pu_cancel(self, tower):
        tower.damage = towerType[tower.typeName]["damage"][tower.level - 1]

    def power_up_ticker(self):
        if self.pu_tick != 360:
            self.pu_tick += 1
        else:
            self.pu_casted = False
            self.pu_tick = 0

    def freeze_ticker(self):
        if self.F_tick != 280:
            self.F_tick += 1
        else:
            self.freeze_casted = False
            self.F_tick = 0

    def freeze_cancel(self, mob):
        mob.velocity = enemyType[mob.typeName]["velocity"]

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
