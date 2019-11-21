import pygame
import os
from .Mapi.map import Turn
from .Enemies.enemies import Enemy

height = 150
width = 150

playBTN = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/td-gui/PNG/menu/button_play.png')),(200, 200))
background = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/win/bg.png'))), (1368, 720))
vertical_path = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/6.png'))), (height, width))
horizontal_path = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/8.png'))), (height, width))
turn_path1 = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-tilesets1-2/version-for-the-program-Tiled/PNG/tail_1/1.png'))), (height, width))
some_pathetic_mob = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/2d-monster-sprites/PNG/5/5_enemies_1_attack_000.png'))), (45, 45))
X = 0
mob = Enemy(0, 345)

def turner(x, y, radius, clockW, halfSTART, halfEND):
    turn = Turn(x, y, radius, clockW, halfSTART, halfEND)
    if (turn.isInside(mob.posX, mob.posY)):
        mob.turn(turn)
    else:
        mob.move()

class MainMenu:
    def __init__(self, win):
        self.width = 1368
        self.height = 720
        self.menu_bg = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/win/bg.png'))), (self.width, self.height))
        self.win = win
        self.lvl_on = False

    def draw(self):
        global X
        if self.lvl_on == False:
            self.win.blit(self.menu_bg, (0, 0))
            self.win.blit(playBTN, (565, 275))
            pygame.display.update()
        if self.lvl_on == True:
            self.win.blit(background, (50, 50))
            self.win.blit(horizontal_path, (0, 300))
            self.win.blit(pygame.transform.rotate(turn_path1, 180), (150, 300))
            self.win.blit(turn_path1, (150, 150))
            self.win.blit(horizontal_path, (300, 150))
            
            mob.velX = 2
            turner(75, 225, 275, False, 4, 4)
            print(mob.posX, mob.posY)
            self.win.blit(some_pathetic_mob, (mob.posX, mob.posY))
            pygame.display.update()

    def run(self):
        run = True
        while run:

            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1] <= 475 and mouse_pos[0] >= 565 and mouse_pos[1] >= 275 and mouse_pos[0] <= 765:
                    self.lvl_on = True

            self.draw()
