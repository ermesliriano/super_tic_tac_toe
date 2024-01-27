import pygame

from super_tic_tac_toe.assets.board import Board
from super_tic_tac_toe.assets.logic import Logic


class Start_scene:
    
    def __init__(self, font, screen):
        self.__one_player_txt = "1 player"
        self.__two_player_txt = "2 players"
        self.__screen = screen
        self.__font = font
        self.is_running = False
        self.is_visible = True
        self.board = None
        self.mode_selected = True
        
    def run(self):
        if self.is_running and self.is_visible:
            x, y = pygame.mouse.get_pos()

            player_one = self.__font.render(self.__one_player_txt, True, (255, 255, 255))
            player_two = self.__font.render(self.__two_player_txt, True, (255, 255, 255))
            
            p1_rect = player_one.get_rect(center=(480 / 2, (480 * 0.83)))
            p2_rect = player_two.get_rect(center=(480 / 2, (480 * 0.93)))
            
            bg_rect = pygame.Rect(120, 370, 240, 100)
            pygame.draw.rect(self.__screen, (0,0,0), bg_rect)

            if p1_rect.collidepoint((x, y)):
                player_one = self.__font.render(self.__one_player_txt, True, (255, 0, 0))
            if p2_rect.collidepoint((x, y)):
                player_two = self.__font.render(self.__two_player_txt, True, (255, 0, 0))

            self.__screen.blit(player_one, p1_rect)
            self.__screen.blit(player_two, p2_rect)
        
        if self.board != None:
            if self.board.is_running:
                self.board.draw()

    def handle_mouse_click(self, x, y, intro, start):
        self.__start_scene = start
        self.__intro_scene = intro
        p1_rect = self.__font.render(self.__one_player_txt, True, (255, 255, 255)).get_rect(center=(480 / 2, (480 * 0.83)))
        p2_rect = self.__font.render(self.__two_player_txt, True, (255, 255, 255)).get_rect(center=(480 / 2, (480 * 0.93)))

        if p1_rect.collidepoint((x, y)):
            self.one_player_mode()
        elif p2_rect.collidepoint((x, y)):
            self.two_player_mode()
        
        if not self.__start_scene.is_visible and not self.__intro_scene.is_visible:
            self.board.handle_click(x, y)

    def one_player_mode(self):
        if self.mode_selected:
            print("Modo de 1 jugador seleccionado.")
            self.is_visible = False
            self.__start_scene.is_visible = False
            self.__intro_scene.is_visible = False
            self.board = Board(self.__screen, self.__font)
            self.logic = Logic(self.board)
            self.mode_selected = False

    def two_player_mode(self):
        if self.mode_selected:
            print("Modo de 2 jugadores seleccionado.")
            self.is_visible = False
            self.__start_scene.is_visible = False
            self.__intro_scene.is_visible = False
            self.board = Board(self.__screen, self.__font)
            self.logic = Logic(self.board)
            self.mode_selected = False
