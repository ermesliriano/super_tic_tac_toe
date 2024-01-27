class Logic:
    def __init__(self, board):
        self.board = board
        self.current_subgame = None
        self.subgame_winners = [None for _ in range(9)]
        self.player_turn = "X"

    def update_logic(self, row, col):
        self.determine_subgame(row, col)
        self.board.mark_cell(row, col, self.player_turn)
        self.check_subgame_winner()
        self.toggle_player()

    def determine_subgame(self, row, col):
        if self.current_subgame is None or not self.is_subgame_open(self.current_subgame):
            self.current_subgame = (row % 3) * 3 + (col % 3)
        # Aquí puedes agregar la lógica para cambiar el color del sub-juego activo

    def is_subgame_open(self, subgame_index):
        return self.subgame_winners[subgame_index] is None

    def check_subgame_winner(self):
        pass
        # Comprueba si hay un ganador en el sub-juego actual
        # Actualiza self.subgame_winners según corresponda

    def toggle_player(self):
        self.player_turn = "O" if self.player_turn == "X" else "X"