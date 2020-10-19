import random as rand


class AI_Rand_Up:

    def __init__(self, board, piece):
        self.board = board
        self.piece = piece

    def get_play(self):
        # S'il ne reste qu'une colonne dans laquelle jouer on joue dedans
        if self.board.validLocationsLength == 1:
            return self.board.validLocations[0]
        else:
            # S'il y a un coup obligatoire (gagnant ou empechant la défaite) on le joue
            mandatory = self.board.get_mandatory_play(self.piece)
            if mandatory is not None:
                return mandatory
            else:
                validsNotLosing = self.board.get_not_losing_play(self.piece)
                # S'il existe des plays non perdant on en retourne un aléatoire
                if len(validsNotLosing) > 0:
                    return rand.choice(validsNotLosing)
                else:
                    # Sinon on renvoit un play perdant
                    return self.board.validLocations[0]
