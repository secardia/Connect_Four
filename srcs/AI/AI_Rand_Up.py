import random as rand


class AI_Rand_Up:

    def __init__(self, board, piece):
        self.board = board
        self.piece = piece

    def get_play(self):
        valid = self.board.validLocations
        # S'il ne reste qu'un coup à jouer on le joue
        if len(valid) == 1:
            return valid[-1]
        else:
            # S'il y a un coup obligatoire (gagnant ou empechant la défaite) on le joue
            mandatory = self.board.get_mandatory_play(self.piece)
            if mandatory is not None:
                return mandatory
            else:
                validsNotLosing = self.board.get_not_losing_play(self.piece)
                # S'il existe un play non perdant on le retourne
                if len(validsNotLosing) > 0:
                    return rand.choice(validsNotLosing)
                else:
                    # Sinon on renvoit un play aléatoire mais perdant
                    return rand.choice(valid)
