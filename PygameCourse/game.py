import pygame
import random
import math

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
score = 0

def player(x, y):
    screen.blit(player_img, (x, y))


# Enemy
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []  
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img = pygame.image.load("img/enemy.png")
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Bullet
# Bulltet state ready -> you can't see the bullet
# Bulltet state fire -> you can see the bullet
bullet_img = pygame.image.load("img/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 1
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    return False


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
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Bounderies of the player
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    
    for i in range(num_of_enemies):

        # Bounderies of the enemies
        enemyX[i] += enemyX_change[i] 
        if enemyX[i] < 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -0.3

        # Collision detection
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_state = "ready"
            bulletY = 480
            score += 10
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        
        enemy(enemyX[i], enemyY[i])

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire": 
        fire_bullet(bulletX, bulletY) 
        bulletY -= bulletY_change


    player(playerX, playerY)
    pygame.display.update()
    
pygame.quit()
# Finish pygame