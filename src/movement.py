##
## EPITECH PROJECT, 2020
## movement
## File description:
## movement
##

import pygame
from pygame.locals import *

def check_movement(self):
    pos = self.p.get_positions()
    sprite = self.p.get_animation("Down")

    if self.move_keys[0]:
        if self.move_keys[4]:
            pos[1] -= 1
        pos[1] -= 1
        sprite = self.p.get_animation("Up")
    if self.move_keys[1]:
        if self.move_keys[4]:
            pos[1] += 1
        pos[1] += 1
        sprite = self.p.get_animation("Down")
    if self.move_keys[2]:
        if self.move_keys[4]:
            pos[0] -= 1
        pos[0] -= 1
        sprite = self.p.get_animation("Left")
    if self.move_keys[3]:
        if self.move_keys[4]:
            pos[0] += 1
        pos[0] += 1
        sprite = self.p.get_animation("Right")

    nb = 0
    for i in self.move_keys:
        if i == True:
            nb += 1
    if nb > 1:
        if self.move_keys[0]:
            if self.move_keys[4]:
                pos[1] += 0.5
            pos[1] += 0.25
        if self.move_keys[1]:
            if self.move_keys[4]:
                pos[1] -= 0.5
            pos[1] -= 0.25
        if self.move_keys[2]:
            if self.move_keys[4]:
                pos[0] += 0.5
            pos[0] += 0.25
        if self.move_keys[3]:
            if self.move_keys[4]:
                pos[0] -= 0.5
            pos[0] -= 0.25

    if True in self.move_keys:
        if self.refresh_time % 15 == 0:
            self.index_animation += 1
            if self.index_animation == 3:
                self.index_animation = 0
    else:
        self.index_animation = 1
    return pos, sprite