##
## EPITECH PROJECT, 2020
## event
## File description:
## functions event
##

import pygame
from pygame.locals import *
import save
import detect_key

def event_main_menu(event, self):
    if event.type == MOUSEBUTTONDOWN:
        if self.mouse[0] >= 610 and self.mouse[0] <= 700 and self.mouse[1] >= 315 and self.mouse[1] <= 345:
            self.fen, self.page = 1, 0
            pygame.mixer.music.stop()
        if self.mouse[0] >= 610 and self.mouse[0] <= 705 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
            save.load(self, "file1")
            self.fen, self.page = 1, 0
            # self.fen, self.page = 0, 1
        if self.mouse[0] >= 610 and self.mouse[0] <= 760 and self.mouse[1] >= 515 and self.mouse[1] <= 545:
            self.change_key = [False, False, False, False, False, False, False, False]
            self.fen, self.page = 0, 2
        if self.mouse[0] >= 610 and self.mouse[0] <= 690 and self.mouse[1] >= 615 and self.mouse[1] <= 645:
            exit(0)
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            exit(0)
    if event.type == QUIT:
        exit(0)

def event_options(event, self):
    try:
        if self.change_key[2]:
            pass
    except:
        self.change_key = [False, False, False, False, False, False, False, False]
    if event.type == QUIT:
        exit(0)
    if event.type == MOUSEBUTTONDOWN:
        if True not in self.change_key:
            if self.mouse[0] >= 400 and self.mouse[0] <= 450 and self.mouse[1] >= 260 and self.mouse[1] <= 300:
                self.change_key[0] = True
            if self.mouse[0] >= 400 and self.mouse[0] <= 515 and self.mouse[1] >= 310 and self.mouse[1] <= 345:
                self.change_key[1] = True
            if self.mouse[0] >= 400 and self.mouse[0] <= 490 and self.mouse[1] >= 360 and self.mouse[1] <= 400:
                self.change_key[2] = True
            if self.mouse[0] >= 400 and self.mouse[0] <= 505 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
                self.change_key[3] = True
            if self.mouse[0] >= 400 and self.mouse[0] <= 600 and self.mouse[1] >= 460 and self.mouse[1] <= 505:
                self.change_key[4] = True
            if self.mouse[0] >= 400 and self.mouse[0] <= 515 and self.mouse[1] >= 510 and self.mouse[1] <= 545:
                self.change_key[5] = True
            if self.mouse[0] >= 400 and self.mouse[0] <= 530 and self.mouse[1] >= 565 and self.mouse[1] <= 595:
                self.change_key[6] = True
            if self.mouse[0] >= 400 and self.mouse[0] <= 500 and self.mouse[1] >= 610 and self.mouse[1] <= 645:
                self.change_key[7] = True
            if self.mouse[0] >= 610 and self.mouse[0] <= 710 and self.mouse[1] >= 710 and self.mouse[1] <= 745:
                del self.change_key
                self.fen, self.page = 0, 0
    if event.type == KEYDOWN:
        if True in self.change_key:
            if self.change_key[0]:
                self.option.change_key("Up", event.key)
                self.change_key[0] = False
            if self.change_key[1]:
                self.option.change_key("Down", event.key)
                self.change_key[1] = False
            if self.change_key[2]:
                self.option.change_key("Left", event.key)
                self.change_key[2] = False
            if self.change_key[3]:
                self.option.change_key("Right", event.key)
                self.change_key[3] = False
            if self.change_key[4]:
                self.option.change_key("Inventory", event.key)
                self.change_key[4] = False
            if self.change_key[5]:
                self.option.change_key("Menu", event.key)
                self.change_key[5] = False
            if self.change_key[6]:
                self.option.change_key("Action", event.key)
                self.change_key[6] = False
            if self.change_key[7]:
                self.option.change_key("Dash", event.key)
                self.change_key[7] = False


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
        if event.key == self.option.get_key("Dash"):
            self.move_keys[4] = True
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
        if event.key == self.option.get_key("Dash"):
            self.move_keys[4] = False
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
                self.move_keys = [False, False, False, False, False]
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