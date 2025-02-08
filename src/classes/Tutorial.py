import pygame

from src.classes.windows.pause_window import FONT_PATH
from src.utils.loader import LOADER
from src.constants import TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT


# Новый класс для обучения
class TUTORIAL:
    def __init__(self, scr, start_window):
        self.screen = scr
        self.start_window = start_window
        self.font_jersey60 = LOADER.font.load(FONT_PATH, 60)  # Заголовок
        self.font_jersey40 = LOADER.font.load(FONT_PATH, 40)  # Основной текст
        self.font_jersey50 = LOADER.font.load(FONT_PATH, 50)  # Кнопка "Назад"

    def draw(self):
        # Очистка экрана
        self.screen.fill('black')

        # Заголовок "Обучение"
        title = self.font_jersey60.render('Tutotial', True, (178, 102, 255))
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.1))
        self.screen.blit(title, title_rect)

        # Инструкции
        controls_text = self.font_jersey40.render('Controls: WASD', True, (229, 204, 255))
        controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.3))
        self.screen.blit(controls_text, controls_rect)

        goal_text = self.font_jersey40.render('Eat apple to grow up', True, (229, 204, 255))
        goal_rect = goal_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.4))
        self.screen.blit(goal_text, goal_rect)

        avoid_text = self.font_jersey40.render('Avoid walls and obstacles', True, (229, 204, 255))
        avoid_rect = avoid_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.5))
        self.screen.blit(avoid_text, avoid_rect)

        # Кнопка "Назад"
        back_button = self.font_jersey50.render('Back', True, (229, 204, 255))
        back_rect = back_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.8))
        self.screen.blit(back_button, back_rect)

        # Обработка клика на кнопку "Назад"
        mouse_pos = pygame.mouse.get_pos()
        if back_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.start_window.is_tutorial = False