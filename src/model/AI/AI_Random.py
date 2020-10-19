import random as rand


class AI_Random:

    def __init__(self, board, piece):
        self.board = board
        self.piece = piece

    def get_play(self):
        # On renvoit un play aléatoire
        valid = self.board.validLocations
        return rand.choice(valid)
