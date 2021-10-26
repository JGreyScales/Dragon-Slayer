#imports
import pygame, pathlib, sys, fnmatch, os
#local imports
from scripts.render import level_load as ll

#todo:
# add movement
# add placing
# add detection
        
pygame.init()

# var define
# tuple define
size = width, height = 1478, 896

# string define
dir = str(pathlib.Path(__file__).parent.resolve())

# int/float define
# gathers all levels from levels folder (this allows users to make their own levels and play them)
level_total = len(fnmatch.filter(os.listdir(dir + r'\\Assets\\levels'), '*dsm'))


getTicksLastFrame = 0
time_pass = 0.0

#function/class define
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
level_load = ll(dir)

#fonts
Run_button = pygame.transform.rotate(pygame.font.SysFont('arial', 68).render('RUN', True, (0, 0, 0)), 90)

# level loop
for level in range(-1, level_total - 1):
    # clear render_list and load current level
    render_list, temp_file = level_load.render_load(level, dir)

    # loop start definement
    load_level_b = True
    print('load level ' + str(level))

    # game loop
    while load_level_b:
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) /1000.0
        getTicksLastFrame = t
        time_pass += deltaTime



        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if level == -1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checks if player hits play button
                    if event.pos[0] >= 614 and event.pos[0] <= 790 and event.pos[1] >= 419 and event.pos[1] <= 473: load_level_b = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    None

        # creates inner gameclock
        if time_pass >= 0.5 and level != -1:
            movement, temp_file = level_load.cycle_tick(render_list, temp_file, ('p'))

            time_pass = 0.0
        # render options
        else:              
            # render to screen
            for object in render_list: 
                # try and catch to catch place holders
                try: screen.blit(object[0], object[1])
                except(TypeError, IndexError): None
            if level != -1:
                for column in range(128, 1408, 128):
                    pygame.draw.line(screen, (0,0,0), (column, 0), (column, 896), 1)
                for row in range(128, 896, 128):
                    pygame.draw.line(screen, (0,0,0), (0, row), (1408, row), 1)
                screen.blit(Run_button, (1405, 55))

        # renders grid based system




        # extra render options
        pygame.display.flip()