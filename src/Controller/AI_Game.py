
class AI_Game:

    """
    Game sans view donc pas d'interface pour intéragir
    """
    def __init__(self, board, player1, player2):
        self.board = board
        player1.set_board(board)
        player2.set_board(board)
        self.players = [player1, player2]

        self.playersTurn = 0
        self.gameOver = 0

    def run(self):
        # GameOver = 0 : partie en cours
        # GameOver = 1 : partie gagnée par le joueur courant
        # GameOver = 2 : partie terminée, égalité
        while self.gameOver == 0:
            # L'AI joue un coup
            self.gameOver = self.get_current_player().play()
            # Changement de tour
            self.switch_turn()
        # On rechange de joueur pour avoir le gagnant
        self.switch_turn()
        if self.gameOver == 1:
            # Partie gagnée
            return self.playersTurn
        else:
            # Egalité
            return 2

    def get_current_player(self):
        return self.players[self.playersTurn]

    def switch_turn(self):
        self.playersTurn = 1 - self.playersTurn
