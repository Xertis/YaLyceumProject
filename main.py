import pygame
import sys
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME, FPS
from src.classes.map.map import MAP
from src.classes.windows.start_window import DrawStartWindow
from src.classes.windows.options import OPTIONS
from src.classes.windows.rating import RATING
from src.classes.windows.pause_window import PAUSE
from src.classes.windows.tutorial import TUTORIAL
from src.utils.loader import LOADER
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
CLICK_EFFECT_PATH = "click_effect.wav"
click_effect = LOADER.sound.load(CLICK_EFFECT_PATH)


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
    global running
    delta_time = clock.tick(FPS) / 1000.0
    speed = map_window.snake.controller.speed * delta_time

    map_window.snake.move(speed)
    map_window.draw()
    if map_window.snake.check_death():
        running = False


def is_options():
    options_window.draw()


def is_rating():
    rating_window.draw()


def is_pause():
    pause_window.draw()


def is_tutorial():
    tutorial_window.draw()


while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(map_window.snake.score)  # Сохраняем результат при выходе
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and options_window.increase_music_button_rect.collidepoint(pos):
            if not options_window.music >= 0.99:
                options_window.music += 0.1
                click_effect.play(loops=0)
                pygame.mixer.Channel(0).set_volume(options_window.music)
        if event.type == pygame.MOUSEBUTTONDOWN and options_window.reduce_music_button_rect.collidepoint(pos):
            if not options_window.music < 0.05:
                options_window.music -= 0.1
                click_effect.play(loops=0)
                pygame.mixer.Channel(0).set_volume(options_window.music)
        if event.type == pygame.MOUSEBUTTONDOWN and options_window.increase_effects_button_rect.collidepoint(pos):
            if not options_window.effect >= 0.99:
                options_window.effect += 0.1
                click_effect.play(loops=0)
                pygame.mixer.Channel(1).set_volume(options_window.effect)
                click_effect.set_volume(pygame.mixer.Channel(1).get_volume())
        if event.type == pygame.MOUSEBUTTONDOWN and options_window.reduce_effects_button_rect.collidepoint(pos):
            if not options_window.effect < 0.05:
                options_window.effect -= 0.1
                click_effect.play(loops=0)
                pygame.mixer.Channel(1).set_volume(options_window.effect)
                click_effect.set_volume(pygame.mixer.Channel(1).get_volume())


    if start_window.is_play:
        is_play()
    elif start_window.is_options:
        is_options()
    elif start_window.is_rating:
        is_rating()
    elif start_window.is_tutorial:
        is_tutorial()
    elif start_window.is_pause:
        is_pause()
    else:
        start_window.draw()
    pygame.display.flip()
    

pygame.quit()
sys.exit()
