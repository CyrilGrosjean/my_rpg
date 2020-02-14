##
## EPITECH PROJECT, 2020
## animations
## File description:
## functions animation
##

import pygame
from pygame.locals import *

def animation_menu(self, img):
    if img["inventory"].get_alpha() < 255:
        img["inventory"].set_alpha(img["inventory"].get_alpha() + 30)
    elif img["save"].get_alpha() < 255:
        img["save"].set_alpha(img["save"].get_alpha() + 30)
    elif img["option"].get_alpha() < 255:
        img["option"].set_alpha(img["option"].get_alpha() + 30)
    elif img["quit"].get_alpha() < 255:
        img["quit"].set_alpha(img["quit"].get_alpha() + 30)
    elif img["quests"].get_alpha() < 255:
        img["quests"].set_alpha(img["quests"].get_alpha() + 30)
    elif img["equip"].get_alpha() < 255:
        img["equip"].set_alpha(img["equip"].get_alpha() + 30)

def display_text_menu(self):
    mouse = pygame.mouse.get_pos()

    if mouse[0] >= 590 and mouse[0] <= 620 and mouse[1] >= 360 and mouse[1] <= 390:
        text = self.small_font.render("Inventory", 1, (255, 255, 255))
        self.window.blit(text, (570, 400))
    if mouse[0] >= 670 and mouse[0] <= 700 and mouse[1] >= 365 and mouse[1] <= 390:
        text = self.small_font.render("Equip", 1, (255, 255, 255))
        self.window.blit(text, (665, 400))
    if mouse[0] >= 560 and mouse[0] <= 590 and mouse[1] >= 435 and mouse[1] <= 460:
        text = self.small_font.render("Save", 1, (255, 255, 255))
        self.window.blit(text, (560, 470))
    if mouse[0] >= 690 and mouse[0] <= 720 and mouse[1] >= 435 and mouse[1] <= 460:
        text = self.small_font.render("Quests", 1, (255, 255, 255))
        self.window.blit(text, (685, 470))
    if mouse[0] >= 590 and mouse[0] <= 620 and mouse[1] >= 500 and mouse[1] <= 530:
        text = self.small_font.render("Options", 1, (255, 255, 255))
        self.window.blit(text, (583, 540))
    if mouse[0] >= 670 and mouse[0] <= 700 and mouse[1] >= 500 and mouse[1] <= 530: # 40, 70
        text = self.small_font.render("Quit", 1, (255, 255, 255))
        self.window.blit(text, (672, 540))