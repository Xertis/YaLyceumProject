import pygame
import sys
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME, FPS
from src.classes.map.map import MAP
from src.classes.windows.start_window import DrawStartWindow
from src.classes.windows.options import OPTIONS
from src.classes.windows.rating import RATING
from src.classes.windows.pause_window import PAUSE
from src.classes.Tutorial import TUTORIAL
import json
import os
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pygame.init()
pygame.display.set_caption(SCREEN_NAME)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start_window = DrawStartWindow(screen)
options_window = OPTIONS(screen, start_window)
map_window = MAP(SCREEN_WIDTH, SCREEN_HEIGHT, screen, start_window)
rating_window = RATING(screen, start_window)
pause_window = PAUSE(screen, start_window)
clock = pygame.time.Clock()


SCORES_FILE = "scores.json"


def save_score(score):
    if not os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'w') as file:
            json.dump([], file)

    with open(SCORES_FILE, 'r+') as file:
        scores = json.load(file)
        scores.append(score)
        scores = sorted(scores, reverse=True)[:5]  # Топ-5 результатов
        file.seek(0)
        json.dump(scores, file)
        file.truncate()



map_window.generate()

tutorial_window = TUTORIAL(screen, start_window)

running = True

def is_play():
    delta_time = clock.tick(FPS) / 1000.0
    speed = map_window.snake.controller.speed * delta_time

    map_window.snake.move(speed)
    map_window.draw()


def is_options():
    options_window.draw()


def is_rating():
    rating_window.draw()

def is_pause():
    pause_window.draw()

while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(map_window.snake.score)  # Сохраняем результат при выходе
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and options_window.increase_volume_button_rect.collidepoint(pos):
            if not options_window.volume >= 0.99:
                options_window.volume += 0.1
            pygame.mixer.Channel(0).set_volume(options_window.volume)
        if event.type == pygame.MOUSEBUTTONDOWN and options_window.reduce_volume_button_rect.collidepoint(pos):
            if not options_window.volume < 0.05:
                options_window.volume -= 0.1
                pygame.mixer.Channel(0).set_volume(options_window.volume)


    if start_window.is_play:
        is_play()
    elif start_window.is_options:
        is_options()
    elif start_window.is_rating:
        is_rating()
    elif start_window.is_pause:
        is_pause()
    elif start_window.is_tutorial:
            tutorial_window.draw()
    else:
        start_window.draw()
    pygame.display.flip()
    

pygame.quit()
sys.exit()
