##
## EPITECH PROJECT, 2020
## objects
## File description:
## objects
##

import pygame
from pygame.locals import *

class Item():

    image = pygame.image.load("data/icons/menu/save.png")
    ID = 0
    effects = {}
    count = 0

    def __init__(self):
        pass

    def set_presets(self, image, id, effects):
        self.image = image
        self.ID = id
        self.effects = effects

    def set_count(self, count):
        self.count = count

    def get_effects(self, name):
        return self.effects.get(name)

    def set_effects(self, name, value):
        self.effects[name] = value

    def get_id(self):
        return (self.ID)

    def get_count(self):
        return self.count