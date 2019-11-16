import pygame

class game_process:
    def __init__(self, win):
        self.background = pygame.image.load('bg.png')
        self.win = win

    def run(self):
        self.blit(background, (50, 50))
        pygame.display.update()