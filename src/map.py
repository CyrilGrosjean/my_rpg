##
## EPITECH PROJECT, 2020
## map
## File description:
## functions to create map collision
##

def get_map(map):
    text = "data/maps/" + map
    file = open(text, "r")
    map_read = file.read()
    file.close()
    del text
    map_coords = map_read.split("\n")
    my_map = []
    for i in map_coords:
        my_map.append([])
        for a in i:
            my_map[-1].append(int(a))
    del map_coords
    return my_map