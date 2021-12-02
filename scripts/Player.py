class player():
    def __init__(self) -> None:
        pass

    def gather_inventory(dir, level):
        inventory = []
        for line in open(dir + r'//Assets//levels//'+ str(level) + r'.inv','r').readlines():
            for trap in line:
                inventory.append(trap)
        return inventory

    def place_trap(event, level, useable):
        cell_X, cell_Y = event.pos[0] // 128, event.pos[1] //128
        if cell_X >= 11: return useable
