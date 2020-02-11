##
## EPITECH PROJECT, 2020
## event
## File description:
## functions event
##

import pygame
from pygame.locals import *
import save

def event_main_menu(event, self):
    if event.type == MOUSEBUTTONDOWN:
        if self.mouse[0] >= 610 and self.mouse[0] <= 700 and self.mouse[1] >= 315 and self.mouse[1] <= 345:
            self.fen, self.page = 1, 0
            pygame.mixer.music.stop()
        if self.mouse[0] >= 610 and self.mouse[0] <= 705 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
            # self.fen, self.page = 0, 1
            save.load(self, "file1")
        if self.mouse[0] >= 610 and self.mouse[0] <= 690 and self.mouse[1] >= 515 and self.mouse[1] <= 545:
            exit(0)
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            exit(0)
    if event.type == QUIT:
        exit(0)

def event_options(event, self):
    if event.type == QUIT:
        exit(0)
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            exit(0)

def event_game(event, self):
    if event.type == KEYDOWN:
        if event.key == self.option.get_key("Up"):
            self.move_keys[0] = True
        if event.key == self.option.get_key("Down"):
            self.move_keys[1] = True
        if event.key == self.option.get_key("Left"):
            self.move_keys[2] = True
        if event.key == self.option.get_key("Right"):
            self.move_keys[3] = True
        if event.key == self.option.get_key("Menu"):
            if not self.keys.get("Escape"):
                img = self.images.get("menu_in_game")
                self.size = 4
                for i in img.keys():
                    if i != "map" and i != "alt_menu":
                        self.images["menu_in_game"].get(i).set_alpha(0)
                self.keys["Escape"] = True
                self.page = 1
        if event.key == self.option.get_key("Inventory"):
            if not self.keys.get("Inventory"):
                self.keys["Inventory"] = True
                self.page = 2
    if event.type == KEYUP:
        if event.key == self.option.get_key("Up"):
            self.move_keys[0] = False
        if event.key == self.option.get_key("Down"):
            self.move_keys[1] = False
        if event.key == self.option.get_key("Left"):
            self.move_keys[2] = False
        if event.key == self.option.get_key("Right"):
            self.move_keys[3] = False
        if event.key == self.option.get_key("Menu"):
            self.keys["Escape"] = False
        if event.key == self.option.get_key("Inventory"):
            self.keys["Inventory"] = False
    if event.type == QUIT:
        exit(0)

def event_menu(event, self):
    if event.type == QUIT:
        exit(0)
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if mouse[0] >= 590 and mouse[0] <= 620 and mouse[1] >= 360 and mouse[1] <= 390:
            self.page = 2
        if mouse[0] >= 670 and mouse[0] <= 700 and mouse[1] >= 365 and mouse[1] <= 390:
            print("Equip")
        if mouse[0] >= 560 and mouse[0] <= 590 and mouse[1] >= 435 and mouse[1] <= 460:
            save.save(self, "file1")
        if mouse[0] >= 690 and mouse[0] <= 720 and mouse[1] >= 435 and mouse[1] <= 460:
            print("Quests")
        if mouse[0] >= 630 and mouse[0] <= 660 and mouse[1] >= 480 and mouse[1] <= 510:
            self.fen = 0
            self.page = 0
    if event.type == KEYUP:
        if event.key == self.option.get_key("Menu"):
            self.keys["Escape"] = False
    if event.type == KEYDOWN:
        if event.key == self.option.get_key("Menu"):
            if not self.keys.get("Escape"):
                self.page = 0
                self.move_keys = [False, False, False, False]
                self.keys["Escape"] = True

def event_inventory(event, self):
    if event.type == QUIT:
        exit(0)
    if event.type == KEYUP:
        if event.key == self.option.get_key("Inventory"):
            self.keys["Inventory"] = False
    if event.type == KEYDOWN:
        if event.key == self.option.get_key("Inventory"):
            if not self.keys.get("Inventory"):
                self.page = 0
                self.move_keys = [False, False, False, False]
                self.keys["Inventory"] = True
        if event.key == self.option.get_key("Menu"):
            self.keys["Escape"] = True
            self.page = 0
            self.move_keys = [False, False, False, False]