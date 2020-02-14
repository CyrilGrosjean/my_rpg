##
## EPITECH PROJECT, 2020
## detect key
## File description:
## detect_key
##

import pygame
from pygame.locals import *

keys = {"A": K_a, "B": K_b, "C": K_c, "D": K_d, "E": K_e, "F": K_f, "G": K_g, "H": K_h, "I": K_i, "J": K_j, "K": K_k, "L": K_l,
"M": K_m, "N": K_n, "O": K_o, "P": K_p, "Q": K_q, "R": K_r, "S": K_s, "T": K_t, "U": K_u, "V": K_v, "W": K_w, "X": K_x, "Y": K_y, "Z": K_z,
"0": K_0, "1": K_1, "2": K_2, "3": K_3, "4": K_4, "5": K_5, "6": K_6, "7": K_7, "8": K_8, "9": K_9, "Tab": K_TAB, "MAJ": K_CAPSLOCK, "LSHIFT": K_LSHIFT,
"LCTRL": K_LCTRL, ")": K_RIGHTPAREN, "MENU": K_MENU, "ALT": K_LALT, ",": K_COMMA, ";": K_SEMICOLON, ":": K_COLON, "!": K_EXCLAIM, "ALTGR": K_RALT, "RCTRL": K_RCTRL,
"UP": K_UP, "DOWN": K_DOWN, "LEFT": K_LEFT, "RIGHT": K_RIGHT, "RSHIFT": K_RSHIFT, "RETURN": K_RETURN, "DEL": K_DELETE, "ESCAPE": K_ESCAPE,
"F1": K_F1, "F2": K_F2, "F3": K_F3, "F4": K_F4, "F5": K_F5, "F6": K_F6, "F7": K_F7, "F8": K_F8, "F9": K_F9, "F10": K_F10, "F11": K_F11, "F12": K_F12,
"F13": K_F13, "F14": K_F14, "F15": K_F15, "=": K_EQUALS}

def check_this_key(key):
    global keys

    name = ""
    for i in keys.keys():
        if keys.get(i) == key:
            name = i
            break
    return name