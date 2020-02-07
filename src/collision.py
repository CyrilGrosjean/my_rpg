##
## EPITECH PROJECT, 2020
## collision
## File description:
## function collision
##

import pygame
from pygame.locals import *
from math import floor

def check_map_other_number(self, x, y, map_block):
    X = x + 620 + 25
    Y = y = 400 + 50
    X = floor(X / 48)
    Y = floor(Y / 48)
    map_block_new = self.map_collisions[Y][X]

    if map_block != map_block_new and map_block != 0:
        if map_block != map_block_new - 1:
            if map_block != map_block_new + 1:
                return False
    return True

def check_collision(self, pos):
    x = pos[0] + 620 + 25
    y = pos[1] + 400 + 50
    x = floor(x / 48)
    y = floor(y / 48)
    map_block = self.map_collisions[y][x]

    if map_block == 0:
        if self.move_keys[0]:
            pos[1] += 3
        if self.move_keys[1]:
            pos[1] -= 3
        if self.move_keys[2]:
            pos[0] += 3
        if self.move_keys[3]:
            pos[0] -= 3
    else:
        pass
    return pos