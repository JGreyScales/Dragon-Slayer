#imports
import pygame, pathlib, sys, time
#local imports
from scripts.level import level_load

#todo:
# add movement
# add UI
# add placing
# add detection
        
# pygame init
pygame.init()

# var define
# tuple define
size = width, height = 1478, 896

# string define
dir = str(pathlib.Path(__file__).parent.resolve())

# int define
level_total = 2

#function/class define
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#fonts
Run_button = pygame.transform.rotate(pygame.font.SysFont('arial', 68).render('RUN', False, (0, 0, 0)), 90)

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

            if level == -1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checks if player hits play button
                    if event.pos[0] >= 614 and event.pos[0] <= 790 and event.pos[1] >= 419 and event.pos[1] <= 473: load_level_b = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    None

                        
        # render to screen
        for object in render_list: screen.blit(object[0], object[1])
        
        screen.blit(Run_button, (1405, 55))

        # renders grid based system
        if level != -1:
            for column in range(128, 1408, 128):
                pygame.draw.line(screen, (0,0,0), (column, 0), (column, 896), 1)
            for row in range(128, 896, 128):
                pygame.draw.line(screen, (0,0,0), (0, row), (1408, row), 1)



        # extra render options
        pygame.display.flip()