

class Player:

    def __init__(self, name, board, piece):
        self.name = name
        self.set_board(board)
        self.piece = piece

    def play(self, column):
        # Si le coup est possible
        if self.board.is_a_valid_location(column):
            # On joue le coup et on retourne la valeur (0, 1 ou 2)
            return self.board.drop_piece_and_check_end(column, self.piece)

    def set_board(self, board):
        self.board = board
