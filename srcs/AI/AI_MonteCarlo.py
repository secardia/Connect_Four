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


class AI_MonteCarlo:

	def __init__(self, board, piece, numberOfSimulations):
		self.board = board
		self.piece = piece
		self.numberOfSimulations = numberOfSimulations

	def get_play(self):
		valids = self.board.validLocations
		# S'il ne reste qu'un coup à jouer on le joue
		if len(valids) == 1:
			return valids.pop()
		else:
			play = self.board._get_winning_play(self.piece)
			# S'il existe un play gagnant on le retourne
			if play is not None:
				return play
			else:
				# Sinon on cherche un play gagnant pour l'adversaire
				counterPlay = self.board._get_winning_play(2 - self.piece + 1)
				# S'il existe un play gagnant pour l'adversaire on le retourne
				if counterPlay is not None:
					return counterPlay
				else:
					validNotLosing = []
					# Sinon on trie les coups qui ne feraient pas gagner l'adversaire
					for col in valids:
						if not self.board._is_a_losing_play(col, self.piece):
							validNotLosing.append(col)
					# S'il existe un play non perdant on cherche le meilleur
					if len(validNotLosing) > 0:

						bestCol = validNotLosing.pop()
						# On copie le board
						bCopy = self.board.copy()
						# On joue dans la colonne
						bCopy.drop_piece_and_check_end(bestCol, self.piece)
						# On calcul son score
						bestScore = monte_carlo_worker(bCopy, self.piece, self.numberOfSimulations)

						for col in validNotLosing:
							# On copie le board
							bCopy = self.board.copy()
							# On joue dans la colonne
							bCopy.drop_piece_and_check_end(col, self.piece)
							res = monte_carlo_worker(bCopy, self.piece, self.numberOfSimulations)
							if max(bestScore, res) == res:
								bestScore = res
								bestCol = col

						return bestCol

					else:
						# Sinon on renvoit un play perdant aléatoire
						return rand.choice(valids)

