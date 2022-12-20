from constants import *


class Human:
    def __init__(self, player=1):
        self.player = player

    def make_move(self, event, game):
        col, row = map(lambda x: int(x // SQ_SIZE), event.pos)
        game.make_move(row, col) if game.board.is_sqr_empty(row, col) and game.running else 1

