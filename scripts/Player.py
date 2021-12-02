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
        print(event, level, useable)