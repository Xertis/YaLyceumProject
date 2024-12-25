import pygame
import sys
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME
from src.classes.map import MAP

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
map = MAP(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
pygame.display.set_caption(SCREEN_NAME)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    map.snake.move()
    map.draw()
    pygame.display.flip()

pygame.quit()
sys.exit()
