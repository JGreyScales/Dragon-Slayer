import pygame

# to do, add rotation to player
# to do, add movement
class level_load:
    def __init__(self, dir) -> None:
        None

    def render_load(self, level, dir, start, temp) -> list:

        
        paths = {
            '-' : str(dir + r'//Assets//Props//backgrounds//clear_background.png'),
            'x': str(dir + r'//Assets//Props//walls//wall[1].png'),
            'p' : str(dir + r'//Assets//Characters//knight.png')
        }
        # define cleared renderlist
        render_list = []

        # reads from hexmap
        if start:
            lines = open(dir + r'//Assets//levels//'+ str(level) + r'.dsm','r').readlines()
        else:
            lines = temp


        #temp.seek(0)
       # temp.truncate()

        # converts hexmap to images / image cords
        row = 0
        for line in lines:
            column = 0
            if start:
                temp.append(line)
            for object in line:
                if object == 'p': 
                    # append background to images that do not have full 128x128 sizes
                    render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//Props//backgrounds//clear_background.png'), (128,128)), (column, row)])

                    
                    #place a holder in to find the players index
                    render_list.append('p')
                    render_list.append(None)
                
                try: render_list.append([pygame.transform.scale(pygame.image.load(paths.get(object)), (128, 128)), (column, row)])
                except(TypeError): None

                column += 128
            row += 128

        # load scene into render list
        if level == -1:
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//UI//Play button.png'), (200, 75)), (604, 410.5)])
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//UI//Title.png'), (750, 100)), (329 , 174)])
        else:
            # player UI (right side)
            for item in [[70,896, 1408, 0], [68, 200, 1409, 28]]:
                render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//UI//text.png'), (item[0],item[1])), (item[2], item[3])])

        if temp[len(temp) - 1] == '\n': temp = temp[:len(temp) - 1]
        # return render listwhat 
        return [render_list, temp]


    # inner clock
    def cycle_tick(self, map, movement, objects) -> tuple:
        # 0 right, 1 left, 2 down, 3 up
        for item in objects:
            for line in range(len(map)):
                try: 
                    row, column = line, map[line].index(item)
                    break
                except(ValueError): None
            else: print('PLAYER NOT FOUND, PLEASE FIX LEVEL (USE \'p\' IN LEVEL TO FIX). IF YOU HAVE NOT CREATED OR EDITED THE FILE. PLEASE REDOWNLOAD OR SELF REPAIR')


                # if players next move is not a background wall
            if map[row][column+ 1] != '-':
                print('Nonemoveable') #rotate player 90 to the right and move in said direction
            else:   

                # create temp of map
                temp = map[row]
                map[row] = ''
                next = False

                for i in temp:
                    # if is the object we are searching for, move it forwards one. if not 
                    if i == item:
                        map[row] += '-'
                        next = True
                    elif next:
                        map[row] += item
                        next = False
                    else:
                        map[row] += i
        return[map, column, row, objects]




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

# TO FIND WHERE PLAYER CLICKS. TAKE THE FLOOR DIVSION OF PLAYER POS (X,Y) / (128,128)