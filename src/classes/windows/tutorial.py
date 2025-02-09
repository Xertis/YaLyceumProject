import pygame

from src.classes.windows.pause_window import FONT_PATH
from src.utils.loader import LOADER
from src.constants import TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT

CLICK_EFFECT_PATH = "click_effect.wav"

# Новый класс для обучения
class TUTORIAL:
    def __init__(self, scr, start_window):
        self.screen = scr
        self.start_window = start_window
        self.font_jersey60 = LOADER.font.load(FONT_PATH, 60)  # Заголовок
        self.font_jersey40 = LOADER.font.load(FONT_PATH, 40)  # Основной текст
        self.font_jersey50 = LOADER.font.load(FONT_PATH, 50)  # Кнопка "Назад"
        self.font_jersey55 = LOADER.font.load(FONT_PATH, 55)  # Кнопка назад при увеличении
        self.apple = LOADER.sprite.load("apple.png", (38, 38))
        self.background = LOADER.sprite.load("menu_background.png", (1374, 1259))
        self.click_effect = LOADER.sound.load(CLICK_EFFECT_PATH)

    def draw(self):
        self.click_effect.set_volume(pygame.mixer.Channel(1).get_volume())
        # Очистка экрана
        self.screen.blit(self.background, (-230, -285))

        # Заголовок "Обучение"
        title = self.font_jersey60.render(TEXTS["tutorial"], True, (0, 70, 0))
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.1))
        self.screen.blit(title, title_rect)

        self.screen.blit(self.apple, (200, 84))
        self.screen.blit(self.apple, (700, 145))
        self.screen.blit(self.apple, (60, 204))
        self.screen.blit(self.apple, (450, 296))
        self.screen.blit(self.apple, (355, 414))


        # Инструкции
        controls_text = self.font_jersey40.render('1. Controls: WASD', True, (200, 0, 0))
        controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2.9, SCREEN_HEIGHT * 0.25))
        pygame.draw.rect(self.screen, (240, 143, 104), controls_rect)
        self.screen.blit(controls_text, controls_rect)
        line1_controls = pygame.Rect(SCREEN_WIDTH - 648, SCREEN_HEIGHT - 485, 247, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line1_controls)
        line2_controls = pygame.Rect(SCREEN_WIDTH - 648, SCREEN_HEIGHT - 432, 247, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line2_controls)
        line3_controls = pygame.Rect(SCREEN_WIDTH - 644, SCREEN_HEIGHT - 475, 3, 43)
        pygame.draw.rect(self.screen, (64, 64, 64), line3_controls)
        line4_controls = pygame.Rect(SCREEN_WIDTH - 408, SCREEN_HEIGHT - 475, 3, 43)
        pygame.draw.rect(self.screen, (64, 64, 64), line4_controls)

        goal_text = self.font_jersey40.render('2. Eat apple to grow up', True, (200, 0, 0))
        goal_rect = goal_text.get_rect(center=(SCREEN_WIDTH // 1.3, SCREEN_HEIGHT * 0.35))
        pygame.draw.rect(self.screen, (240, 143, 104), goal_rect)
        self.screen.blit(goal_text, goal_rect)
        line1_goal = pygame.Rect(SCREEN_WIDTH - 355, SCREEN_HEIGHT - 424, 340, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line1_goal)
        line2_goal = pygame.Rect(SCREEN_WIDTH - 355, SCREEN_HEIGHT - 371, 340, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line2_goal)
        line3_goal = pygame.Rect(SCREEN_WIDTH - 351, SCREEN_HEIGHT - 414, 3, 44)
        pygame.draw.rect(self.screen, (64, 64, 64), line3_goal)
        line4_goal = pygame.Rect(SCREEN_WIDTH - 22, SCREEN_HEIGHT - 414, 3, 44)
        pygame.draw.rect(self.screen, (64, 64, 64), line4_goal)

        avoid_text = self.font_jersey40.render('3. Avoid walls and obstacles', True, (200, 0, 0))
        avoid_rect = avoid_text.get_rect(center=(SCREEN_WIDTH // 3.4, SCREEN_HEIGHT * 0.45))
        pygame.draw.rect(self.screen, (240, 143, 104), avoid_rect)
        self.screen.blit(avoid_text, avoid_rect)
        line1_avoid = pygame.Rect(SCREEN_WIDTH - 765, SCREEN_HEIGHT - 365, 400, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line1_avoid)
        line2_avoid = pygame.Rect(SCREEN_WIDTH - 765, SCREEN_HEIGHT - 312, 400, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line2_avoid)
        line3_avoid = pygame.Rect(SCREEN_WIDTH - 761, SCREEN_HEIGHT - 355, 3, 44)
        pygame.draw.rect(self.screen, (64, 64, 64), line3_avoid)
        line4_avoid = pygame.Rect(SCREEN_WIDTH - 373, SCREEN_HEIGHT - 355, 3, 44)
        pygame.draw.rect(self.screen, (64, 64, 64), line4_avoid)

        important_text = self.font_jersey40.render('4. HAVE A GOOD GAME!', True, (200, 0, 0))
        important_rect = important_text.get_rect(center=(SCREEN_WIDTH // 1.9, SCREEN_HEIGHT * 0.6))
        pygame.draw.rect(self.screen, (240, 143, 104), important_rect)
        self.screen.blit(important_text, important_rect)
        line1_important = pygame.Rect(SCREEN_WIDTH - 530, SCREEN_HEIGHT - 273, 302, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line1_important)
        line2_important = pygame.Rect(SCREEN_WIDTH - 530, SCREEN_HEIGHT - 220, 302, 10)
        pygame.draw.rect(self.screen, (0, 121, 13), line2_important)
        line3_important = pygame.Rect(SCREEN_WIDTH - 524, SCREEN_HEIGHT - 263, 3, 44)
        pygame.draw.rect(self.screen, (64, 64, 64), line3_important)
        line4_important = pygame.Rect(SCREEN_WIDTH - 237, SCREEN_HEIGHT - 263, 3, 44)
        pygame.draw.rect(self.screen, (64, 64, 64), line4_important)

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

        # Кнопка "Назад"
        back_button = self.font_jersey50.render(TEXTS['back'], True, (64, 64, 64))
        back_rect = back_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.8))
        self.screen.blit(back_button, back_rect)

        # Обработка клика на кнопку "Назад"
        mouse_pos = pygame.mouse.get_pos()
        if back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (240, 143, 104), back_rect)
            back_button2 = self.font_jersey55.render(TEXTS['back'], True, (128, 128, 128))
            self.screen.blit(back_button2,
                             back_button.get_rect(center=(SCREEN_WIDTH // 2.02, SCREEN_HEIGHT * 0.796)))
            if pygame.mouse.get_pressed()[0]:
                self.click_effect.play(loops=0)
                self.start_window.is_tutorial = False