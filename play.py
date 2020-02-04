import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

class my_rpg(object):
    screen = pygame.display.set_mode((1240, 800))
    font = pygame.font.Font("data/font/rpgfont.ttf", 48)

    def __init__(self, load="(empty)"):
        # Load game / New game
        pygame.display.set_caption("The Legend of Paradou")

        if load == "(empty)":
            self.rpg()
        else:
            pass

    def rpg(self):
        clock = pygame.time.Clock()
        while True:
            self.screen.fill((0, 0, 0))
            clock.tick(60)
            self.display()
            self.event()
            pygame.display.flip()

    def event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_i:
                    print("Inventaire")
            if event.type == QUIT:
                exit(0)

    def display(self):
        pass

def start(file="(empty)"):
    my_rpg()