##
## EPITECH PROJECT, 2020
## display
## File description:
## display function
##

import pygame
from pygame.locals import *
import collision

def display_main_menu(self):
    new_text = self.font.render("New", 1, (255, 255, 255))
    load_text = self.font.render("Load", 1, (255, 255, 255))
    quit_text = self.font.render("Quit", 1, (255, 255, 255))

    if self.mouse[0] >= 610 and self.mouse[0] <= 700 and self.mouse[1] >= 315 and self.mouse[1] <= 345:
        new_text = self.font.render("New", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 705 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
        load_text = self.font.render("Load", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 690 and self.mouse[1] >= 515 and self.mouse[1] <= 545:
        quit_text = self.font.render("Quit", 1, (255, 0, 0))
    self.window.blit(self.images.get("main_menu"), (0, 0))
    self.window.blit(self.images.get("logo"), (450, 0))
    self.window.blit(new_text, (610, 300))
    self.window.blit(load_text, (610, 400))
    self.window.blit(quit_text, (610, 500))

def display_options(self):
    logo = pygame.image.load("data/img/logo.png")

    self.window.blit(self.images.get("main_menu"), (0, 0))
    self.window.blit(self.images.get("logo"), (450, 0))

def display_menu(self):
    pos = self.p.get_positions()
    sprite = self.p.get_animation("Down")

    self.window.blit(self.images.get("map1"), (0 - pos[0], 0 - pos[1]))
    self.window.blit(sprite[1], (620, 400))
    self.window.blit(self.images.get("alt_menu"), (0, 0))

def display_map(self):
    pos = self.p.get_positions()
    sprite = self.p.get_animation("Down")

    if self.move_keys[0]:
        pos[1] -= 1
        sprite = self.p.get_animation("Up")
    if self.move_keys[1]:
        pos[1] += 1
        sprite = self.p.get_animation("Down")
    if self.move_keys[2]:
        pos[0] -= 1
        sprite = self.p.get_animation("Left")
    if self.move_keys[3]:
        pos[0] += 1
        sprite = self.p.get_animation("Right")
    if True in self.move_keys:
        if self.refresh_time % 10 == 0:
            self.index_animation += 1
            if self.index_animation == 3:
                self.index_animation = 0
    else:
        self.index_animation = 1

    pos = collision.check_collision(self, pos)
    self.p.change_positions(pos[0], pos[1])
    self.window.blit(self.images.get("map1"), (0 - pos[0], 0 - pos[1]))
    self.window.blit(sprite[self.index_animation], (620, 400))