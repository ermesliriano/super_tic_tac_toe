from importlib import resources
import pygame
from super_tic_tac_toe.assets.start_scene import Start_scene
from super_tic_tac_toe.config import cfg_item
from super_tic_tac_toe.assets.images.intro_scene import Intro_scene


class Game:
    def __init__(self):
        pygame.init()
        
        self.__screen = pygame.display.set_mode(cfg_item("game", "screen_size"), 0, 32)
        pygame.display.set_caption(cfg_item("game","title"))
        
        self.__clock = pygame.time.Clock()
        self.delta_time = 0
        self.last_update = pygame.time.get_ticks()

        self.__font_path = cfg_item("font", "file")
        with resources.path(self.__font_path[0], self.__font_path[1]) as font_path:
            self.__font = pygame.font.Font(font_path, 36)
        
        self.__intro_scene = Intro_scene(cfg_item("entities","intro_file"), self.__font, self.__screen)
        self.__start_scene = Start_scene(self.__font, self.__screen)

        self.__is_running = False

    def run(self):
        self.__is_running = True

        while self.__is_running:
            self.__clock.tick(3)
            self.handle()
            self.render()

    def handle(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__intro_scene.set_start_scene(self.__start_scene)
                self.__start_scene.handle_mouse_click(x, y, self.__intro_scene, self.__start_scene)
                
        

    def render(self):
            self.__screen.fill(cfg_item("game","bg_color"))
            self.__intro_scene.run()
            self.__start_scene.run()

            now = pygame.time.get_ticks()
            self.delta_time = (now - self.last_update) / 1000.0

            pygame.display.flip()
            pygame.display.update()

    pygame.quit()