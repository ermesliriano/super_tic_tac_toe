import pygame


class Start_scene:
    
    def __init__(self, font, screen):
        self.__one_player_txt = " 1 player"
        self.__two_player_txt = " 2 players"
        self.__screen = screen
        self.__font = font
        self.is_running = False
        
    def run(self):
        if self.is_running:
            player_one = self.__font.render(self.__one_player_txt, True, (255,255,255))
            player_two = self.__font.render(self.__two_player_txt, True, (255,255,255))
            
            p1_rect = player_one.get_rect(center=(480/2,(480*0.83)))
            p2_rect = player_two.get_rect(center=(480/2,(480*0.93)))
            
            p1_bg_rect = pygame.Rect(120, p1_rect.top - 10, 240, p1_rect.height + 20)
            p2_bg_rect = pygame.Rect(120, p2_rect.top - 10, 240, p2_rect.height + 20)

            pygame.draw.rect(self.__screen, (0,0,0), p1_bg_rect)
            pygame.draw.rect(self.__screen, (0,0,0), p2_bg_rect)

            self.__screen.blit(player_one, p1_bg_rect)
            self.__screen.blit(player_two, p2_bg_rect)

