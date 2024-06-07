import pygame
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting

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
    ray_casting(sc,player_pos,player_angle)

    pygame.draw.circle(sc, GREEN, player.pos, 12)
    for x,y in world_map:
        pygame.draw.rect(sc, DARKGREY,(x, y, TILE, TILE),2)

    pygame.display.flip()
    clock.tick(FPS)