import pygame
pygame.init()

win = pygame.display.set_mode((1360,768))

pygame.display.set_caption("Bruh TD protobuild")

x = 0
y = 400
width = 40
height = 40
vel = 5
stepCount = 0

def windowRE():
    global stepCount
    win.blit(main_bg, (0, 0))
    #win.blit(road1, (0, 0))
    #win.blit(road2, (150, 0))
    #win.blit(road5, (200, 150))
    player1[stepCount] = pygame.transform.scale(player1[stepCount], (60, 60))
    win.blit(player1[stepCount], (x, y))
    if stepCount != 9:
        stepCount += 1
    elif stepCount > 8:
        stepCount = 0
    pygame.display.update()


#player1 = [pygame.image.load('1_enemies_1_WALK_000.png'),
#pygame.image.load('1_enemies_1_WALK_002.png'),
#pygame.image.load('1_enemies_1_WALK_003.png'),
#pygame.image.load('1_enemies_1_WALK_004.png'),
#pygame.image.load('1_enemies_1_WALK_005.png'),
#pygame.image.load('1_enemies_1_WALK_006.png'),
#pygame.image.load('1_enemies_1_WALK_007.png'),
#pygame.image.load('1_enemies_1_WALK_008.png'),
#pygame.image.load('1_enemies_1_WALK_009.png')]

main_bg = pygame.image.load('main_bg.png')
main_bg = pygame.transform.scale(main_bg, (1360, 768))

run = True
while run:

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and x > 1:
        x -= vel
    if key[pygame.K_RIGHT] and x < 680:
        x += vel
    if key[pygame.K_DOWN] and y < 650:
        y += vel
    if key[pygame.K_UP] and y > 1:
        y -= vel

    if x < 440:
        x += 2
    if x == 440 and y < 880:
        y += 2

    windowRE()

pygame.quit()