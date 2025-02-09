import pygame
from numpy.ma.core import swapaxes

from src.constants import SCREEN_NAME, TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils.loader import LOADER

FONT_PATH = "Jersey10-Regular.ttf"

class OPTIONS:
    def __init__(self, scr, start_window):
        self.screen = scr
        self.volume = pygame.mixer.Channel(0).get_volume()
        self.start_window = start_window
        self.font_jersey75 = LOADER.font.load(FONT_PATH, 75)
        self.font_jersey65 = LOADER.font.load(FONT_PATH, 65)
        self.font_jersey50 = LOADER.font.load(FONT_PATH, 50)
        self.font_jersey55 = LOADER.font.load(FONT_PATH, 55)
        self.apple = LOADER.sprite.load("apple.png", (38, 38))

        self.increase_volume_button = self.font_jersey65.render(
            TEXTS['+'], True, (229, 204, 255))
        self.increase_volume_button_width = self.increase_volume_button.get_width()
        self.increase_volume_button_x = (SCREEN_WIDTH - self.increase_volume_button_width) / 1.78
        self.increase_volume_button_y = SCREEN_HEIGHT * 0.3
        self.screen.blit(self.increase_volume_button, (self.increase_volume_button_x, self.increase_volume_button_y))

        self.reduce_volume_button = self.font_jersey65.render(
            TEXTS['-'], True, (229, 204, 255))
        self.reduce_volume_button_width = self.increase_volume_button.get_width()
        self.reduce_volume_button_x = (SCREEN_WIDTH - self.reduce_volume_button_width) / 2.28
        self.reduce_volume_button_y = SCREEN_HEIGHT * 0.3
        self.screen.blit(self.reduce_volume_button, (self.reduce_volume_button_x, self.reduce_volume_button_y))

        self.increase_volume_button_rect = pygame.Rect(
            self.increase_volume_button_x - 5,
            self.increase_volume_button_y + 20,
            self.increase_volume_button_width + 10,
            30)
        self.reduce_volume_button_rect = pygame.Rect(
            self.reduce_volume_button_x - 5,
            self.reduce_volume_button_y + 20,
            self.reduce_volume_button_width + 10,
            30)

    def draw(self):
        pygame.Surface.fill(self.screen, (220, 123, 84))

        back_rect = pygame.Rect(SCREEN_WIDTH - 455, SCREEN_HEIGHT - 150, 107, 55)
        pygame.draw.rect(self.screen, (240, 143, 104), back_rect)
        left_back_vignette = pygame.Rect(SCREEN_WIDTH - 460, SCREEN_HEIGHT - 155, 5, 65)
        pygame.draw.rect(self.screen, (0, 121, 13), left_back_vignette)
        right_back_vignette = pygame.Rect(SCREEN_WIDTH - 348, SCREEN_HEIGHT - 155, 5, 65)
        pygame.draw.rect(self.screen, (0, 121, 13), right_back_vignette)
        upper_back_vignette = pygame.Rect(SCREEN_WIDTH - 460, SCREEN_HEIGHT - 155, 117, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_back_vignette)
        lower_back_vignette = pygame.Rect(SCREEN_WIDTH - 460, SCREEN_HEIGHT - 95, 117, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_back_vignette)

        volume_rect = pygame.Rect(SCREEN_WIDTH - 490, SCREEN_HEIGHT - 385, 180, 50)
        pygame.draw.rect(self.screen, (240, 143, 104), volume_rect)
        left_volume_vignette = pygame.Rect(SCREEN_WIDTH - 495, SCREEN_HEIGHT - 390, 5, 60)
        pygame.draw.rect(self.screen, (0, 121, 13), left_volume_vignette)
        right_volume_vignette = pygame.Rect(SCREEN_WIDTH - 310, SCREEN_HEIGHT - 390, 5, 60)
        pygame.draw.rect(self.screen, (0, 121, 13), right_volume_vignette)
        upper_volume_vignette = pygame.Rect(SCREEN_WIDTH - 495, SCREEN_HEIGHT - 390, 190, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_volume_vignette)
        lower_volume_vignette = pygame.Rect(SCREEN_WIDTH - 495, SCREEN_HEIGHT - 335, 190, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_volume_vignette)

        self.screen.blit(self.apple, (400, 415))
        self.screen.blit(self.apple, (330, 180))


        return_button = self.font_jersey50.render(
            TEXTS['back'], True, (64, 64, 64))

        return_button_width = return_button.get_width()
        return_button_x = (SCREEN_WIDTH - return_button_width) / 2
        return_button_y = SCREEN_HEIGHT * 0.75

        self.screen.blit(return_button, (return_button_x, return_button_y))

        return_button_rect = pygame.Rect(
            return_button_x - 10,
            return_button_y + 5,
            return_button_width + 20,
            50)


        volume_text = self.font_jersey65.render(
            TEXTS['volume'], True, (0, 70, 0))
        volume_text_width = volume_text.get_width()
        volume_text_x = (SCREEN_WIDTH - volume_text_width) / 2
        volume_text_y = SCREEN_HEIGHT * 0.18
        self.screen.blit(volume_text, (volume_text_x, volume_text_y))

        increase_volume_button = self.font_jersey65.render(
            TEXTS['+'], True, (64, 64, 64))
        increase_volume_button_width = increase_volume_button.get_width()
        increase_volume_button_x = (SCREEN_WIDTH - increase_volume_button_width) / 1.70
        increase_volume_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(increase_volume_button, (increase_volume_button_x, increase_volume_button_y))

        reduce_volume_button = self.font_jersey65.render(
            TEXTS['-'], True, (64, 64, 64))
        reduce_volume_button_width = increase_volume_button.get_width()
        reduce_volume_button_x = (SCREEN_WIDTH - reduce_volume_button_width) / 2.41
        reduce_volume_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(reduce_volume_button, (reduce_volume_button_x, reduce_volume_button_y))

        self.increase_volume_button_rect = pygame.Rect(
            increase_volume_button_x - 5,
            increase_volume_button_y + 20,
            increase_volume_button_width + 10,
            30)

        self.reduce_volume_button_rect = pygame.Rect(
            reduce_volume_button_x - 5,
            reduce_volume_button_y + 20,
            reduce_volume_button_width + 10,
            30)


        volume_digit = self.font_jersey55.render(
            str(round(self.volume * 10)), True, (0, 121, 13))
        volume_digit_width = volume_digit.get_width()
        volume_digit_x = (SCREEN_WIDTH - volume_digit_width) / 2
        volume_digit_y = SCREEN_HEIGHT * 0.36
        self.screen.blit(volume_digit, (volume_digit_x, volume_digit_y))

        pos = pygame.mouse.get_pos()

        if return_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), return_button_rect)

            return_button2 = self.font_jersey55.render(
                TEXTS['back'], True, (64, 64, 64))
            self.screen.blit(
                return_button2,
                (return_button_x - 6,
                 return_button_y - 2))

        if self.increase_volume_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), self.increase_volume_button_rect)

            increase_volume_button2 = self.font_jersey75.render(
                TEXTS['+'], True, (64, 64, 64))
            self.screen.blit(
                increase_volume_button2,
                (increase_volume_button_x - 1,
                 increase_volume_button_y - 5))

        if self.reduce_volume_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), self.reduce_volume_button_rect)

            reduce_volume_button2 = self.font_jersey75.render(
                TEXTS['-'], True, (64, 64, 64))
            self.screen.blit(
                reduce_volume_button2,
                (reduce_volume_button_x - 1,
                 reduce_volume_button_y - 5))

        if pygame.mouse.get_pressed(
        )[0] and return_button_rect.collidepoint(pos):
            self.start_window.is_options = False