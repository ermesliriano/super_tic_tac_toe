import pygame

class Board:
    def __init__(self, screen, font, size=480):
        self.screen = screen
        self.font = font
        self.size = size
        self.cell_size = size // 9
        self.grid = [["" for _ in range(9)] for _ in range(9)]
        self.current_player = "X"
        self.is_running = True
        self.game_started = False

    def draw(self):
        # Dibujar las líneas del tablero
        for x in range(0, self.size, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.size))
        for y in range(0, self.size, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (self.size, y))

        # Dibujar las "X" y "O" en el tablero
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] != "":
                    text = self.font.render(self.grid[row][col], True, (0, 0, 0))
                    text_rect = text.get_rect(center=(col * self.cell_size + self.cell_size // 2, 
                                                       row * self.cell_size + self.cell_size // 2))
                    self.screen.blit(text, text_rect)

    def handle_click(self, x, y):
        if self.game_started:
            col = x // self.cell_size
            row = y // self.cell_size

            # Verificar que la celda esté vacía antes de asignar
            if self.grid[row][col] == "":
                self.grid[row][col] = self.current_player
                self.current_player = "O" if self.current_player == "X" else "X"
        self.game_started = True
