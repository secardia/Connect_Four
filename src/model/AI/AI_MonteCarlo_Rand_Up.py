from controller.AI_Game import AI_Game

from model.AI.AI_Rand_Up import AI_Rand_Up
from model.players.AI_Player import AI_Player


def monte_carlo_worker(board, piece, numberOfSimulations):
	adversaryWin = 0
	ourWin = 0
	draw = 0
	# On simule numberOfSimulations games aléatoires
	for i in range(numberOfSimulations):
		# Board
		bCopy = board.copy()

		# P1 : l'adversaire
		oracle = AI_Rand_Up(bCopy, 2 - piece + 1)
		player1 = AI_Player("Player 1", oracle.board, oracle.piece, oracle)

		# P2 : nous
		oracle = AI_Rand_Up(bCopy, piece)
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


class AI_MonteCarlo_Rand_Up:

	def __init__(self, board, piece, numberOfSimulations):
		self.board = board
		self.piece = piece
		self.numberOfSimulations = numberOfSimulations

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
				# S'il existe des coups non perdant on cherche le meilleur
				if len(validsNotLosing) > 0:

					bestCol = validsNotLosing.pop()
					# On copie le board
					bCopy = self.board.copy()
					# On joue dans la colonne sans check la victoire
					bCopy.drop_piece(bestCol, self.piece)
					# On calcul son score
					bestScore = monte_carlo_worker(bCopy, self.piece, self.numberOfSimulations)
					for col in validsNotLosing:
						# On copie le board
						bCopy = self.board.copy()
						# On joue dans la colonne sans check la victoire
						bCopy.drop_piece(col, self.piece)
						# On calcul son score
						res = monte_carlo_worker(bCopy, self.piece, self.numberOfSimulations)
						# S'il est meilleur on prend col comme nouvelle meilleure colonne
						bestScore = max(bestScore, res)
						if bestScore == res:
							bestCol = col
					return bestCol

				else:
					# Sinon on renvoit un play perdant
					return self.board.validLocations[0]
