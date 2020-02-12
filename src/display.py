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
import movement
import monster
import detect_key
from math import floor

def display_main_menu(self):
    new_text = self.font.render("New", 1, (255, 255, 255))
    load_text = self.font.render("Load", 1, (255, 255, 255))
    option_text = self.font.render("Options", 1, (255, 255, 255))
    quit_text = self.font.render("Quit", 1, (255, 255, 255))
    img = self.images.get("main_menu")

    if self.mouse[0] >= 610 and self.mouse[0] <= 700 and self.mouse[1] >= 315 and self.mouse[1] <= 345:
        new_text = self.font.render("New", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 705 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
        load_text = self.font.render("Load", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 760 and self.mouse[1] >= 515 and self.mouse[1] <= 545:
        option_text = self.font.render("Options", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 690 and self.mouse[1] >= 615 and self.mouse[1] <= 645:
        quit_text = self.font.render("Quit", 1, (255, 0, 0))
    self.window.blit(img.get("background"), (0, 0))
    self.window.blit(img.get("logo"), (450, 0))
    self.window.blit(new_text, (610, 300))
    self.window.blit(load_text, (610, 400))
    self.window.blit(option_text, (610, 500))
    self.window.blit(quit_text, (610, 600))

def display_options(self):
    img = self.images.get("main_option")
    up = self.font.render("Up", 1, (255, 255, 255))
    down = self.font.render("Down", 1, (255, 255, 255))
    left = self.font.render("Left", 1, (255, 255, 255))
    right = self.font.render("Right", 1, (255, 255, 255))
    inventory = self.font.render("Inventory", 1, (255, 255, 255))
    menu = self.font.render("Menu", 1, (255, 255, 255))
    action = self.font.render("Action", 1, (255, 255, 255))
    dash = self.font.render("Dash", 1, (255, 255, 255))
    back = self.font.render("Back", 1, (255, 255, 255))
    up_key = self.font.render(detect_key.check_this_key(self.option.get_key("Up")), 1, (255, 255, 255))
    down_key = self.font.render(detect_key.check_this_key(self.option.get_key("Down")), 1, (255, 255, 255))
    left_key = self.font.render(detect_key.check_this_key(self.option.get_key("Left")), 1, (255, 255, 255))
    right_key = self.font.render(detect_key.check_this_key(self.option.get_key("Right")), 1, (255, 255, 255))
    inventory_key = self.font.render(detect_key.check_this_key(self.option.get_key("Inventory")), 1, (255, 255, 255))
    menu_key = self.font.render(detect_key.check_this_key(self.option.get_key("Menu")), 1, (255, 255, 255))
    action_key = self.font.render(detect_key.check_this_key(self.option.get_key("Action")), 1, (255, 255, 255))
    dash_key = self.font.render(detect_key.check_this_key(self.option.get_key("Dash")), 1, (255, 255, 255))

    if self.mouse[0] >= 610 and self.mouse[0] <= 710 and self.mouse[1] >= 710 and self.mouse[1] <= 745:
        back = self.font.render("Back", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 450 and self.mouse[1] >= 260 and self.mouse[1] <= 300 or self.change_key[0]:
        up = self.font.render("Up", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 515 and self.mouse[1] >= 310 and self.mouse[1] <= 345 or self.change_key[1]:
        down = self.font.render("Down", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 490 and self.mouse[1] >= 360 and self.mouse[1] <= 400 or self.change_key[2]:
        left = self.font.render("Left", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 505 and self.mouse[1] >= 410 and self.mouse[1] <= 445 or self.change_key[3]:
        right = self.font.render("Right", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 600 and self.mouse[1] >= 460 and self.mouse[1] <= 505 or self.change_key[4]:
        inventory = self.font.render("Inventory", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 515 and self.mouse[1] >= 510 and self.mouse[1] <= 545 or self.change_key[5]:
        menu = self.font.render("Menu", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 530 and self.mouse[1] >= 565 and self.mouse[1] <= 595 or self.change_key[6]:
        action = self.font.render("Action", 1, (255, 0, 0))
    if self.mouse[0] >= 400 and self.mouse[0] <= 500 and self.mouse[1] >= 610 and self.mouse[1] <= 645 or self.change_key[7]:
        dash = self.font.render("Dash", 1, (255, 0, 0))

    self.window.blit(img.get("background"), (0, 0))
    self.window.blit(img.get("logo"), (450, 0))
    self.window.blit(up, (400, 250))
    self.window.blit(up_key, (700, 250))
    self.window.blit(down, (400, 300))
    self.window.blit(down_key, (700, 300))
    self.window.blit(left, (400, 350))
    self.window.blit(left_key, (700, 350))
    self.window.blit(right, (400, 400))
    self.window.blit(right_key, (700, 400))
    self.window.blit(inventory, (400, 450))
    self.window.blit(inventory_key, (700, 450))
    self.window.blit(menu, (400, 500))
    self.window.blit(menu_key, (700, 500))
    self.window.blit(action, (400, 550))
    self.window.blit(action_key, (700, 550))
    self.window.blit(dash, (400, 600))
    self.window.blit(dash_key, (700, 600))
    self.window.blit(back, (610, 700))

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
    p_health = self.p.get_player_info("Health")
    max_health = self.p.get_player_info("MaxHealth")
    pos, sprite = movement.check_movement(self)
    pos = collision.check_collision(self, pos)

    self.p.change_positions(pos[0], pos[1])
    self.window.blit(img.get("map"), (0 - pos[0], 0 - pos[1]))
    for i in self.mobs:
        anim = i.get_animation("Down")
        self.window.blit(anim[1], (i.pos[0] - pos[0], i.pos[1] - pos[1]))
    self.window.blit(img.get("empty_bar"), (1110, 760), (0, 0, 100, 25))
    self.window.blit(img.get("heal_bar"), (1110, 760), (0, 0, floor(p_health / max_health * 100), 25))
    self.window.blit(sprite[self.index_animation], (620, 400))