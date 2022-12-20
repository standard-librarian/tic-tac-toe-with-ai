import pygame
from human import Human
from board import Board
from ai import AI
from constants import *
from setup import screen


class Game:
    def __init__(self):
        self.human = Human()
        self.board = Board()
        self.ai = AI()
        self.running = True
        self.player = 1
        self.show_lines()

    def next_turn(self):
        self.player = self.player % 2 + 1

    def show_lines(self):
        # vertical
        pygame.draw.line(screen, LINE_COLOR, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (2 * SQ_SIZE, 0), (2 * SQ_SIZE, HEIGHT), LINE_WIDTH)
        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQ_SIZE), (WIDTH, SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQ_SIZE), (WIDTH, 2 * SQ_SIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            # X
            start_desc = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + OFFSET)
            end_desc = ((col + 1) * SQ_SIZE - OFFSET, (row + 1) * SQ_SIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            start_asc = (col * SQ_SIZE + OFFSET, (row + 1) * SQ_SIZE - OFFSET)
            end_asc = ((col + 1) * SQ_SIZE - OFFSET, row * SQ_SIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            # O
            center = (SQ_SIZE * (col + 0.5), SQ_SIZE * (row + 0.5))
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()
