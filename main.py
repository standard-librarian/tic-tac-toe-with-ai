import pygame
from game import Game
from util import do_nothing, close_screen
from setup import setup

setup()


def main():
    game = Game()
    human, ai = game.human, game.ai
    while True:
        for event in pygame.event.get():
            close_screen() if event.type == pygame.QUIT else do_nothing()
            human.make_move(event, game) if event.type == pygame.MOUSEBUTTONDOWN else do_nothing()
            pygame.display.update()
            ai.make_move(game) if game.player == ai.player and game.running else do_nothing()

        pygame.display.update()


if __name__ == '__main__':
    main()

