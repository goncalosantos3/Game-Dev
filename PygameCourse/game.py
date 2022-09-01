import pygame

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

def player():
    screen.blit(player_img, (playerX, playerY))


run_game =  True
# Game loop
while run_game:

    screen.blit(bg_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
    player()
    pygame.display.update()
    

pygame.quit()
# Finish pygame