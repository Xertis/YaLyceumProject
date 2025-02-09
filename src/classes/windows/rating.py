import pygame
from src.constants import SCREEN_NAME, TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils.loader import LOADER
import json
import os
FONT_PATH = "Jersey10-Regular.ttf"
SCORES_FILE = "scores.json"


def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []

    with open(SCORES_FILE, 'r') as f:
        return json.load(f)


class RATING:
    def __init__(self, scr, start_window):
        self.screen = scr
        self.start_window = start_window

        self.font_jersey50 = LOADER.font.load(FONT_PATH, 50)
        self.font_jersey55 = LOADER.font.load(FONT_PATH, 55)
        self.apple = LOADER.sprite.load("apple.png", (38, 38))


    def draw(self):

        pygame.Surface.fill(self.screen, (220, 123, 84))
        self.screen.blit(self.apple, (310, 90))
        self.screen.blit(self.apple, (410, 415))

        back_rect = pygame.Rect(SCREEN_WIDTH - 455, SCREEN_HEIGHT - 150, 107, 60)
        pygame.draw.rect(self.screen, (240, 143, 104), back_rect)
        left_back_vignette = pygame.Rect(SCREEN_WIDTH - 460, SCREEN_HEIGHT - 150, 5, 65)
        pygame.draw.rect(self.screen, (0, 121, 13), left_back_vignette)
        right_back_vignette = pygame.Rect(SCREEN_WIDTH - 348, SCREEN_HEIGHT - 150, 5, 65)
        pygame.draw.rect(self.screen, (0, 121, 13), right_back_vignette)
        upper_back_vignette = pygame.Rect(SCREEN_WIDTH - 460, SCREEN_HEIGHT - 155, 117, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_back_vignette)
        lower_back_vignette = pygame.Rect(SCREEN_WIDTH - 460, SCREEN_HEIGHT - 90, 117, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_back_vignette)

        rating_rect = pygame.Rect(SCREEN_WIDTH - 505, SCREEN_HEIGHT - 480, 210, 250)
        pygame.draw.rect(self.screen, (240, 143, 104), rating_rect)
        left_rating_vignette = pygame.Rect(SCREEN_WIDTH - 515, SCREEN_HEIGHT - 490, 10, 270)
        pygame.draw.rect(self.screen, (0, 121, 13), left_rating_vignette)
        right_rating_vignette = pygame.Rect(SCREEN_WIDTH - 295, SCREEN_HEIGHT - 490, 10, 270)
        pygame.draw.rect(self.screen, (0, 121, 13), right_rating_vignette)
        line1 = pygame.Rect(SCREEN_WIDTH - 505, SCREEN_HEIGHT - 480, 210, 3)
        pygame.draw.rect(self.screen, (64, 64, 64), line1)
        line2 = pygame.Rect(SCREEN_WIDTH - 505, SCREEN_HEIGHT - 430, 210, 3)
        pygame.draw.rect(self.screen, (64, 64, 64), line2)
        line3 = pygame.Rect(SCREEN_WIDTH - 505, SCREEN_HEIGHT - 380, 210, 3)
        pygame.draw.rect(self.screen, (64, 64, 64), line3)
        line4 = pygame.Rect(SCREEN_WIDTH - 505, SCREEN_HEIGHT - 330, 210, 3)
        pygame.draw.rect(self.screen, (64, 64, 64), line4)
        line5 = pygame.Rect(SCREEN_WIDTH - 505, SCREEN_HEIGHT - 280, 210, 3)
        pygame.draw.rect(self.screen, (64, 64, 64), line5)
        line6 = pygame.Rect(SCREEN_WIDTH - 505, SCREEN_HEIGHT - 230, 210, 3)
        pygame.draw.rect(self.screen, (64, 64, 64), line6)

        back_button = self.font_jersey50.render(TEXTS['back'], True, (64, 64, 64))
        back_rect = back_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.8))
        self.screen.blit(back_button, back_rect)

        # Обработка клика на кнопку "Назад"
        mouse_pos = pygame.mouse.get_pos()
        if back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (240, 143, 104), back_rect)
            back_button2 = self.font_jersey55.render(TEXTS['back'], True, (64, 64, 64))
            self.screen.blit(back_button2,
                             back_button.get_rect(center=(SCREEN_WIDTH // 2.02, SCREEN_HEIGHT * 0.796)))
            if pygame.mouse.get_pressed()[0]:
                self.start_window.is_rating = False

        # Загрузка результатов
        scores = load_scores()

        # Отрисовка заголовка
        title = self.font_jersey50.render(TEXTS["rating"], True, (0, 70, 0))
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(title, title_rect)

        # Отрисовка результатов
        y = 150
        for i, score in enumerate(scores[:10], 1):
            score_text = self.font_jersey50.render(
                f"{i}. {score} apples",
                True,
                (200, 0, 0)
            )
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, y))
            self.screen.blit(score_text, score_rect)
            y += 50
