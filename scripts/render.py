from os import write
from posixpath import expanduser
from typing import List
import pygame


class level_load:
    def __init__(self, dir) -> None:
        f = open(dir + r'\\Assets\\TEMP.dsm', 'w+')

    def render_load(self, level, dir, *screen) -> list:
        
        paths = {
            '-' : str(dir + r'\\Assets\\Props\\backgrounds\\clear_background.png'),
            'x': str(dir + r'\\Assets\\Props\\walls\\wall[1].png'),
            'p' : str(dir + r'\\Assets\\Characters\\knight.png')
        }
        # define cleared renderlist
        render_list = []

        # reads from hexmap
        lines = open(dir + r'\\Assets\\levels\\'+ str(level) + r'.dsm','r').readlines()
        temp =  []

        #temp.seek(0)
       # temp.truncate()

        # converts hexmap to images / image cords
        row = 0
        for line in lines:
            column = 0
            temp.append(line)
            for object in line:
                if object == 'p': 
                    # append background to images that do not have full 128x128 sizes
                    render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\Props\\backgrounds\\clear_background.png'), (128,128)), (column, row)])
                    
                    #place a holder in to find the players index
                    render_list.append('p')

                
                try: render_list.append([pygame.transform.scale(pygame.image.load(paths.get(object)), (128, 128)), (column, row)])
                except(TypeError): None

                column += 128
            row += 128

        # load scene into render list
        if level == -1:
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\Play button.png'), (200, 75)), (604, 410.5)])
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\Title.png'), (750, 100)), (329 , 174)])
        else:
            # player UI (right side)
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\text.png'), (70,896)), (1408, 0)])
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\text.png'), (68, 200)), (1409, 28)])


        # return render listwhat 
        return [render_list, temp]


    # inner clock
    def cycle_tick(self, list, map, *objects) -> List:
        for line in range(len(map)):
            try: 
                row, column = line, map[line].index('p')
                break
            except(ValueError): None
        else:
            print('PLAYER NOT FOUND, PLEASE FIX LEVEL (USE \'p\' IN LEVEL TO FIX). IF YOU HAVE NOT CREATED OR EDITED THE FILE. PLEASE REDOWNLOAD OR SELF REPAIR')

        move = None
        return[move, map]






# def break_point():
#     print('a')**
#     try:
#         break_point()
#     except(RecursionError):
#         break_catch()
# def break_catch():
#     try:
#         breakpoint()
#     except(RecursionError):
#         break_catch()


# break_point()