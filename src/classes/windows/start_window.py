import pygame
from src.constants import SCREEN_NAME, TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils.loader import LOADER

MUSIC_PATH = "Fluffing-a-Duck (start window sound).mp3"
FONT_PATH = "Jersey10-Regular.ttf"

class DrawStartWindow:
    def __init__(self, scr):
        self.is_play = False
        self.is_options = False
        self.is_rating = False
        self.is_pause = False
        self.screen = scr
        self.is_tutorial = False
        self.font_jersey100 = LOADER.font.load(FONT_PATH, 100)
        self.font_jersey60 = LOADER.font.load(FONT_PATH, 60)
        self.font_jersey65 = LOADER.font.load(FONT_PATH, 65)

        channel = pygame.mixer.Channel(0)
        music = LOADER.sound.load(MUSIC_PATH)
        channel.play(music, loops=-1)

        self.draw()

    def draw(self):
        pygame.Surface.fill(self.screen, 'black')

        # Заголовок игры
        name_of_game = self.font_jersey100.render(SCREEN_NAME, False, (178, 102, 255))
        name_rect = name_of_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.1))
        self.screen.blit(name_of_game, name_rect)

        # Кнопки меню
        start_button = self.font_jersey60.render(TEXTS['start'], True, (229, 204, 255))
        start_rect = start_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.4))
        self.screen.blit(start_button, start_rect)

        tutorial_button = self.font_jersey60.render('tutorial', True, (229, 204, 255))
        tutorial_rect = tutorial_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.5))
        self.screen.blit(tutorial_button, tutorial_rect)

        rating_button = self.font_jersey60.render(TEXTS['rating'], True, (229, 204, 255))
        rating_rect = rating_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.6))
        self.screen.blit(rating_button, rating_rect)

        options_button = self.font_jersey60.render(TEXTS['options'], True, (229, 204, 255))
        options_rect = options_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7))
        self.screen.blit(options_button, options_rect)

        # Обработка кликов
        mouse_pos = pygame.mouse.get_pos()
        if start_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.is_play = True

        if tutorial_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.is_tutorial = True

        if rating_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.is_rating = True

        if options_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.is_options = True
