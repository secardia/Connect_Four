import random as rand
from Controller.AI_Game import AI_Game

from AI.AI_Random import AI_Random
from Players.AI_Player import AI_Player


def monte_carlo_worker(board, piece, numberOfSimulations):
	adversaryWin = 0
	ourWin = 0
	draw = 0
	# On simule numberOfSimulations games aléatoires
	for i in range(numberOfSimulations):
		# Board
		bCopy = board.copy()

		# P1 : l'adversaire
		oracle = AI_Random(bCopy, 2 - piece + 1)
		player1 = AI_Player("Player 1", oracle.board, oracle.piece, oracle)

		# P2 : nous
		oracle = AI_Random(bCopy, piece)
		player2 = AI_Player("Player 2", oracle.board, oracle.piece, oracle)

		game = AI_Game(bCopy, player1, player2)
		res = game.run()
		if res == 0:
			adversaryWin += 1
		elif res == 1:
			ourWin += 1
		else:
			draw += 1
	# On retourne les stats avec une heuristique
	return 3*ourWin+1*draw


class AI_MonteCarlo_True:

	def __init__(self, board, piece, numberOfSimulations):
		self.board = board
		self.piece = piece
		self.numberOfSimulations = numberOfSimulations

	def get_play(self):
		valids = self.board.validLocations.copy()
		if len(valids) == 1:
			return valids.pop()
		else:
			bestCol = valids.pop()
			# On copie le board
			bCopy = self.board.copy()
			# On joue dans la colonne
			if bCopy.drop_piece_and_check_end(bestCol, self.piece) == 1:
				# Si c'est un coup gagnant on le renvoie
				return bestCol
			else:
				# Sinon on calcul son score
				bestScore = monte_carlo_worker(bCopy, self.piece, self.numberOfSimulations)
				# Puis on teste toutes les colonnes
				for col in valids:
					# On copie le board
					bCopy = self.board.copy()
					# On joue dans la colonne
					if bCopy.drop_piece_and_check_end(col, self.piece) == 1:
						# Si c'est un coup gagnant on le renvoie
						return col
					else:
						# Sinon on calcul son score
						res = monte_carlo_worker(bCopy, self.piece, self.numberOfSimulations)
						# S'il est meilleur on prend col comme nouvelle meilleure colonne
						bestScore = max(bestScore, res)
						if bestScore == res:
							bestCol = col

		return bestCol
