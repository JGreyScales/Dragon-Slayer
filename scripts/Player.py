class player():
    def __init__(self) -> None:
        pass

    def gather_inventory(dir, level):
        inventory = []
        for line in open(dir + r'//Assets//levels//'+ str(level) + r'.inv','r').readlines():
            for trap in line:
                inventory.append(trap)
        return inventory

    def place_trap(event, level_loaded, useable, placeable = False):
        cell_X, cell_Y = event.pos[0] // 128, event.pos[1] //128
        if cell_X >= 11: return useable

        # checks that the placement is valid by checking what tile is being interacted with and if the surrounding tiles are walls
        if level_loaded[cell_Y][cell_X] != 'x':
            for i in (1,-1):
                try:
                    if level_loaded[cell_Y][cell_X + i] == 'x': placeable = True
                except(IndexError): None
                try:
                    if level_loaded[cell_Y + i][cell_X] == 'x': placeable = True
                except(IndexError): None
            print(placeable)

        # if player is clicking in the UI do not place trap

