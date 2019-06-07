import src.Constants as Co
import TimeCounter as Tc
import time


def create_matrix():
    return [[Co.EMPTY_PIECE] * Co.COLUMN_NUMBER for _ in range(Co.ROW_NUMBER)]


def create_empty_row():
    return [0] * Co.COLUMN_NUMBER


def create_valid_locations():
    return list(range(Co.COLUMN_NUMBER))


class Board:

    def __init__(self, matrix=None, emptyRow=None, validLocations=None):
        self.matrix = create_matrix() if matrix is None else matrix
        self.emptyRow = create_empty_row() if emptyRow is None else emptyRow
        self.validLocations = create_valid_locations() if validLocations is None else validLocations
        self.validLocationsLength = len(self.validLocations)

    def copy(self):
        return Board([r.copy() for r in self.matrix], self.emptyRow.copy(), self.validLocations.copy())

    # NEED TO CHECK
    def print_matrix(self):
        print(self.matrix)

    # Seulement utilisé par les Views (donc pas par l'IA)
    def is_a_valid_location(self, col):
        return self.emptyRow[col] <= Co.ROW_NUMBER - 1 and 0 <= col <= Co.COLUMN_NUMBER - 1

    def _update_playable_col_after_drop(self, col):
        # Si le pion joué est le dernier de la colonne on le supprime des solutions possibles
        self.emptyRow[col] += 1
        if self.emptyRow[col] == Co.ROW_NUMBER:
            self.validLocations.remove(col)
            self.validLocationsLength -= 1

    def _update_playable_col_after_undo(self, col):
        # Si le pion retiré est le dernier de la colonne on rajoute la colonne aux solutions
        if self.emptyRow[col] == Co.ROW_NUMBER:
            self.validLocations.append(col)
            self.validLocationsLength += 1
        self.emptyRow[col] -= 1

    def drop_piece_and_check_end(self, col, piece):
        # On récupère la ligne où jouer
        row = self.emptyRow[col]
        # On ajoute la pièce
        self.matrix[row][col] = piece
        self._update_playable_col_after_drop(col)

        # Si c'est un coup gagnant on retourne 1
        if self._is_a_winning_play(row, col, piece):
            return 1
        # S'il le board est plein on retourne 2
        elif self.validLocationsLength == 0:
            return 2
        else:
            return 0

    def undo_piece(self, col):
        self._update_playable_col_after_undo(col)
        # On récupère la ligne à retirer
        row = self.emptyRow[col]
        # On retire la pièce
        self.matrix[row][col] = Co.EMPTY_PIECE

    def get_mandatory_play(self, piece):
        """
        Retourne un coup gagnant s'il y en a un, s'il n'y en a pas retourne un coup qui bloque la victoire de
        l'adversaire
        :param piece:
        :return un coup gagnant ou empechant la défaite:
        """
        winning = self._get_winning_play(piece)
        if winning is not None:
            return winning
        else:
            # On retourne un coup empechant la défaite s'il y en a un, None sinon
            return self._get_winning_play(2 - piece + 1)

    def _get_winning_play(self, piece):
        for col in self.validLocations:
            # On récupère le résultat après avoir joué le coup
            res = self.drop_piece_and_check_end(col, piece)
            # On undo le coup
            self.undo_piece(col)
            # Si ce coup est gagnant on le retourne
            if res == 1:
                return col
        return None

    def get_not_losing_play(self, piece):
        validsNotLosing = []
        # On trie les coups qui ne feraient pas gagner l'adversaire
        for col in self.validLocations:
            if not self._is_a_losing_play(col, piece):
                validsNotLosing.append(col)
        return validsNotLosing

    def _is_a_losing_play(self, column, piece):
        # S'il reste plus d'un pion à mettre on regarde si c'est un coup perdant
        if self.emptyRow[column] < Co.ROW_NUMBER - 1:
            # On joue à cet endroit sans check la fin du jeu
            row = self.emptyRow[column]
            self.matrix[row][column] = piece
            self.emptyRow[column] += 1

            # On récupère le résultat après avoir joué le coup pour l'adversaire au même endroit
            res = self.drop_piece_and_check_end(column, 2 - piece + 1)
            # On undo les 2 coups
            self.undo_piece(column)
            self.undo_piece(column)
            # Si le coup est perdant on retourne True
            if res == 1:
                return True
        return False

    def _is_a_winning_play(self, realRow, column, piece):
        # Tc.Iter_is_a_winning_play += 1
        start = time.time()

        # Check vertical locations for win
        row = realRow - 1
        col = column
        botCounter = 1
        while row >= 0 and botCounter < 4 and self.matrix[row][col] == piece:
            row -= 1
            botCounter += 1
        if botCounter < 4:
            row = realRow + 1
            verticalCounter = botCounter
            while row < Co.ROW_NUMBER and verticalCounter < 4 and self.matrix[row][col] == piece:
                row += 1
                verticalCounter += 1
            if verticalCounter > 3:
                Tc.Time_is_a_winning_play += time.time() - start
                return True
        else:
            Tc.Time_is_a_winning_play += time.time() - start
            return True

        # Check horizontal locations for win
        row = realRow
        col = column - 1
        leftCounter = 1
        while col >= 0 and leftCounter < 4 and self.matrix[row][col] == piece:
            col -= 1
            leftCounter += 1
        if leftCounter < 4:
            col = column + 1
            horizontalCounter = leftCounter
            while col < Co.COLUMN_NUMBER and horizontalCounter < 4 and self.matrix[row][col] == piece:
                col += 1
                horizontalCounter += 1
            if horizontalCounter > 3:
                Tc.Time_is_a_winning_play += time.time() - start
                return True
        else:
            Tc.Time_is_a_winning_play += time.time() - start
            return True

        # Check / diags for win
        row = realRow - 1
        col = column - 1
        botLeftCounter = 1
        while col >= 0 and row >= 0 and botLeftCounter < 4 and self.matrix[row][col] == piece:
            col -= 1
            row -= 1
            botLeftCounter += 1
        if botLeftCounter < 4:
            row = realRow + 1
            col = column + 1
            diagOneCounter = botLeftCounter
            while row < Co.ROW_NUMBER and col < Co.COLUMN_NUMBER and diagOneCounter < 4 and self.matrix[row][
                col] == piece:
                col += 1
                row += 1
                diagOneCounter += 1
            if diagOneCounter > 3:
                Tc.Time_is_a_winning_play += time.time() - start
                return True
        else:
            Tc.Time_is_a_winning_play += time.time() - start
            return True

        # Check \ diags for win
        row = realRow - 1
        col = column + 1
        botRightCounter = 1
        while col < Co.COLUMN_NUMBER and row >= 0 and botRightCounter < 4 and self.matrix[row][col] == piece:
            col += 1
            row -= 1
            botRightCounter += 1
        if botRightCounter < 4:
            row = realRow + 1
            col = column - 1
            diagTwoCounter = botRightCounter
            while row < Co.ROW_NUMBER and col >= 0 and diagTwoCounter < 4 and self.matrix[row][col] == piece:
                col -= 1
                row += 1
                diagTwoCounter += 1
            if diagTwoCounter > 3:
                Tc.Time_is_a_winning_play += time.time() - start
                return True
        else:
            Tc.Time_is_a_winning_play += time.time() - start
            return True

        Tc.Time_is_a_winning_play += time.time() - start
        return False

    """
    def winning_move(self, piece):

        # Check horizontal locations for win
        for c in range(Co.COLUMN_NUMBER - 3):
            for r in range(Co.ROW_NUMBER):
                if self.matrix[r][c] == piece and self.matrix[r][c + 1] == piece and self.matrix[r][c + 2] == piece and \
                        self.matrix[r][c + 3] == piece:
                    return [True, 0, c]

        # Check vertical locations for win
        for c in range(Co.COLUMN_NUMBER):
            for r in range(Co.ROW_NUMBER - 3):
                if self.matrix[r][c] == piece and self.matrix[r + 1][c] == piece and self.matrix[r + 2][c] == piece and \
                        self.matrix[r + 3][c] == piece:
                    return [True, 1, c]

        # Check / diaganols
        for c in range(Co.COLUMN_NUMBER - 3):
            for r in range(Co.ROW_NUMBER - 3):
                if self.matrix[r][c] == piece and self.matrix[r + 1][c + 1] == piece and self.matrix[r + 2][c + 2] == \
                        piece and self.matrix[r + 3][c + 3] == piece:
                    return [True, 2, c]

        # Check \ diaganols
        for r in range(Co.ROW_NUMBER - 3):
            for c in range(3, Co.COLUMN_NUMBER):
                if self.matrix[r][c] == piece and self.matrix[r + 1][c - 1] == piece and self.matrix[r + 2][c - 2] == \
                        piece and self.matrix[r + 3][c - 3] == piece:
                    return [True, 3, c]
        return [False, 4]
    """


