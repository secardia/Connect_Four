
class AI_Player:

    def __init__(self, name, board, piece, oracle):
        self.name = name
        self.board = board
        self.piece = piece
        self.oracle = oracle

    def play(self):
        # On récupère la colonne où jouer
        column = self.oracle.get_play()
        # On joue le coup et on retourne la valeur (0, 1 ou 2)
        return self.board.drop_piece_and_check_end(column, self.piece)
