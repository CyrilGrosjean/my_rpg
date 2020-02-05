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

def event_options(event, self):
    if event.type == QUIT:
        exit(0)

def event_game(event, self):
    if event.type == KEYDOWN:
        if event.key == self.option.get_key("Up"):
            self.move_keys[0] = True
        if event.key == self.option.get_key("Down"):
            self.move_keys[1] = True
        if event.key == self.option.get_key("Left"):
            self.move_keys[2] = True
        if event.key == self.option.get_key("Right"):
            self.move_keys[3] = True
    if event.type == KEYUP:
        if event.key == self.option.get_key("Up"):
            self.move_keys[0] = False
        if event.key == self.option.get_key("Down"):
            self.move_keys[1] = False
        if event.key == self.option.get_key("Left"):
            self.move_keys[2] = False
        if event.key == self.option.get_key("Right"):
            self.move_keys[3] = False
    if event.type == QUIT:
        exit(0)