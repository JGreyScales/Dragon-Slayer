import pygame


class level_load:
    def __init__(self) -> None:
        pass

    def render_load(level, dir):
        render_list = []

        if level is -1:
            play_button = [pygame.transform.scale(pygame.image.load(dir + r'\\Assets\\UI\\Play button.png'), (200, 75)), (540, 341)]
            play_button.append(play_button[0].get_rect())
            render_list.append(play_button)
            
        return render_list