import pygame
import random
import math

# Inicia o jogo
pygame.init()

# janela: 800px de largura e 600px de altura 
screen = pygame.display.set_mode((800,600))

# Título da janela
pygame.display.set_caption("Floppy Disk Game")
# Icon da janela (não funciona em Linux acho)
icon = pygame.image.load('img/floppy-disk.png')
pygame.display.set_icon(icon)

# Background
bgImg = pygame.image.load('img/bg.png')
bgImg = pygame.transform.scale(bgImg, (800,600))

# Pipes
pipeBImg = pygame.image.load('img/pipe_baixo.png')
pipeBImg = pygame.transform.scale(pipeBImg, (100, 500))

pipeCImg = pygame.image.load('img/pipe_cima.png')
pipeCImg = pygame.transform.scale(pipeCImg, (100, 500))

# Lista de posições de 3 conjuntos de pipes
pipesPos = [(800, random.randint(200,500)), (1100, random.randint(200,500)), (1300, random.randint(200,500))]

# Jogador
img = pygame.image.load('img/floppy-disk.png')
playerImg = pygame.transform.scale(img, (50,50))
playerX = 100
playerY = 300

def player(img, x, y):
    # Desenhar a imagem do jogador
    screen.blit(img, (x, y))

def pipes(l):
    for pipe in l:
        x, y = pipe
        screen.blit(pipeBImg, (x, y+50))
        screen.blit(pipeCImg, (x, y-550))

def is_collision(x1, y1, l): 

    for pipe in l:
        x2, y2 = pipe
        
        dist_x = abs(x1 - x2) 

        if dist_x < 50 and (y1 < y2 - 25 or y1 > y2 + 25):
            return True
            
    return False


# Variável de controlo de terminação do jogo
running = True

# Main Loop do jogo
while running:
    # Background
    screen.blit(bgImg, (0,0))
    playerY += 0.3  
    
    for i in enumerate(pipesPos):
        i, (x, y) = i
        x -= 0.8
        if x <= 0:
            x = 800
        pipesPos[i] = (x, y)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Fechar a janela
            running = False   
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY -= 50

    # Jogador saiu da tela
    if playerY >= 600 or playerY <= 0:
        running = False

    collison = is_collision(playerX, playerY, pipesPos)
    if collison:
        running = False

    player(playerImg, playerX, playerY)
    pipes(pipesPos)

    pygame.display.update()

print("Jogo terminado!")
if collison: 
    print("Houve uma colisão com um pipe!")