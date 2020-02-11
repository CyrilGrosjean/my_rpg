##
## EPITECH PROJECT, 2020
## monster
## File description:
## monster
##

import pygame
from pygame.locals import *

class Monster():

    pos = [0, 900]
    monster_info = {"MaxHealth": 100, "Health": 100, "Attack": 10, "Defense": 10, "Agility": 10, "Speed": 10}
    monster_loot = {"Gold": 10, "Exp": 10, "Objects": []}
    monster_animation = {"Up": [pygame.image.load("data/sprite/monster/up1.png"), pygame.image.load("data/sprite/monster/up2.png"), pygame.image.load("data/sprite/monster/up3.png")],
    "Down": [pygame.image.load("data/sprite/monster/down1.png"), pygame.image.load("data/sprite/monster/down2.png"), pygame.image.load("data/sprite/monster/down3.png")],
    "Left": [pygame.image.load("data/sprite/monster/left1.png"), pygame.image.load("data/sprite/monster/left2.png"), pygame.image.load("data/sprite/monster/left3.png")],
    "Right": [pygame.image.load("data/sprite/monster/right1.png"), pygame.image.load("data/sprite/monster/right2.png"), pygame.image.load("data/sprite/monster/right3.png")]}

    def __init__(self):
        pass

    def get_animation(self, name):
        return self.monster_animation.get(name)

    def get_monster_info(self, name):
        return self.monster_info.get(name)

    def get_monster_loot(self, name):
        return self.monster_loot.get(name)

    def set_monster_info(self, name, value):
        self.monster_info[name] = value

    def set_monster_loot(self, name, value):
        self.monster_loot[name] = value

    def get_positions(self):
        return self.pos

    def change_positions(self, x, y):
        self.pos[0] = x
        self.pos[1] = y