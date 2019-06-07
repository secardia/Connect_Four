from View.GraphicView import *

from AI.AI_Determinist import *
from AI.AI_MonteCarlo import *
from AI.AI_MonteCarlo_Rand_Up import *
from AI.AI_MonteCarlo_Up import *
from AI.AI_MonteCarlo_Up_Heur import *

from AI.AI_Rand_Up import *
from AI.AI_Random import *

from Board import Board
import src.Constants as Co
from Controller.Game import *
from Controller.AI_Game import *
import TimeCounter as Tc


def run():
    # Board
    board = Board()

    # AI
    # P1
    oracle = AI_MonteCarlo_Up(board, Co.P1_PIECE, 100)
    player1 = AI_Player("Player 1", oracle.board, oracle.piece, oracle)

    oracle2 = AI_MonteCarlo_Up(board, Co.P2_PIECE, 1000)
    player2 = AI_Player("Player 2", oracle2.board, oracle2.piece, oracle2)

    # Human
    #player1 = Player("Player 1", board, Co.P1_PIECE)
    #player2 = Player("Player 2", board, Co.P2_PIECE)

    # View
    #view = TextView()
    view = GraphicView()

    # Game / Controller
    game = Game(board, player1, player2, view)
    res = game.run()
    if isinstance(view, GraphicView):
        time.sleep(5)
    print(res)


# Fais jouer gameNumber parties entre oracle1 et oracle2 où oracle1 joue toujours premier
def run_AI_battle_ordered(player1, player2, gameNumber):
    if isinstance(player1, AI_Player) and isinstance(player2, AI_Player):
        p1Win = 0
        p2Win = 0
        draw = 0
        for i in range(gameNumber):
            board = Board()
            player1.set_board(board)
            player2.set_board(board)
            game = AI_Game(board, player1, player2)
            res = game.run()
            if res == 0:
                p1Win += 1
            elif res == 1:
                p2Win += 1
            else:
                draw += 1
        return [p1Win, p2Win, draw]
    else:
        print("Erreur : Les 2 joueurs doivent être des IA")


# Fais jouer gameNumber parties entre oracle1 et oracle2 où les jouers jouent autant de fois en 1er
def run_AI_battle(player1, player2, gameNumber):
    if isinstance(player1, AI_Player) and isinstance(player2, AI_Player):
        p1Win = 0
        p2Win = 0
        draw = 0
        for i in range(int(gameNumber/2)):
            board = Board()
            player1.set_board(board)
            player2.set_board(board)
            game = AI_Game(board, player1, player2)
            res = game.run()
            if res == 0:
                p1Win += 1
            elif res == 1:
                p2Win += 1
            else:
                draw += 1
            print(res)
        for i in range(gameNumber-int(gameNumber/2)):
            board = Board()
            player1.set_board(board)
            player2.set_board(board)
            game = AI_Game(board, player2, player1)
            res = game.run()
            if res == 0:
                p2Win += 1
            elif res == 1:
                p1Win += 1
            else:
                draw += 1
            print(res)
        return [p1Win, p2Win, draw]
    else:
        print("Erreur : Les 2 joueurs doivent être des IA")


if __name__ == '__main__':
    oracle1 = AI_MonteCarlo_Up(None, Co.P1_PIECE, 100)
    oracle2 = AI_MonteCarlo_Up(None, Co.P1_PIECE, 500)
    player1 = AI_Player("Player 1", oracle1.board, oracle1.piece, oracle1)
    player2 = AI_Player("Player 2", oracle2.board, oracle2.piece, oracle2)
    print(run_AI_battle_ordered(player1, player2, 100))

    """
    from multiprocessing import Process

    nbInstances = 5000
    for worker_count in (2, ):
        start = time.time()
        worker_pool = []
        for _ in range(worker_count):
            p = Process(target=run_test_2, args=(int(nbInstances/worker_count),))
            p.start()
            worker_pool.append(p)
        for p in worker_pool:
            p.join()  # Wait for all of the workers to finish.
        end = time.time()
        print("With", worker_count, "process, process time : ", end - start)

"""
    """
    mid = time.time()
    print(run_test_2(4000))

    total = time.time() - start

    print("1st :", mid - start)
    print("2nd :", time.time() - mid)

    print("Time_is_a_winning_play :", Tc.Time_is_a_winning_play / total * 100, "%")
    print("Iter_is_a_winning_play :", Tc.Iter_is_a_winning_play)
    print("Time_is_full :", Tc.Time_is_full / total * 100, "%")

"""