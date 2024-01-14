import pygame
from super_tic_tac_toe.config import cfg_item
from super_tic_tac_toe.assets.images.game_intro import Game_intro_image


class Game:
    def __init__(self):
        pass

    def run(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(cfg_item("game", "screen_size"), 0, 32)
        pygame.display.set_caption(cfg_item("game","title"))
        self.game_intro = Game_intro_image(cfg_item("entities","intro_file"))
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with black
            self.__screen.fill((68, 159, 223))
            self.__screen.blit(self.game_intro.image, (35,0))
            # Render hero image in mouse position
            # x, y = pygame.mouse.get_pos()

            # Flip the display
            pygame.display.update()

        # Done! Time to quit
        pygame.quit()