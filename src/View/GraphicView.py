import math
import sys
import pygame
from Players.Player import *
import src.Constants as Co


class GraphicView:

    def __init__(self):
        self.game = None
        self.screen = pygame.display.set_mode((Co.WIDTH, Co.HEIGHT))
        self.playerColors = [Co.P1_PIECE_COLOR, Co.P2_PIECE_COLOR]
        pygame.init()
        self.font = pygame.font.SysFont("monospace", 75)
        pygame.display.update()

    def set_game(self, game):
        self.game = game

    def ask_column(self):
        retColumn = -1
        # Boucle pour l'interface
        while not self.game.board.is_a_valid_location(retColumn):
            # Boucle sur les évènements
            for event in pygame.event.get():

                # Mouvement de la souris
                if event.type == pygame.MOUSEMOTION:
                    # Efface le pion en haut
                    pygame.draw.rect(self.screen, Co.BACKGROUND_COLOR, (0, 0, Co.WIDTH, Co.SQUARESIZE))
                    # Récupère la colonne
                    posx = event.pos[0]
                    column = int(math.floor(posx / Co.SQUARESIZE))
                    # Récupère la couleur dans laquelle le dessiner
                    color = self.get_current_color()
                    # Dessine le jeton et rafraichi l'interface
                    pygame.draw.circle(self.screen, color, (column * Co.SQUARESIZE + int(Co.SQUARESIZE / 2),
                                                            int(Co.SQUARESIZE / 2)), Co.RADIUS)
                    pygame.display.update()

                # Clique
                elif event.type == pygame.MOUSEBUTTONDOWN and type(self.game.get_current_player()) is Player:
                    # Efface le pion en haut
                    pygame.draw.rect(self.screen, Co.BACKGROUND_COLOR, (0, 0, Co.WIDTH, Co.SQUARESIZE))
                    # Récupère la colonne dans laquelle dessiner le jeton
                    posx = event.pos[0]
                    retColumn = int(math.floor(posx / Co.SQUARESIZE))
                    break

                elif event.type == pygame.QUIT:
                    sys.exit()
        return retColumn

    def print_board(self):
        pygame.draw.rect(self.screen, Co.BOARD_COLOR,
                         (0, Co.SQUARESIZE, Co.SQUARESIZE * Co.COLUMN_NUMBER, Co.SQUARESIZE * Co.ROW_NUMBER))
        for c in range(Co.COLUMN_NUMBER):
            for r in range(Co.ROW_NUMBER):
                piece = self.game.board.matrix[r][c]
                color = Co.BACKGROUND_COLOR
                if piece == Co.P1_PIECE:
                    color = Co.P1_PIECE_COLOR
                elif piece == Co.P2_PIECE:
                    color = Co.P2_PIECE_COLOR
                pygame.draw.circle(self.screen, color, (int(c * Co.SQUARESIZE + Co.SQUARESIZE / 2),
                                    Co.HEIGHT - int(r * Co.SQUARESIZE + Co.SQUARESIZE / 2)), Co.RADIUS)
        # Update l'interface
        pygame.display.update()
        # On clear les events pour refresh
        pygame.event.clear()

    def print_winner(self):
        if self.game.gameOver == 1:
            # Partie gagnée
            label = self.font.render(self.game.get_current_player().name + " wins !", 1, self.get_current_color())
        else:
            # Egalité
            label = self.font.render("No winner !", 1, Co.BOARD_COLOR)
        self.screen.blit(label, (40, 10))
        # Update l'interface
        pygame.display.update()
        # On clear les events pour refresh
        pygame.event.clear()

    def get_current_color(self):
        return self.playerColors[self.game.playersTurn]
