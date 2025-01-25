import pygame
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
        self.is_reduce_vol = False
        self.is_increase_vol = False

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
        pygame.Surface.fill(self.screen, 'black')

        return_button = self.font_jersey50.render(
            TEXTS['return'], True, (229, 204, 255))

        return_button_width = return_button.get_width()
        return_button_x = (SCREEN_WIDTH - return_button_width) / 2
        return_button_y = SCREEN_HEIGHT * 0.7

        self.screen.blit(return_button, (return_button_x, return_button_y))

        return_button_rect = pygame.Rect(
            return_button_x - 10,
            return_button_y - 5,
            return_button_width + 20,
            70)


        volume_text = self.font_jersey65.render(
            TEXTS['volume'], True, (178, 102, 255))
        volume_text_width = volume_text.get_width()
        volume_text_x = (SCREEN_WIDTH - volume_text_width) / 2
        volume_text_y = SCREEN_HEIGHT * 0.18
        self.screen.blit(volume_text, (volume_text_x, volume_text_y))

        increase_volume_button = self.font_jersey65.render(
            TEXTS['+'], True, (229, 204, 255))
        increase_volume_button_width = increase_volume_button.get_width()
        increase_volume_button_x = (SCREEN_WIDTH - increase_volume_button_width) / 1.78
        increase_volume_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(increase_volume_button, (increase_volume_button_x, increase_volume_button_y))

        reduce_volume_button = self.font_jersey65.render(
            TEXTS['-'], True, (229, 204, 255))
        reduce_volume_button_width = increase_volume_button.get_width()
        reduce_volume_button_x = (SCREEN_WIDTH - reduce_volume_button_width) / 2.28
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
            str(round(self.volume * 10)), True, (178, 102, 255))
        volume_digit_width = volume_digit.get_width()
        volume_digit_x = (SCREEN_WIDTH - volume_digit_width) / 2
        volume_digit_y = SCREEN_HEIGHT * 0.36
        self.screen.blit(volume_digit, (volume_digit_x, volume_digit_y))

        pos = pygame.mouse.get_pos()

        if return_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', return_button_rect)

            return_button2 = self.font_jersey55.render(
                TEXTS['return'], True, (229, 204, 255))
            self.screen.blit(
                return_button2,
                (return_button_x - 6,
                 return_button_y - 2))

        if self.increase_volume_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', self.increase_volume_button_rect)

            increase_volume_button2 = self.font_jersey75.render(
                TEXTS['+'], True, (229, 204, 255))
            self.screen.blit(
                increase_volume_button2,
                (increase_volume_button_x - 1,
                 increase_volume_button_y - 5))

        if self.reduce_volume_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', self.reduce_volume_button_rect)

            reduce_volume_button2 = self.font_jersey75.render(
                TEXTS['-'], True, (229, 204, 255))
            self.screen.blit(
                reduce_volume_button2,
                (reduce_volume_button_x - 1,
                 reduce_volume_button_y - 5))

        if pygame.mouse.get_pressed(
        )[0] and return_button_rect.collidepoint(pos):
            self.start_window.is_options = False