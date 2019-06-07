# Matrix codes
EMPTY_PIECE = 0
P1_PIECE = 1
P2_PIECE = 2

# Parameters
ROW_NUMBER = 6
COLUMN_NUMBER = 7

# Colors
#                    R      G       B
BOARD_COLOR =       (0,     0,      255)
BACKGROUND_COLOR =  (0,     0,      0)
P1_PIECE_COLOR =    (255,   0,      0)
P2_PIECE_COLOR =    (255,   255,    0)


# View
# Size of 1 square (each square contains 1 piece)
SQUARESIZE = 100
# Radius of 1 pieece
RADIUS = int(SQUARESIZE / 2 - 5)
WIDTH = COLUMN_NUMBER * SQUARESIZE
HEIGHT = (ROW_NUMBER + 1) * SQUARESIZE

# Used for search all faisible move
WINDOW_LENGTH = COLUMN_NUMBER-3
