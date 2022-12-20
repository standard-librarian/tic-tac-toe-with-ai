import numpy as np

from constants import *


class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs_count = 0

    def final_state(self):
        """
        @returns 0 if no wins yet
        @returns 1 if player 1 won
        @returns 2 if player 2 won
        """
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]
        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        # asc diagonal
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1]
        # no win yet
        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs_count += 1

    def is_sqr_empty(self, row, col):
        return self.squares[row][col] == 0

    def is_full(self):
        return self.marked_sqrs_count == 9

    def is_empty(self):
        return self.marked_sqrs_count == 0

    def get_empty_squares(self):
        return [(row, col) for row in range(ROWS) for col in range(COLS)
                if self.is_sqr_empty(row, col)]
