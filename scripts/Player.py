import pygame

class player():
    def __init__(self) -> None:
        pass

    def gather_inventory(dir, level, inventory = []):
        for line in open(dir + r'//Assets//levels//'+ str(level) + r'.inv','r').readlines():
            for trap in line:
                inventory.append(trap)
        return inventory

    def place_trap(event, level_loaded, useable, dir:str, render_traps:list, placeable = True):

        # to do, find proper rotation of object, append object with proper rotation to render_list. Bing Bang Bong shit done

        traps = {
            's' : str(dir + r'//Assets//Traps//spikes.png')
        }
        if len(useable) == 0: return None
        cell_X, cell_Y = event.pos[0] // 128, event.pos[1] //128
        # if player is clicking in the UI do not place trap
        if cell_X >= 11: return None
        # checks that the placement is valid by checking what tile is being interacted with and if the surrounding tiles are walls
        if level_loaded[cell_Y][cell_X] != 'x':
            for i in (1,-1):
                try:
                   if level_loaded[cell_Y + i][cell_X] == 'x':
                         if i == 1: placeable = False

                         else: placeable = 180
                         break
                except(IndexError): None
                try:
                    if level_loaded[cell_Y][cell_X + i] == 'x':
                         if i == 1: placeable = 90
                         else: placeable = 270
                         break
                except(IndexError): None
            if placeable != True:
                render_traps.append([pygame.transform.rotate(pygame.transform.scale(pygame.image.load(traps[useable[0]]), (128, 128)), placeable), (cell_X * 128, cell_Y * 128)])
                # render to screen
                return [useable[1:], render_traps]
        return [useable, render_traps]
            