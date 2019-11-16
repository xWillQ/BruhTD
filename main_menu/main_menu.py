import pygame

playBTN = pygame.transform.scale(pygame.image.load('button_play.png'),(200, 200))

class MainMenu:
    def __init__(self, win):
        self.width = 1368
        self.height = 720
        self.menu_bg = pygame.image.load('bg.png')
        self.menu_bg = pygame.transform.scale(self.menu_bg, (self.width, self.height))
        self.win = win

    def draw(self):
        self.win.blit(self.menu_bg, (0, 0))
        self.win.blit(playBTN, (565,275))
        pygame.display.update()

    def run(self):
        run = True
        while run:

            pygame.time.delay(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1] <= 475 and mouse_pos[0] >= 565 and mouse_pos[1] >= 275 and mouse_pos[0] <= 765:
                    gamel = game_process(win)
                    gamel.run()
            self.draw()
