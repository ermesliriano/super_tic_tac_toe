from importlib import resources
import pygame

class Game_intro_image:
    def __init__(self, file_path):
        with resources.path(file_path[0], file_path[1]) as intro_filename:
            self.image = pygame.image.load(intro_filename).convert_alpha()