import pygame

from super_tic_tac_toe.config import cfg_item


class Game:
    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(cfg_item("game", "screen_size"), 0, 32)
        pygame.display.set_caption(cfg_item("game","caption"))