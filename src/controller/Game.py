from model.players.Player import Player
import time

class Game:

    """
    Game avec view pour pouvoir intéragir (jouer/regarder)
    """
    def __init__(self, board, player1, player2, view):
        self.board = board
        player1.set_board(board)
        player2.set_board(board)
        self.players = [player1, player2]
        self.view = view
        self.view.set_game(self)

        self.playersTurn = 0
        self.gameOver = 0

    def run(self):
        # On affiche le board
        self.view.print_board()

        # GameOver = 0 : partie en cours
        # GameOver = 1 : partie gagnée par le joueur courant
        # GameOver = 2 : partie terminée, égalité
        while self.gameOver == 0:
            # Ask for IA_Player
            if type(self.get_current_player()) is not Player:
                # L'AI joue un coup
                start = time.time()
                self.gameOver = self.get_current_player().play()
                print("Computing time : ", time.time() - start)
                # On affiche le board modifié
                self.view.print_board()
            else:
                # On demande le coup à jouer et on le joue
                column = self.view.ask_column()
                self.gameOver = self.get_current_player().play(column)
                # On affiche le board modifié
                self.view.print_board()

            # Changement de tour
            self.switch_turn()

        # On rechange de joueur pour avoir le gagnant
        self.switch_turn()
        self.view.print_winner()

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
