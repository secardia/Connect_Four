from View.GraphicView import *
from AI.AI_MonteCarlo import *
from AI.AI_MonteCarlo_Up import *
from AI.AI_MonteCarlo_Rand_Up import *

from AI.AI_Random import *
from Board import Board
from AI.AI_Rand_Up import *
import src.Constants as Co
from Controller.Game import *
from Controller.AI_Game import *
import TimeCounter as Tc

import time
import psutil
import multiprocessing as mp


def run():
    # Board
    matrix = [[1, 1, 1, 2, 1, 0, 2], [2, 2, 0, 0, 1, 0, 2], [1, 2, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    emptyrow = [3, 3, 1, 1, 3, 0, 2]
    valids = [0, 1, 2, 3, 4, 5, 6]
    board = Board(matrix, emptyrow, valids)

    # AI
    # P1
    #oracle = AI_MonteCarlo(board, Co.P1_PIECE, 100)
    #player1 = AI_Player("Player 1", oracle.board, oracle.piece, oracle)

    # P2
    #oracle = AI_MonteCarlo(board, Co.P2_PIECE, 1000)
    #player2 = AI_Player("Player 2", oracle.board, oracle.piece, oracle)

    # Human
    player1 = Player("Player 1", board, Co.P1_PIECE)
    player2 = Player("Player 2", board, Co.P2_PIECE)

    # View
    #view = TextView()
    view = GraphicView()

    # Game / Controller
    game = Game(board, player1, player2, view)
    res = game.run()
    print(res)


def run_test(testNumber):
    p1Win = 0
    p2Win = 0
    draw = 0

    for i in range(testNumber):
        board = Board()

        oracle = AI_Random(board, Co.P1_PIECE)
        player1 = AI_Player("Player 1", oracle.board, oracle.piece, oracle)

        oracle = AI_Random(board, Co.P2_PIECE)
        player2 = AI_Player("Player 2", oracle.board, oracle.piece, oracle)

        game = AI_Game(board, player1, player2)
        res = game.run()
        if res == 0:
            p1Win += 1
        elif res == 1:
            p2Win += 1
        else:
            draw += 1
        print(res)

    return [p1Win, p2Win, draw]


def run_test_2(testNumber):
    p1Win = 0
    p2Win = 0
    draw = 0

    for i in range(testNumber):
        board = Board()

        oracle = AI_Rand_Up(board, Co.P1_PIECE)
        player1 = AI_Player("Player 1", oracle.board, oracle.piece, oracle)

        oracle = AI_Rand_Up(board, Co.P2_PIECE)
        player2 = AI_Player("Player 2", oracle.board, oracle.piece, oracle)

        game = AI_Game(board, player1, player2)
        #game = Game(board, player1, player2, GraphicView())

        res = game.run()

        if res == 0:
            p1Win += 1
        elif res == 1:
            p2Win += 1
        else:
            draw += 1
        #print(res)

    return [p1Win, p2Win, draw]


if __name__ == '__main__':
    """
    run()

    """

    start = time.time()
    run_test_2(2000)
    end = time.time()
    total = end - start
    print("Total time : ", total)
    print("Time_is_a_winning_play : ", Tc.Time_is_a_winning_play / total * 100, "%")
    print("Iter_is_a_winning_play : ", Tc.Iter_is_a_winning_play)
    print("Time_is_full : ", Tc.Time_is_full / total * 100, "%")

