import pygame
from src.constants import SCREEN_NAME, TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils.loader import LOADER

START_WINDOW_MUSIC_PATH = "Fluffing-a-Duck (start window sound).mp3"
GAME_MUSIC_PATH = 'game_music.mp3'
CLICK_EFFECT_PATH = "click_effect.wav"
FONT_PATH = "Jersey10-Regular.ttf"

class DrawStartWindow:
    def __init__(self, scr):
        self.is_play = False
        self.is_options = False
        self.is_rating = False
        self.is_pause = False
        self.screen = scr
        self.is_tutorial = False
        self.is_game_over = False
        self.font_jersey100 = LOADER.font.load(FONT_PATH, 100)
        self.font_jersey60 = LOADER.font.load(FONT_PATH, 60)
        self.font_jersey65 = LOADER.font.load(FONT_PATH, 65)
        self.apple = LOADER.sprite.load("apple.png", (38, 38))
        self.background = LOADER.sprite.load("menu_background.png", (1374, 1259))
        self.head = LOADER.sprite.load("snake_head_menu.png", (56, 57))
        self.tail = LOADER.sprite.load("snake_tail.png", (56, 56))

        self.start_window_music = pygame.mixer.Channel(0)
        music = LOADER.sound.load(START_WINDOW_MUSIC_PATH)
        self.start_window_music.play(music, loops=-1)
        self.click_effect = LOADER.sound.load(CLICK_EFFECT_PATH)

        self.game_music = pygame.mixer.Channel(0)
        self.music2 = LOADER.sound.load(GAME_MUSIC_PATH)

        self.draw()

    def draw(self):
        self.click_effect.set_volume(pygame.mixer.Channel(1).get_volume())
        self.screen.blit(self.background, (-230, -285))
        self.screen.blit(self.head, (200, 140))
        self.screen.blit(self.tail, (190, 187))
        self.screen.blit(self.tail, (170, 228))
        self.screen.blit(self.tail, (156, 272))
        self.screen.blit(self.tail, (170, 314))
        self.screen.blit(self.tail, (195, 349))
        self.screen.blit(self.tail, (225, 377))
        self.screen.blit(self.tail, (320, 430))
        self.screen.blit(self.tail, (328, 474))
        self.screen.blit(self.tail, (313, 515))

        buttons_rect = pygame.Rect(SCREEN_WIDTH - 540, SCREEN_HEIGHT - 400, 277, 255)
        pygame.draw.rect(self.screen, (240, 143, 104), buttons_rect)

        self.screen.blit(self.apple, (430, 160))
        self.screen.blit(self.apple, (157, 30))
        self.screen.blit(self.apple, (260, 424))

        left_vignette = pygame.Rect(SCREEN_WIDTH - 550, SCREEN_HEIGHT - 410, 10, 275)
        pygame.draw.rect(self.screen, (0, 121, 13), left_vignette)
        right_vignette = pygame.Rect(SCREEN_WIDTH - 263, SCREEN_HEIGHT - 410, 10, 275)
        pygame.draw.rect(self.screen, (0, 121, 13), right_vignette)
        upper_vignette = pygame.Rect(SCREEN_WIDTH - 550, SCREEN_HEIGHT - 410, 297, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_vignette)
        lower_vignette = pygame.Rect(SCREEN_WIDTH - 550, SCREEN_HEIGHT - 145, 297, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_vignette)

        # Заголовок игры
        name_of_game = self.font_jersey100.render(SCREEN_NAME, False, (0, 70, 0))
        name_rect = name_of_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.15))
        self.screen.blit(name_of_game, name_rect)

        # Кнопки меню
        start_button = self.font_jersey60.render(TEXTS['start'], True, (64, 64, 64))
        start_rect = start_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.4))
        self.screen.blit(start_button, start_rect)

        tutorial_button = self.font_jersey60.render(TEXTS["tutorial"], True, (64, 64, 64))
        tutorial_rect = tutorial_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.5))
        self.screen.blit(tutorial_button, tutorial_rect)

        rating_button = self.font_jersey60.render(TEXTS['rating'], True, (64, 64, 64))
        rating_rect = rating_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.6))
        self.screen.blit(rating_button, rating_rect)

        options_button = self.font_jersey60.render(TEXTS['options'], True, (64, 64, 64))
        options_rect = options_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7))
        self.screen.blit(options_button, options_rect)

        # Обработка кликов
        mouse_pos = pygame.mouse.get_pos()

        if start_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (240, 143, 104), start_rect)
            start_button2 = self.font_jersey65.render(TEXTS['start'], True, (128, 128, 128))
            self.screen.blit(start_button2,
                             start_button.get_rect(center=(SCREEN_WIDTH // 2.05, SCREEN_HEIGHT * 0.396)))
            if pygame.mouse.get_pressed()[0]:
                self.click_effect.play(loops=0)
                self.start_window_music.stop()
                self.game_music.play(self.music2, loops=-1)
                self.is_play = True

        if tutorial_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (240, 143, 104), tutorial_rect)
            tutorial_button2 = self.font_jersey65.render(TEXTS["tutorial"], True, (128, 128, 128))
            self.screen.blit(tutorial_button2,
                             tutorial_button.get_rect(center=(SCREEN_WIDTH // 2.03, SCREEN_HEIGHT * 0.496)))
            if pygame.mouse.get_pressed()[0]:
                self.click_effect.play(loops=0)
                self.is_tutorial = True

        if rating_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (240, 143, 104), rating_rect)
            rating_button2 = self.font_jersey65.render(TEXTS['rating'], True, (128, 128, 128))
            self.screen.blit(rating_button2,
                             rating_button.get_rect(center=(SCREEN_WIDTH // 2.02, SCREEN_HEIGHT * 0.595)))
            if pygame.mouse.get_pressed()[0]:
                self.click_effect.play(loops=0)
                self.is_rating = True

        if options_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (240, 143, 104), options_rect)
            options_button2 = self.font_jersey65.render(TEXTS['options'], True, (128, 128, 128))
            self.screen.blit(options_button2,
                             options_button.get_rect(center=(SCREEN_WIDTH // 2.02, SCREEN_HEIGHT * 0.696)))
            if pygame.mouse.get_pressed()[0]:
                self.click_effect.play(loops=0)
                self.is_options = True
