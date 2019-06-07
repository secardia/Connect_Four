
class AI_Determinist:

    def __init__(self, board, piece):
        self.board = board
        self.piece = piece
        self.plays = [0, 0, 0, 1, 1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 6, 6, 6, 3]
        self.playNumber = -1

    def get_play(self):
        # On renvoit le coup à jouer
        self.playNumber += 1
        return self.plays[self.playNumber]
