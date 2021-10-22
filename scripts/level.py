import pygame


class level_load:
    def __init__(self) -> None:
        pass

    def render_load(level, dir):
        # define cleared renderlist
        render_list = []

        # load scene into render list
        if level is -1:
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\Play button.png'), (200, 75)), (540, 341)])
        
        # return render list
        return render_list