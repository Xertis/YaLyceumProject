import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TEXTS
from src.utils.loader import LOADER

FONT_PATH = "Jersey10-Regular.ttf"
CLICK_EFFECT_PATH = "click_effect.wav"
GAME_MUSIC_PATH = 'game_music.mp3'
START_WINDOW_MUSIC_PATH = "Fluffing-a-Duck (start window sound).mp3"

class GAME_OVER:
    def __init__(self, scr, st_win, m_win):
        self.screen = scr
        self.start_window = st_win
        self.map_window = m_win
        self.font_jersey35 = LOADER.font.load(FONT_PATH, 35)
        self.font_jersey30 = LOADER.font.load(FONT_PATH, 30)
        self.font_jersey55 = LOADER.font.load(FONT_PATH, 55)
        self.font_jersey80 = LOADER.font.load(FONT_PATH, 80)
        self.apple = LOADER.sprite.load("apple.png", (38, 38))
        self.click_effect = LOADER.sound.load(CLICK_EFFECT_PATH)
        self.apple = LOADER.sprite.load("apple.png", (38, 38))

        self.start_window_music = pygame.mixer.Channel(0)
        self.music = LOADER.sound.load(START_WINDOW_MUSIC_PATH)
        self.game_music = pygame.mixer.Channel(0)
        self.music2 = LOADER.sound.load(GAME_MUSIC_PATH)

    def draw(self):
        self.game_music.stop()
        self.click_effect.set_volume(pygame.mixer.Channel(1).get_volume())

        game_over_rect = pygame.Rect(SCREEN_WIDTH - 650, SCREEN_HEIGHT - 500, 500, 350)
        pygame.draw.rect(self.screen, (240, 143, 104), game_over_rect)

        self.screen.blit(self.apple, (250, 414))
        self.screen.blit(self.apple, (478, 126))

        left_vignette = pygame.Rect(game_over_rect.width - 350, game_over_rect.height - 255, 18, 370)
        pygame.draw.rect(self.screen, (0, 121, 13), left_vignette)

        right_vignette = pygame.Rect(game_over_rect.width + 135, game_over_rect.height - 255, 18, 370)
        pygame.draw.rect(self.screen, (0, 121, 13), right_vignette)

        upper_vignette = pygame.Rect(game_over_rect.width - 350, game_over_rect.height - 255, 500, 18)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_vignette)

        lower_vignette = pygame.Rect(game_over_rect.width - 350, game_over_rect.height + 100, 500, 18)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_vignette)

        game_over_text = self.font_jersey80.render(TEXTS["game over"], True, (0, 70, 0))
        game_over_text_width = game_over_text.get_width()
        game_over_text_x = (game_over_rect.width - game_over_text_width) / 0.81
        game_over_text_y = game_over_rect.height * 0.4

        score_text = self.font_jersey55.render(f"{TEXTS['score']}: {self.map_window.snake.score}", True, (200, 0, 0))
        score_text_width = score_text.get_width()
        score_text_x = (game_over_rect.width - score_text_width) / 1.05
        score_text_y = game_over_rect.height * 0.7

        back_button = self.font_jersey30.render(TEXTS['back to menu'], True, (64, 64, 64))
        back_button_width = back_button.get_width()
        back_button_x = (game_over_rect.width - back_button_width) / 0.8
        back_button_y = game_over_rect.height * 1.1

        self.screen.blit(game_over_text, (game_over_text_x, game_over_text_y))
        self.screen.blit(back_button, (back_button_x, back_button_y))
        self.screen.blit(score_text, (score_text_x, score_text_y))

        back_button_rect = pygame.Rect(back_button_x, back_button_y, back_button_width + 5, 25)

        pos = pygame.mouse.get_pos()
        if back_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), back_button_rect)
            back_button2 = self.font_jersey35.render(TEXTS['back to menu'], True, (128, 128, 128))
            self.screen.blit(back_button2, (back_button_x - 8, back_button_y - 3))
            if pygame.mouse.get_pressed()[0]:
                self.click_effect.play(loops=0)
                self.start_window_music.play(self.music, loops=-1)
                self.start_window.is_game_over = False
                self.map_window.snake.score = 0