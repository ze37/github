import pygame
from settings import *
from player import Player
pygame.init()
from map import world_map

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
    for x,y in world_map:
        pygame.draw.rect(sc, DARKGREY,(x, y, TILE, TILE),2)

    pygame.display.flip()
    clock.tick(FPS)