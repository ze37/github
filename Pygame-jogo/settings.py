import math
# configuracoes basicas do nosso game
WIDTH = 1200
HEIGTH = 700


HALTH_WIDTH = WIDTH // 2
HALTH_HEIGTH = HEIGTH // 2

#Configurando o fps do jogo
TILE = 100
FPS = 60

FOV = math.pi / 3
HELTH_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS


#configuracoes dos jogadores
player_pos = (HALTH_WIDTH, HALTH_HEIGTH)
player_angle = 0
player_speed = 2



WHITE = (225,225,225)
BLACK = (0,0,0)
RED = (220,0,0)
GREEN = (0,220,0)
BLUE = (0,0,220)
DARKGREY = (110,110,110)
PURPLE = (120,0,120)