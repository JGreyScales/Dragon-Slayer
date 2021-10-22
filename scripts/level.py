import pygame


class level_load:
    def __init__(self) -> None:
        pass

    def render_load(level, dir):
        # define cleared renderlist
        render_list = []

        # load scene into render list
        if level is -1:

            for column in range(0, 768, 128):
                for row in range(0, 1281, 128):
                    render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\Props\\backgrounds\\clear_background.png'), (128, 128)), (row, column)])
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\Play button.png'), (200, 75)), (540, 341)])
            render_list.append([pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\Title.png'), (750, 100)), (265,149)])


        
        # return render list
        return render_list