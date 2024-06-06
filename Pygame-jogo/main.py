import pygame
from settings import *
from player import Player
pygame.init()


sc = pygame.display.set_mode((WIDTH,HEIGTH))
clock = pygame.time.Clock()

player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.circle(sc, GREEN, player.pos, 12)

    pygame.display.flip()
    clock.tick(FPS)