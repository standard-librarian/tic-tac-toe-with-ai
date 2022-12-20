import copy
import time


class AI:
    def __init__(self, player=2):
        self.player = player

    def minimax(self, board, maximizing):
        case = board.final_state()
        if case == 1:
            return 1, None
        elif case == 2:
            return -1, None
        elif board.is_full():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_squares()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_squares()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    def eval(self, board):
        _eval, move = self.minimax(board, False)
        self.minimax(board, False)
        print(f'AI has chosen to mark the square in pos {move} with an eval of {_eval}')
        return move

    def make_move(self, game):
        time.sleep(0.3)
        row, col = self.eval(game.board)
        game.make_move(row, col)
