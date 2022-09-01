import pygame
import random

# Initialize pygame
pygame.init()

# 800 px of width and 600 px of height
screen = pygame.display.set_mode((800,600))

# Title, icon and background
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/space-ship.png")
pygame.display.set_icon(icon)
bg_img = pygame.image.load("img/background.png")


# Player
player_img = pygame.image.load("img/space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))


# Enemy
enemy_img = pygame.image.load("img/enemy.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0
enemyY_change = 0

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

run_game =  True
# Game loop
while run_game:

    screen.blit(bg_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
        # If keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  
                playerX_change -= 0.2
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.2
            if event.key == pygame.K_UP:  
                playerY_change -= 0.2
            if event.key == pygame.K_DOWN:
                playerY_change += 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736
    if playerY > 536:
        playerY = 536
    if playerY < 0:
        playerY = 0

    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
    
pygame.quit()
# Finish pygame