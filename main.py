import pygame
import sys
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME, FPS
from src.classes.map.map import MAP
from src.classes.windows.start_window import DrawStartWindow

pygame.init()
pygame.display.set_caption(SCREEN_NAME)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
map = MAP(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
start_window = DrawStartWindow(screen, map)
clock = pygame.time.Clock()

map.generate()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta_time = clock.tick(FPS) / 1000.0
    speed = map.snake.controller.speed * delta_time
    map.snake.move(speed)

    if start_window.is_play:
        map.draw()
    else:
        start_window.draw()
    pygame.display.flip()
    

pygame.quit()
sys.exit()
