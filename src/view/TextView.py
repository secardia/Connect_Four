import src.Constants as Co


class TextView:

    def __init__(self):
        self.game = None

    def set_game(self, game):
        self.game = game

    def ask_column(self):
        column = -1
        # On demande le coup à jouer
        while not self.game.is_a_valid_location(column):
            column = "No"
            while not column.isdigit():
                # On demande le coup à jouer
                column = input("Column (0-" + str(Co.COLUMN_NUMBER) + ") : ")
            column = int(column)
        return column

    def print_board(self):
        self.game.board.print_matrix()

    def print_winner(self):
        if self.game.gameOver == 1:
            # Partie gagnée
            print(self.game.get_current_player().name + " wins !")
        else:
            # Egalité
            print("No winner !")
