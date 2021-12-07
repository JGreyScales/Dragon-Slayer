import pygame

class level_load:
    def __init__(self, dir) -> None:
        self.traps = ['s']
        self.moveable = ['-', 'f']
        self.paths = {
            'f' : str(dir + r'//Assets//Props//backgrounds//clear_background.png'),
            '-' : str(dir + r'//Assets//Props//backgrounds//clear_background.png'),
            'x': str(dir + r'//Assets//Props//walls//wall[1].png'),
            'p' : str(dir + r'//Assets//Characters//knight.png'),
            's' : str(dir + r'//Assets//Traps//spikes.png')
        }

    def render_load(self, level, dir, start, temp, PL, inv) -> list:

        
        # define cleared renderlist
        render_list = []

        # reads from hexmap
        if start: 
            lines = open(dir + r'//Assets//levels//'+ str(level) + r'.dsm','r').readlines()

        # if level is already started 'read' from old snapshot
        else: lines = temp

        # converts hexmap to images / image cords
        row = 0
        for line in lines:
            column = 0
            if start: temp.append(line)
            for object in line:
                if object == 'p': 
                    # append background to images that do not have full 128x128 sizes
                    render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//Props//backgrounds//clear_background.png'), (128,128)), (column, row)])

                    
                    #place a holder in to find the players index
                    render_list.append('p')
                    render_list.append(None)
                
                try: render_list.append([pygame.transform.scale(pygame.image.load(self.paths.get(object)), (128, 128)), (column, row)])
                except(TypeError): None

                column += 128
            row += 128

        # render UI elements
        if level == -1:
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//UI//Play button.png'), (200, 75)), (604, 410.5)])
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//UI//Title.png'), (750, 100)), (329 , 174)])
            useable = []
        else:
            #add placeholder
            render_list.append('run')
            
            # render text boxes around items
            for item in [[70,896, 1408, 0], [68, 200, 1409, 28]]: 
                render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//UI//text.png'), (item[0],item[1])), (item[2], item[3])])

            # store useable traps in the level
            if start: useable = PL.gather_inventory(dir, level)
            else: useable = inv 

            #render useable traps to UI elements
            if len(useable) > 4: stop = 800
            else: stop = len(useable) * 200

            for trap in range(0, stop, 200):
                render_list.append([pygame.transform.scale(pygame.image.load(dir + r'//Assets//UI//text.png'), (68,200)), (1409, 228 + trap)])
                render_list.append([pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.paths['s']), (188,293)), 90), (1182, 235 + trap)])


        if temp[len(temp) - 1] == '\n': temp = temp[:len(temp) - 1]

        # return render list
        return [render_list, temp, useable]


    # inner clock
    def cycle_tick(self, map, direction, objects, run, win, render_traps) -> list:
        # 1 right, -1 left,      -1.0 down, 1.0 up

        # get player position in reference to temp hexmap
        for item in objects:
            for line in range(len(map)):
                try: 
                    row, column = line, map[line].index(item)
                    break
                except(ValueError): None
            else: print('PLAYER NOT FOUND, PLEASE FIX LEVEL (USE \'p\' IN LEVEL TO FIX). IF YOU HAVE NOT CREATED OR EDITED THE FILE. PLEASE REDOWNLOAD OR SELF REPAIR')

            for trap in render_traps: 
                cell_x, cell_y = trap[1][0] // 128, trap[1][1] // 128
                if column == cell_x and row == cell_y:
                    return [map, column, direction, row, objects, 3]
            # if player win, tell main.py to restart the level
            if win: return [map, column, direction, row, objects, 2]

            elif run:

                # player is moving horizontal
                if type(direction) == int:

                    # if player cannot move that way, rotate the player
                    if map[row][column + direction] not in self.moveable:
                        return level_load.cycle_tick(self, map, float(direction - (2 * direction)), objects, run, win, render_traps)
                    else:   
                        if map[row][column + direction] == 'f':
                            win = True
                        # create temp of map
                        temp, map[row], next = map[row], '', False
                        if direction < 0: temp = temp[::-1]
                        for i in temp:
                            # if is the object we are searching for, move it forwards one. if not do not also mamove
                            if i == item:
                                map[row] += '-'
                                next = True
                            elif next:
                                map[row] += item
                                next = False
                                
                            else: map[row] += i
                        #reverses render order if the player is moving left
                        if direction < 0: map[row] = map[row][::-1]
                
                # player is moving vertical
                elif type(direction) == float:
                    # convert movement direction to something easier to use
                    direction = int(direction - (direction * 2))

                    if map[row + direction][column] not in self.moveable: 
                        return level_load.cycle_tick(self, map, int(direction - (direction * 2)), objects, run, win, render_traps)
                    else:
                        # if player is on finish
                        if map[row + direction][column] == 'f':
                            win = True

                        if direction < 0:
                            start = line + direction
                            end = line + 1
                        else: 
                            start = line
                            end = line + (direction * 2)
                        temp = map[:start]

                        # remake the hexmap with moved pieces 
                        for line in map[start:end]:
                            updated_line = ''
                            for object in range(len(line)):
                                if object == column:
                                    if line[object] == 'p': updated_line += '-'
                                    else: updated_line += 'p'
                                else: updated_line += line[object]
                            temp.append(updated_line)

                        for line in map[end:]: temp.append(line)
                        map = temp[:]
                        direction = float(direction - (direction * 2))
                       
        return[map, column, direction, row, objects, win]