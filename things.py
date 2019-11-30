// /
def turner(x, y, radius, clockW, halfSTART, halfEND):
    turn = Turn(x, y, radius, clockW, halfSTART, halfEND)
    if (turn.isInside(mob.posX, mob.posY)):
        mob.turn(turn)
    else:
        mob.move()
// /

// /
mob = Enemy(0, 175)
mobs = [mob]
mob.velX = 2
turn = Turn(300, 150, 90, False, 4, 1)

turns = [turn]
tower = Tower(500, 150)
towers = [tower]
// /

// /
def logicLoop(self, mobs, towers, turns):

    for mob in mobs:
        for turn in turns:
            if (turn.isInside(mob.posX, mob.posY)):
                mob.turn(turn)
        else:
            mob.move()
        for tower in towers:
            if (tower.isInside(mob.posX, mob.posY) and tower.cooldown == 0):
                tower.attack(mob)
                if (mob.hp <= 0):
                    mobs.remove(mob)
    print(mob.hp)
// /

// /
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
// /

// /
global tower_placed
for i in range (0,8):
    for k in range (0,14):
        self.win.blit(bg_tile, (k * 100, i * 100))
self.win.blit(pygame.transform.rotate(st_p, (90)), (0, 150))
 elf.win.blit(pygame.transform.rotate(st_p,(90)), (150, 150))
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
    self.mob.draw(mob1, self.win, self.mob.posX, self.mob.posY) 
    #self.win.blit(mob1, (self.mob.posX, self.mob.posY))
for event in pygame.event.get():
    if event.type is pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] <= 300 and mouse_pos[0] >= 400 and mouse_pos[1] >= 100 and mouse_pos[0] <= 600:
            tower_placed = True
    if tower_placed == True:
        self.win.blit(tower_archer, (460, 130))
        pygame.draw.circle(self.win, (0, 255, 255), (self.tower.x, self.tower.y), self.tower.radius, 1)
// /

// /
mob = Enemy(0, 175)
mobs = [mob]
mob.velX = 2
turn = Turn(300, 150, 90, False, 4, 1)

turns = [turn]
tower = Tower(500, 150)
towers = [tower]
// /
