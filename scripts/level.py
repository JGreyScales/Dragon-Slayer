import pygame


class level_load:
    def __init__(self) -> None:
        pass

    def render_load(level, dir):
        render_list = []

        if level is -1:
            play_button = [pygame.image.load(dir + r'\\Assets\\UI\\Play button.png'), (640, 120)]
            render_list.append(play_button)
            
        return render_list