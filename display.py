##
## EPITECH PROJECT, 2020
## display
## File description:
## display function
##

import pygame
from pygame.locals import *

def display_main_menu(self):
    img = pygame.image.load("data/img/menu.jpg")
    logo = pygame.image.load("data/img/logo.png")
    new_text = self.font.render("New", 1, (255, 255, 255))
    load_text = self.font.render("Load", 1, (255, 255, 255))
    quit_text = self.font.render("Quit", 1, (255, 255, 255))

    if self.mouse[0] >= 610 and self.mouse[0] <= 700 and self.mouse[1] >= 315 and self.mouse[1] <= 345:
        new_text = self.font.render("New", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 705 and self.mouse[1] >= 410 and self.mouse[1] <= 445:
        load_text = self.font.render("Load", 1, (255, 0, 0))
    if self.mouse[0] >= 610 and self.mouse[0] <= 690 and self.mouse[1] >= 515 and self.mouse[1] <= 545:
        quit_text = self.font.render("Quit", 1, (255, 0, 0))
    self.window.blit(img, (0, 0))
    self.window.blit(logo, (450, 0))
    self.window.blit(new_text, (610, 300))
    self.window.blit(load_text, (610, 400))
    self.window.blit(quit_text, (610, 500))

def display_options(self):
    img = pygame.image.load("data/img/menu.jpg")
    logo = pygame.image.load("data/img/logo.png")

    self.window.blit(img, (0, 0))
    self.window.blit(logo, (450, 0))

def display_map(self):
    img = pygame.image.load("data/maps/map1.png", )