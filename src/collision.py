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
    Y = y + 400 + 50
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
    nb = 0

    for i in self.move_keys:
        if i == True:
            nb += 1
    if map_block == 0:
        if self.move_keys[0]:
            if nb > 1:
                if self.move_keys[4]:
                    pos[1] += 0.5
                pos[1] += 0.75
            else:
                if self.move_keys[4]:
                    pos[1] += 1
                pos[1] += 1
        if self.move_keys[1]:
            if nb > 1:
                if self.move_keys[4]:
                    pos[1] -= 0.5
                pos[1] -= 0.75
            else:
                if self.move_keys[4]:
                    pos[1] -= 1
                pos[1] -= 1
        if self.move_keys[2]:
            if nb > 1:
                if self.move_keys[4]:
                    pos[0] += 0.5
                pos[0] += 0.75
            else:
                if self.move_keys[4]:
                    pos[0] += 1
                pos[0] += 1
        if self.move_keys[3]:
            if nb > 1:
                if self.move_keys[4]:
                    pos[0] -= 0.5
                pos[0] -= 0.75
            else:
                if self.move_keys[4]:
                    pos[0] -= 1
                pos[0] -= 1
    else:
        if self.move_keys[0]:
            if not (check_map_other_number(self, pos[0], pos[1] + 1, map_block)):
                if nb > 1:
                    if self.move_keys[4]:
                        pos[1] += 0.5
                    pos[1] += 0.75
                else:
                    if self.move_keys[4]:
                        pos[1] += 1
                    pos[1] += 1
        if self.move_keys[1]:
            if not (check_map_other_number(self, pos[0], pos[1] - 1, map_block)):
                if nb > 1:
                    if self.move_keys[4]:
                        pos[1] -= 0.5
                    pos[1] -= 0.75
                else:
                    if self.move_keys[4]:
                        pos[1] -= 1
                    pos[1] -= 1
        if self.move_keys[2]:
            if not (check_map_other_number(self, pos[0] + 1, pos[1], map_block)):
                if nb > 1:
                    if self.move_keys[4]:
                        pos[0] += 0.5
                    pos[0] += 0.75
                else:
                    if self.move_keys[4]:
                        pos[0] += 1
                    pos[0] += 1
        if self.move_keys[3]:
            if not (check_map_other_number(self, pos[0] - 1, pos[1], map_block)):
                if nb > 1:
                    if self.move_keys[4]:
                        pos[0] -= 0.5
                    pos[0] -= 0.75
                else:
                    if self.move_keys[4]:
                        pos[0] -= 1
                    pos[0] -= 1
    return pos