import pygame
import os
from Map.map import loadLevel
from GUI.button import Button
import Mobs.enemies as enemies
from Map.tower import Tower as Tower

towers = [Tower(680, 300, 120), Tower(1090, 400, 120)]

death_button = Button(15, 325, 40, pygame.image.load(os.path.join('Assets/GUI/interface_game/skull.png')))
lvl1 = ["r", "r", "u", "r", "r", "d", "d", "r", "r", "r", "d", "d", "r", "r", "r"]
turns, background, start, Idirection = loadLevel(lvl1, (0, 250), towers, 0.7, "forest", 1920, 1080)

scorpio_anim = [
    'Assets/Mobs/scorpio/walk_000.png', 'Assets/Mobs/scorpio/walk_001.png', 'Assets/Mobs/scorpio/walk_002.png', 'Assets/Mobs/scorpio/walk_003.png', 'Assets/Mobs/scorpio/walk_004.png',
    'Assets/Mobs/scorpio/walk_005.png', 'Assets/Mobs/scorpio/walk_006.png', 'Assets/Mobs/scorpio/walk_007.png', 'Assets/Mobs/scorpio/walk_008.png', 'Assets/Mobs/scorpio/walk_009.png',
    'Assets/Mobs/scorpio/walk_010.png', 'Assets/Mobs/scorpio/walk_011.png', 'Assets/Mobs/scorpio/walk_012.png', 'Assets/Mobs/scorpio/walk_013.png', 'Assets/Mobs/scorpio/walk_014.png',
    'Assets/Mobs/scorpio/walk_015.png', 'Assets/Mobs/scorpio/walk_016.png', 'Assets/Mobs/scorpio/walk_017.png', 'Assets/Mobs/scorpio/walk_018.png', 'Assets/Mobs/scorpio/walk_018.png'
]

Mobs = [
    enemies.Enemy(-40, 360, "r", "scorpio"),
    enemies.Enemy(-100, 360, "r", "scorpio"),
    enemies.Enemy(-160, 360, "r", "scorpio"),
]

bg = background
tower_place = pygame.transform.scale(pygame.image.load(os.path.join('Assets/tiles/forest/22.png')), (180, 180))


class Level():
    def __init__(self, win, number, mpos, WT, turns=turns):

        self.turns = turns
        self.win = win
        self.number = number
        self.Mpos = mpos
        self.wave_trigger = WT

    def draw(self, tower_placed, tower1_placed):

        self.win.blit(bg, (0, 0))
        if self.number == 1:

            self.win.blit(tower_place, (585, 250))
            self.win.blit(tower_place, (995, 350))

            if self.wave_trigger is True:
                death_button.draw(self.win)

            if self.wave_trigger is False:
                for i in range(0, len(Mobs)):
                    turned = False
                    for turn in self.turns:
                        if (turn.isInside(Mobs[i].x, Mobs[i].y)):
                            Mobs[i].turn(turn)
                            turned = True
                    if (not turned):
                        Mobs[i].move()

                    if ((i > 0) and (Mobs[i - 1].distance > Mobs[i].distance)):
                        t = Mobs[i - 1]
                        Mobs[i - 1] = Mobs[i]
                        Mobs[i] = t

                    if i == len(Mobs) - 1:
                        if tower_placed is True:
                            if towers[0].isInside(Mobs[i].x, Mobs[i].y) is True:
                                towers[0].attack(Mobs[i])
                        if tower1_placed is True:
                            if towers[1].isInside(Mobs[i].x, Mobs[i].y) is True:
                                towers[1].attack(Mobs[i])

                    if Mobs[i].hp < 0:
                        Mobs.pop(i)

                    print(towers[0].cooldown)

                for i in range(0, len(Mobs)):
                    if Mobs[i].hp > 0:
                        Mobs[i].draw(self.win)

        if tower_placed is True:
            towers[0].setType("archer")
            towers[0].loadAssets()
            towers[0].draw(self.win)
            # pygame.draw.circle(self.win, (0, 255, 255), (towers[0].x, towers[0].y), towers[0].radius, 1)
        if tower1_placed is True:
            towers[1].setType("archer")
            towers[1].loadAssets()
            towers[1].draw(self.win)
            # pygame.draw.circle(self.win, (0, 255, 255), (towers[1].x, towers[1].y), towers[1].radius, 1)
