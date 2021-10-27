#imports
import pygame, pathlib, sys, fnmatch, os

from pygame.constants import NOEVENT
#local imports
from scripts.render import level_load as ll

#todo:
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
level_total = len(fnmatch.filter(os.listdir(dir + r'//Assets//levels'), '*dsm'))


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
    

    # loop start definement
    load_level_b = True
    print('load level ' + str(level))
    start = True
    temp_file = []
    # game loop
    while load_level_b:
        render_list, temp_file = level_load.render_load(level, dir, start, temp_file)
        if start:
            start = False
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
        if time_pass >= 1.5 and level != -1:
            time_pass = 0.0
            temp_file, column, row, objects = level_load.cycle_tick(temp_file, ['p'])
            if not False:
                try:
                    render_list[render_list.index(None)] = render_list[render_list.index(None) + 1][0].get_rect()
                    stop = True
                except(ValueError): None

            render_list[render_list.index('p')+ 1][0], render_list[render_list.index('p')+ 1][1] = column * 128 , row * 128
            screen.blit(render_list[render_list.index('p') + 2][0], render_list[render_list.index('p') + 1])

            #render_list[render_list.index('p') + 1][0] = render_list[render_list.index('p') + 1][0].move(movement)
        # render options
        else:            
            next = 0
            # render to screen
            for object in render_list: 
                
                if object == 'p' : next = 2
                elif next > 0: None
                else: next -= 1
                # try and catch place holders
                try: screen.blit(object[0], object[1])
                except(TypeError, IndexError): None

            # renders grids
            if level != -1:
                for column in range(128, 1408, 128):
                    pygame.draw.line(screen, (0,0,0), (column, 0), (column, 896), 1)
                for row in range(128, 896, 128):
                    pygame.draw.line(screen, (0,0,0), (0, row), (1408, row), 1)
                screen.blit(Run_button, (1405, 55))

            #render_list, temp_file = level_load.render_load(level, temp_file)


        # extra render options
        pygame.display.flip()