##
## EPITECH PROJECT, 2020
## display
## File description:
## display function
##

import pygame
from pygame.locals import *
import collision
import animations

def display_main_menu(self):
    new_text = self.font.render("New", 1, (255, 255, 255))
    load_text = self.font.render("Load", 1, (255, 255, 255))
    quit_text = self.font.render("Quit", 1, (255, 255, 255))
    img = self.images.get("main_menu")

    if self.mouse[0] >= 610 and self.mouse[0] <= 700 and self.mouse[1] >= 315 and self.mouse[1] <= 345:
        new_text = self.font.render("New", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 705 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
        load_text = self.font.render("Load", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 690 and self.mouse[1] >= 515 and self.mouse[1] <= 545:
        quit_text = self.font.render("Quit", 1, (255, 0, 0))
    self.window.blit(img.get("background"), (0, 0))
    self.window.blit(img.get("logo"), (450, 0))
    self.window.blit(new_text, (610, 300))
    self.window.blit(load_text, (610, 400))
    self.window.blit(quit_text, (610, 500))

def display_options(self):
    img = self.images.get("main_option")

    self.window.blit(img.get("background"), (0, 0))
    self.window.blit(img.get("logo"), (450, 0))

def display_menu(self):
    pos = self.p.get_positions()
    sprite = self.p.get_animation("Down")
    img = self.images.get("menu_in_game")

    animations.animation_menu(self, img)
    self.window.blit(img.get("map"), (0 - pos[0], 0 - pos[1]))
    self.window.blit(sprite[1], (620, 400))
    self.window.blit(img.get("alt_menu"), (0, 0))
    self.window.blit(img.get("inventory"), (590, 360))
    self.window.blit(img.get("equip"), (670, 360))
    self.window.blit(img.get("quests"), (690, 430))
    self.window.blit(img.get("save"), (560, 430))
    self.window.blit(img.get("quit"), (630, 480))
    animations.display_text_menu(self)

def display_inventory(self):
    pos = self.p.get_positions()
    sprite = self.p.get_animation("Down")
    img = self.images.get("inventory")

    self.window.blit(img.get("map"), (0 - pos[0], 0 - pos[1]))
    self.window.blit(sprite[1], (620, 400))
    self.window.blit(img.get("inventory"), (399, 301))

def display_map(self):
    pos = self.p.get_positions()
    sprite = self.p.get_animation("Down")
    img = self.images.get("in_game")

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
    self.window.blit(img.get("map"), (0 - pos[0], 0 - pos[1]))
    self.window.blit(sprite[self.index_animation], (620, 400))