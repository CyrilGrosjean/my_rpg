##
## EPITECH PROJECT, 2020
## options
## File description:
## functions to get options
##

import pygame
from pygame.locals import *

pygame.init()

class Options():

    key_options = {"Up": K_UP, "Down": K_DOWN, "Left": K_LEFT, "Right": K_RIGHT, "Inventory": K_i, "Menu": K_ESCAPE, "Action": K_RETURN, "Dash": K_LSHIFT}

    def __init__(self):
        pass

    def change_key(self, name, key):
        self.key_options[name] = key

    def get_key(self, name):
        return self.key_options.get(name)