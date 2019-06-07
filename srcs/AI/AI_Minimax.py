import math
import random


def evaluate_window(window, piece):
	score = 0
	opp_piece = P1_PIECE
	if piece == P1_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4

	return score


def score_position(board, piece):
	score = 0
	# Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_NUMBER//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_NUMBER):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_NUMBER-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(COLUMN_NUMBER):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_NUMBER-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_NUMBER-3):
		for c in range(COLUMN_NUMBER-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(ROW_NUMBER-3):
		for c in range(COLUMN_NUMBER-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score










def pick_best_move(self, piece):
	valid_locations = self.board.validLocations(self.board)
	best_score = -10000
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = self.board.get_next_open_row(col)
		temp_board = self.board.copy()
		self.board.drop_piece_and_check_end(temp_board, row, col, piece)
		score = self.score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col

	return best_col


def minimax_worker(board, depth, alpha, beta, maximizingPlayer):
	valid_locations = board.validLocations()
	is_terminal = board.is_terminal_node()
	if depth == 0 or is_terminal:
		if is_terminal:
			if board.winning_move(P2_PIECE):
				return (None, 100000000000000)
			elif self.winning_move(P1_PIECE):
				return (None, -10000000000000)
			else:  # Game is over, no more valid moves
				return (None, 0)
		else:  # Depth is zero
			return (None, score_position(P2_PIECE))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = self.board.get_next_open_row(col)
			b_copy = self.board.copy()
			b_copy.drop_piece_and_check_end(row, col, P2_PIECE)
			new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else:  # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = self.board.get_next_open_row(self.board, col)
			b_copy = self.board.copy()
			self.board.drop_piece_and_check_end(b_copy, row, col, P1_PIECE)
			new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value


class AI_Minimax:

	def __init__(self, board, depth, alpha, beta, piece):
		self.board = board
		self.depth = depth
		self.alpha = alpha
		self.beta = beta
		self.piece = piece

	def minimax(self):
		minimax_worker(self.board, self.depth, self.alpha, self.beta, self.piece)
