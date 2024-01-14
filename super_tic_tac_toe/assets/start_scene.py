import pygame


class Start_scene:
    
    def __init__(self, font, screen):
        self.__one_player_txt = "1 player"
        self.__two_player_txt = "2 players"
        self.__screen = screen
        self.__font = font
        self.is_running = False
        
    def run(self):
        if self.is_running:
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

    def handle_mouse_click(self, x, y):
        p1_rect = self.__font.render(self.__one_player_txt, True, (255, 255, 255)).get_rect(center=(480 / 2, (480 * 0.83)))
        p2_rect = self.__font.render(self.__two_player_txt, True, (255, 255, 255)).get_rect(center=(480 / 2, (480 * 0.93)))

        if p1_rect.collidepoint((x, y)):
            self.one_player_mode()
        elif p2_rect.collidepoint((x, y)):
            self.two_player_mode()

    def one_player_mode(self):
        # Lógica para el modo de 1 jugador
        print("Modo de 1 jugador seleccionado.")

    def two_player_mode(self):
        # Lógica para el modo de 2 jugadores
        print("Modo de 2 jugadores seleccionado.")
