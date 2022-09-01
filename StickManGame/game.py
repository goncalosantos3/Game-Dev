import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Stick Man Game')

bg_img = pygame.image.load('img/background2.png')

run_game = True

while run_game:

    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get(): #Closes the game
        if event.type == pygame.QUIT:
            run_game = False

    pygame.display.update()


pygame.quit()