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



    def draw(self):

        pygame.Surface.fill(self.screen, "black")

        back_button = self.font_jersey50.render('Back', True, (229, 204, 255))
        back_rect = back_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.8))
        self.screen.blit(back_button, back_rect)

        # Обработка клика на кнопку "Назад"
        mouse_pos = pygame.mouse.get_pos()
        if back_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.start_window.is_rating = False

        # Загрузка результатов
        scores = load_scores()

        # Отрисовка заголовка
        title = self.font_jersey50.render("raiting", True, (178, 102, 255))
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(title, title_rect)

        # Отрисовка результатов
        y = 150
        for i, score in enumerate(scores[:10], 1):
            score_text = self.font_jersey50.render(
                f"{i}. {score} apples",
                True,
                (229, 204, 255)
            )
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, y))
            self.screen.blit(score_text, score_rect)
            y += 50
