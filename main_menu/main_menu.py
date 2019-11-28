import pygame
import os
from .Mapi.tower import Tower
from .Enemies.enemies import Enemy
from .Mapi.map import Turn


table = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/table.png'))), (684, 360))
empty_bt = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/btton_empty.png'))), (100, 100))
num1 = pygame.image.load(os.path.join('game_assets/td-gui/PNG/levels/num_1.png'))
rope = pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/rope_big.png'))
close = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-gui/PNG/settings/button_close.png')), (60, 60))
bg_tile = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/42.png')), (100, 100))
turn_p = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/1.png')), (150, 150))
st_p = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/6.png')), (150, 150))
tower_pl = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/22.png')), (250, 250))
mob1 = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/2d-monster-sprites/PNG/1/1_enemies_1_attack_000.png')), (60, 60))
tower_archer = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/archer-tower-game-assets/PNG/8.png')), (90, 90))
tower_placed = False


class main_menu:

    def __init__(self, win, bg, playBTN, condition, mob, tower, turn, mobs, towers, turns):
        self.win = win
        self.bg = bg
        self.playBTN = playBTN
        self.condition = condition
        self.mob = mob
        self.tower = tower
        self.turn = turn
        self.mobs = mobs
        self.towers = towers
        self.turns = turns

    def turner(self, x, y, radius, clockW, halfSTART, halfEND, testnum):
        self.turn = Turn(x, y, radius, clockW, halfSTART, halfEND)
        if (self.turn.isInside(self.mob.posX, self.mob.posY)):
            self.mob.turn(self.turn)
            print(testnum)

    def logicLoop(self, mobs, towers, turns):

        for self.mob in self.mobs:
            for self.turn in self.turns:
                if (self.turn.isInside(self.mob.posX, self.mob.posY)):
                    self.mob.turn(self.turn)
            else:
                self.mob.move()
            for self.tower in self.towers:
                if (self.tower.isInside(self.mob.posX, self.mob.posY) and self.tower.cooldown == 0):
                    self.tower.attack(self.mob)
                    if (self.mob.hp <= 0):
                        self.mobs.remove(self.mob)
        #print(self.mob.hp)

    def draw(self):
        if self.condition == 0:

            self.win.blit(self.bg, (0, 0))
            self.win.blit(self.playBTN, (565, 275))

        if self.condition == 1:
            self.win.blit(self.bg, (0, 0))
            self.win.blit(table, (350, 175))
            self.win.blit(empty_bt, (415, 250))
            self.win.blit(num1, (450, 270))
            self.win.blit(rope, (450, -225))
            self.win.blit(rope, (890, -225))
            self.win.blit(close, (985, 160))

        if self.condition == 2:
            global tower_placed
            for i in range (0,8):
                for k in range (0,14):
                    self.win.blit(bg_tile, (k * 100, i * 100))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (0, 150))
            self.win.blit(pygame.transform.rotate(st_p,(90)), (150, 150))
            self.win.blit(pygame.transform.rotate(turn_p, (180)), (300, 150))
            self.win.blit(pygame.transform.rotate(turn_p, (0)), (300, 0))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (450, 0))
            self.win.blit(pygame.transform.rotate(st_p, (0)), (600, 150))
            self.win.blit(pygame.transform.rotate(st_p, (0)), (600, 300))
            self.win.blit(pygame.transform.rotate(turn_p, (270)), (600, 0))
            self.win.blit(pygame.transform.rotate(turn_p, (90)), (600, 450))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (750, 450))
            self.win.blit(pygame.transform.rotate(st_p, (90)), (900, 450))
            self.win.blit(pygame.transform.rotate(turn_p, (270)), (1050, 450))
            self.win.blit(pygame.transform.rotate(st_p, (0)), (1050, 600))
            self.win.blit(tower_pl, (395, 75))
            self.win.blit(tower_pl, (700, 285))
            self.turner(300, 0, 150, True, 3, 1, 11)
            self.turner(600, 0, 150, True, 4, 1, 22)
            self.turner(600, 300, 150, False, 3, 4, 33)
            self.logicLoop(self.mobs, self.towers, self.turns)
            if self.mob.hp != 0:
                self.win.blit(mob1, (self.mob.posX, self.mob.posY))
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] <= 300 and mouse_pos[0] >= 400 and mouse_pos[1] >= 100 and mouse_pos[0] <= 600:
                        tower_placed = True
            if tower_placed == True:
                self.win.blit(tower_archer, (460, 130))
                pygame.draw.circle(self.win, (0, 255, 255),(self.tower.x, self.tower.y),self.tower.radius, 1)

        pygame.display.update()
