import pygame
from constants import WIDTH, HEIGHT, BG_COLOR

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def setup():
    pygame.init()
    pygame.display.set_caption('XO game for the Clowns')
    screen.fill(BG_COLOR)