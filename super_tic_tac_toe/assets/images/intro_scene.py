from importlib import resources
import pygame

class Intro_scene:
    def __init__(self, file_path, font, screen):
        self.__screen = screen
        self.__font = font
        self.__intro_text, self.__click_start_visible, self.__in_intro = "Click to start" , True, True
        with resources.path(file_path[0], file_path[1]) as intro_filename:
            self.image = pygame.image.load(intro_filename).convert_alpha()
        self.is_visible = True

    def run(self):
        if self.is_visible:
            click_start_txt = self.__font.render(self.__intro_text, True, (255,255,255))
            text_rect = click_start_txt.get_rect(center=(480/2,(480*0.90)))
            self.__screen.blit(self.image, (35,0))
            if self.__click_start_visible and self.__in_intro:
                self.__screen.blit(click_start_txt,text_rect)
                self.__click_start_visible = False
            else:
                 self.__click_start_visible = True

    def handle_input(self, key):
        if key == pygame.K_LEFT:
            self.last_direction = self.direction if self.direction == 'anyone' else None
            self.direction = 'left'
        if key == pygame.K_RIGHT:
            self.last_direction = self.direction if self.direction == 'anyone' else None
            self.direction = 'right'
        if key == pygame.K_SPACE:
            if self.direction == 'anyone':
                pass
            else:
                self.last_direction = self.direction
                self.direction = 'anyone'
    
    def set_start_scene(self, start_scene):
        self.__in_intro = False
        self.__start_scene = start_scene
        self.__start_scene.is_running = True