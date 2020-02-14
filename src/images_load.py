##
## EPITECH PROJECT, 2020
## images load
## File description:
## function to get all loaded images
##

import pygame
from pygame.locals import *

def get_image(self):
    images = {
        "main_menu": {"background": pygame.image.load("data/img/menu.jpg").convert_alpha(), "logo": pygame.image.load("data/img/logo.png").convert_alpha()},
        "main_option": {"background": pygame.image.load("data/img/menu.jpg").convert_alpha(), "logo": pygame.image.load("data/img/logo.png").convert_alpha()},
        "in_game": {"map": pygame.image.load("data/maps/map1.png").convert_alpha(), "heal_bar": pygame.image.load("data/system/heal_bar.png").convert_alpha(), "empty_bar": pygame.image.load("data/system/empty_bar.png").convert_alpha()},
        "menu_in_game": {"map": pygame.image.load("data/maps/map1.png").convert_alpha(), "alt_menu": pygame.image.load("data/img/black_screen.png").convert_alpha(), "save": pygame.image.load("data/icons/menu/save.png").convert(), "option": pygame.image.load("data/icons/menu/options.png").convert(), "quit": pygame.image.load("data/icons/menu/quit.png").convert(), "quests": pygame.image.load("data/icons/menu/quests.png").convert(), "inventory": pygame.image.load("data/icons/menu/inventory.png").convert(), "equip": pygame.image.load("data/icons/menu/equip.png").convert()},
        "inventory": {"map": pygame.image.load("data/maps/map1.png").convert_alpha(), "inventory": pygame.image.load("data/system/inventory.png").convert_alpha()}
    }
    return images