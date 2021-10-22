import pygame, pathlib, sys

from scripts.level import level_load

pygame.init()


dir = str(pathlib.Path(__file__).parent.resolve())

size = width, height = 1280, 960
screen = pygame.display.set_mode(size)

level_total = 1

clock = pygame.time.Clock()
for level in range(-1, level_total - 1):
    render_list = []

    if level is -1:
        render_list = level_load.render_load(i, dir)
        print(548,348  , 722, 400)

    load_level = True
    while load_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if level is -1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >= 548 and event.pos[0] <= 722 and event.pos[1] >= 348 and event.pos[1] <= 400:
                        load_level == False
        
        screen.fill((150,150,150))
        for object in render_list:
            screen.blit(object[0], object[1])

        pygame.display.flip()
        clock.tick(60)
