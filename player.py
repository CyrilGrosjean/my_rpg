##
## EPITECH PROJECT, 2020
## player
## File description:
## functions for player
##

import pygame
from pygame.locals import *

class Player():

    pos = [0, 0]
    money = 100
    player_info = {"Health": 100, "Attack": 10, "Defense": 10, "Speed": 10}
    equipment = {"Weapon": "Sword", "Body": "Chestplate", "Head": "Helmet", "Legs": "Leggings", "Feet": "Boots", "Arm left": "Ring", "Arm right": "Ring"}
    player_animation = {"Up": [pygame.image.load("data/sprite/up1.png"), pygame.image.load("data/sprite/up2.png"), pygame.image.load("data/sprite/up3.png")],
    "Down": [pygame.image.load("data/sprite/down1.png"), pygame.image.load("data/sprite/down2.png"), pygame.image.load("data/sprite/down3.png")],
    "Left": [pygame.image.load("data/sprite/left1.png"), pygame.image.load("data/sprite/left2.png"), pygame.image.load("data/sprite/left3.png")],
    "Right": [pygame.image.load("data/sprite/right1.png"), pygame.image.load("data/sprite/right2.png"), pygame.image.load("data/sprite/right3.png")]}

    def __init__(self):
        pass

    def get_positions(self):
        return (self.pos)

    def change_positions(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def change_player_info(self, info_name, n):
        self.player_info[info_name] = n

    def change_equipment(self, type_eq, equipment):
        self.equipment[type_eq] = equipment

    def get_global_player_info(self):
        return (self.player_info)

    def get_one_player_info(self, name):
        return self.player_info.get(name)

    def get_all_equipment(self):
        return self.equipment

    def get_one_equipment(self, name):
        return self.equipment.get(name)

    def get_money(self):
        return self.money

    def change_money(self, nb):
        self.money = nb