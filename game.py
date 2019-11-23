import pygame
import os
from main_menu.Mapi.map import Turn
from main_menu.Enemies.enemies import Enemy
from main_menu.main_menu import main_menu

condition = 0

bg = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/menu/bg.png'))), (1368, 720))
playBTN = pygame.transform.scale((pygame.image.load(os.path.join('game_assets/td-gui/PNG/menu/button_play.png'))), (200, 200))
win = pygame.display.set_mode((1368, 720))

def turner(x, y, radius, clockW, halfSTART, halfEND):
    turn = Turn(x, y, radius, clockW, halfSTART, halfEND)
    if (turn.isInside(mob.posX, mob.posY)):
        mob.turn(turn)
    else:
        mob.move()

class game:
    def __init__(self, win):
        self.width = 1368
        self.height = 720
        self.win = win
        self.menu_condition = True
        self.game_condition = False

    def draw(self):
        menu = main_menu(win, bg, playBTN, condition)
        if self.menu_condition is True:
            menu.draw()
        #if self.game_condition is True:



    def run(self):

        run = True
        global condition
        while run:

            pygame.time.delay(10)
            print(pygame.mouse.get_pos())

            for event in pygame.event.get():

                if event.type is pygame.QUIT:
                    run = False

                if event.type is pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] <= 475 and mouse_pos[0] >= 565 and mouse_pos[1] >= 275 and mouse_pos[0] <= 765:
                        condition = 1

            self.draw()
