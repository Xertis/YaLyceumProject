import pygame
import sys
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME, FPS
from src.classes.map.map import MAP

pygame.init()
pygame.display.set_caption(SCREEN_NAME)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
map = MAP(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta_time = clock.tick(FPS) / 1000.0

    speed = map.snake.controller.speed * delta_time
    map.snake.move(speed)
    map.draw()
    pygame.display.flip()
    

pygame.quit()
sys.exit()
