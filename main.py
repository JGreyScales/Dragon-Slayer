import pygame, pathlib, sys

from scripts.level import level_load

pygame.init()


dir = str(pathlib.Path(__file__).parent.resolve())

size = width, height = 1280, 960
screen = pygame.display.set_mode(size)

level_total = 1

clock = pygame.time.Clock()
for i in range(-1, level_total - 1):
    render_list = []

    if i is -1:
        print(level_load.render_load(i, dir))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if i is -1:
            None
        
        screen.fill((150,150,150))

        pygame.display.flip()
        clock.tick(60)
