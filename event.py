##
## EPITECH PROJECT, 2020
## event
## File description:
## functions event
##

import pygame
from pygame.locals import *

def event_main_menu(event, self):
    if event.type == MOUSEBUTTONDOWN:
        if self.mouse[0] >= 610 and self.mouse[0] <= 700 and self.mouse[1] >= 315 and self.mouse[1] <= 345:
            self.fen, self.page = 1, 0
        if self.mouse[0] >= 610 and self.mouse[0] <= 705 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
            self.fen, self.page = 0, 1
        if self.mouse[0] >= 610 and self.mouse[0] <= 690 and self.mouse[1] >= 515 and self.mouse[1] <= 545:
            exit(0)
    if event.type == QUIT:
        exit(0)