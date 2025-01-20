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

START_WINDOW_MUSIC_PATH = 'res/Sounds/Fluffing-a-Duck (start window sound).mp3'
start_window_channel = pygame.mixer.Channel(0)
start_window_channel.play(pygame.mixer.Sound(START_WINDOW_MUSIC_PATH), loops=-1, fade_ms=10)

map.generate()

running = True

def is_play():
    delta_time = clock.tick(FPS) / 1000.0
    speed = map.snake.controller.speed * delta_time
    start_window_channel.stop()

    map.snake.move(speed)
    map.draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if start_window.is_play:
        is_play()
    else:
        start_window.draw()
    pygame.display.flip()
    

pygame.quit()
sys.exit()
