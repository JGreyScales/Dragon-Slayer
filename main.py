#imports
import pygame, pathlib, sys, time
#local imports
from scripts.level import level_load


        
# pygame init
pygame.init()

# var define
# tuple define
size = width, height = 1408, 896

# array assignment


# string define
dir = str(pathlib.Path(__file__).parent.resolve())

# int define
level_total = 2

#function/class define
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# level loop
for level in range(-1, level_total - 1):
    # clear render_list and load current level
    render_list = level_load.render_load(level, dir)

    # loop start definement
    load_level_b = True
    print('load level ' + str(level))

    # game loop
    while load_level_b:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if level is -1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checks if player hits play button
                    if event.pos[0] >= 614 and event.pos[0] <= 790 and event.pos[1] >= 419 and event.pos[1] <= 473:
                        load_level_b = False

                        
        # render to screen
        screen.fill((150,150,150))
        for object in render_list:
         screen.blit(object[0], object[1])

        # renders grid based system
        if level != -1:
            for column in range(128, 1408, 128):
                pygame.draw.line(screen, (0,0,0), (column, 0), (column, 896), 1)
            for row in range(128, 896, 128):
                pygame.draw.line(screen, (0,0,0), (0, row), (1408, row), 1)



        # extra render options
        pygame.display.flip()
        clock.tick(60)
