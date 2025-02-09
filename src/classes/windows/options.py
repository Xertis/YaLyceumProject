import pygame
from numpy.ma.core import swapaxes

from src.constants import SCREEN_NAME, TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils.loader import LOADER

FONT_PATH = "Jersey10-Regular.ttf"
CLICK_EFFECT_PATH = "click_effect.wav"

class OPTIONS:
    def __init__(self, scr, start_window):
        self.screen = scr
        self.click_effect = LOADER.sound.load(CLICK_EFFECT_PATH)
        self.effect = pygame.mixer.Channel(1).get_volume()
        self.music = pygame.mixer.Channel(0).get_volume()
        self.start_window = start_window
        self.font_jersey75 = LOADER.font.load(FONT_PATH, 75)
        self.font_jersey65 = LOADER.font.load(FONT_PATH, 65)
        self.font_jersey50 = LOADER.font.load(FONT_PATH, 50)
        self.font_jersey55 = LOADER.font.load(FONT_PATH, 55)
        self.apple = LOADER.sprite.load("apple.png", (38, 38))
        self.background = LOADER.sprite.load("menu_background.png", (1374, 1259))

        self.increase_music_button = self.font_jersey65.render(
            TEXTS['+'], True, (229, 204, 255))
        self.increase_music_button_width = self.increase_music_button.get_width()
        self.increase_music_button_x = (SCREEN_WIDTH - self.increase_music_button_width) / 1.78
        self.increase_music_button_y = SCREEN_HEIGHT * 0.3
        self.screen.blit(self.increase_music_button, (self.increase_music_button_x, self.increase_music_button_y))

        self.reduce_music_button = self.font_jersey65.render(
            TEXTS['-'], True, (229, 204, 255))
        self.reduce_music_button_width = self.increase_music_button.get_width()
        self.reduce_music_button_x = (SCREEN_WIDTH - self.reduce_music_button_width) / 2.28
        self.reduce_music_button_y = SCREEN_HEIGHT * 0.3
        self.screen.blit(self.reduce_music_button, (self.reduce_music_button_x, self.reduce_music_button_y))

        self.increase_music_button_rect = pygame.Rect(
            self.increase_music_button_x - 5,
            self.increase_music_button_y + 20,
            self.increase_music_button_width + 10,
            30)
        self.reduce_music_button_rect = pygame.Rect(
            self.reduce_music_button_x - 5,
            self.reduce_music_button_y + 20,
            self.reduce_music_button_width + 10,
            30)

        self.increase_effects_button = self.font_jersey65.render(
            TEXTS['+'], True, (64, 64, 64))
        self.increase_effects_button_width = self.increase_effects_button.get_width()
        self.increase_effects_button_x = (SCREEN_WIDTH - self.increase_effects_button_width) / 1.32
        self.increase_effects_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(self.increase_effects_button, (self.increase_effects_button_x, self.increase_effects_button_y))

        self.reduce_effects_button = self.font_jersey65.render(
            TEXTS['-'], True, (64, 64, 64))
        self.reduce_effects_button_width = self.reduce_effects_button.get_width()
        self.reduce_effects_button_x = (SCREEN_WIDTH - self.reduce_effects_button_width) / 1.65
        self.reduce_effects_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(self.reduce_effects_button, (self.reduce_effects_button_x, self.reduce_effects_button_y))

        self.increase_effects_button_rect = pygame.Rect(
            self.increase_effects_button_x - 5,
            self.increase_effects_button_y + 20,
            self.increase_effects_button_width + 10,
            30)

        self.reduce_effects_button_rect = pygame.Rect(
            self.reduce_effects_button_x - 5,
            self.reduce_effects_button_y + 20,
            self.reduce_effects_button_width + 10,
            30)

    def draw(self):
        self.screen.blit(self.background, (-230, -285))
        self.click_effect.set_volume(pygame.mixer.Channel(1).get_volume())

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

        music_rect = pygame.Rect(SCREEN_WIDTH - 640, SCREEN_HEIGHT - 385, 180, 50)
        pygame.draw.rect(self.screen, (240, 143, 104), music_rect)
        left_music_vignette = pygame.Rect(SCREEN_WIDTH - 645, SCREEN_HEIGHT - 390, 5, 60)
        pygame.draw.rect(self.screen, (0, 121, 13), left_music_vignette)
        right_music_vignette = pygame.Rect(SCREEN_WIDTH - 460, SCREEN_HEIGHT - 390, 5, 60)
        pygame.draw.rect(self.screen, (0, 121, 13), right_music_vignette)
        upper_music_vignette = pygame.Rect(SCREEN_WIDTH - 645, SCREEN_HEIGHT - 390, 190, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_music_vignette)
        lower_music_vignette = pygame.Rect(SCREEN_WIDTH - 645, SCREEN_HEIGHT - 335, 190, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_music_vignette)

        effects_rect = pygame.Rect(SCREEN_WIDTH - 350, SCREEN_HEIGHT - 385, 180, 50)
        pygame.draw.rect(self.screen, (240, 143, 104), effects_rect)
        left_effects_vignette = pygame.Rect(SCREEN_WIDTH - 355, SCREEN_HEIGHT - 390, 5, 60)
        pygame.draw.rect(self.screen, (0, 121, 13), left_effects_vignette)
        right_effects_vignette = pygame.Rect(SCREEN_WIDTH - 170, SCREEN_HEIGHT - 390, 5, 60)
        pygame.draw.rect(self.screen, (0, 121, 13), right_effects_vignette)
        upper_effects_vignette = pygame.Rect(SCREEN_WIDTH - 355, SCREEN_HEIGHT - 390, 190, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_effects_vignette)
        lower_effects_vignette = pygame.Rect(SCREEN_WIDTH - 355, SCREEN_HEIGHT - 335, 190, 5)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_effects_vignette)

        self.screen.blit(self.apple, (400, 415))
        self.screen.blit(self.apple, (170, 180))


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
        volume_text_x = (SCREEN_WIDTH - volume_text_width) / 2.05
        volume_text_y = SCREEN_HEIGHT * 0.05
        self.screen.blit(volume_text, (volume_text_x, volume_text_y))

        music_text = self.font_jersey50.render(
            TEXTS['music'], True, (0, 70, 0))
        music_text_width = music_text.get_width()
        music_text_x = (SCREEN_WIDTH - music_text_width) / 3.45
        music_text_y = SCREEN_HEIGHT * 0.45
        self.screen.blit(music_text, (music_text_x, music_text_y))

        effects_text = self.font_jersey50.render(
            TEXTS['effects'], True, (0, 70, 0))
        effects_text_width = effects_text.get_width()
        effects_text_x = (SCREEN_WIDTH - effects_text_width) / 1.4
        effects_text_y = SCREEN_HEIGHT * 0.45
        self.screen.blit(effects_text, (effects_text_x, effects_text_y))

        increase_music_button = self.font_jersey65.render(
            TEXTS['+'], True, (64, 64, 64))
        increase_music_button_width = increase_music_button.get_width()
        increase_music_button_x = (SCREEN_WIDTH - increase_music_button_width) / 2.6
        increase_music_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(increase_music_button, (increase_music_button_x, increase_music_button_y))

        reduce_music_button = self.font_jersey65.render(
            TEXTS['-'], True, (64, 64, 64))
        reduce_music_button_width = reduce_music_button.get_width()
        reduce_music_button_x = (SCREEN_WIDTH - reduce_music_button_width) / 4.3
        reduce_music_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(reduce_music_button, (reduce_music_button_x, reduce_music_button_y))

        self.increase_music_button_rect = pygame.Rect(
            increase_music_button_x - 5,
            increase_music_button_y + 20,
            increase_music_button_width + 10,
            30)

        self.reduce_music_button_rect = pygame.Rect(
            reduce_music_button_x - 5,
            reduce_music_button_y + 20,
            reduce_music_button_width + 10,
            30)

        increase_effects_button = self.font_jersey65.render(
            TEXTS['+'], True, (64, 64, 64))
        increase_effects_button_width = increase_effects_button.get_width()
        increase_effects_button_x = (SCREEN_WIDTH - increase_effects_button_width) / 1.32
        increase_effects_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(increase_effects_button, (increase_effects_button_x, increase_effects_button_y))

        reduce_effects_button = self.font_jersey65.render(
            TEXTS['-'], True, (64, 64, 64))
        reduce_effects_button_width = reduce_effects_button.get_width()
        reduce_effects_button_x = (SCREEN_WIDTH - reduce_effects_button_width) / 1.65
        reduce_effects_button_y = SCREEN_HEIGHT * 0.35
        self.screen.blit(reduce_effects_button, (reduce_effects_button_x, reduce_effects_button_y))

        self.increase_effects_button_rect = pygame.Rect(
            increase_effects_button_x - 5,
            increase_effects_button_y + 20,
            increase_effects_button_width + 10,
            30)

        self.reduce_effects_button_rect = pygame.Rect(
            reduce_effects_button_x - 5,
            reduce_effects_button_y + 20,
            reduce_effects_button_width + 10,
            30)


        music_digit = self.font_jersey55.render(
            str(round(self.music * 10)), True, (200, 0, 0))
        music_digit_width = music_digit.get_width()
        music_digit_x = (SCREEN_WIDTH - music_digit_width) / 3.27
        music_digit_y = SCREEN_HEIGHT * 0.36
        self.screen.blit(music_digit, (music_digit_x, music_digit_y))

        effects_digit = self.font_jersey55.render(
            str(round(self.effect * 10)), True, (200, 0, 0))
        effects_digit_width = effects_digit.get_width()
        effects_digit_x = (SCREEN_WIDTH - effects_digit_width) / 1.46
        effects_digit_y = SCREEN_HEIGHT * 0.36
        self.screen.blit(effects_digit, (effects_digit_x, effects_digit_y))

        pos = pygame.mouse.get_pos()

        if return_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), return_button_rect)

            return_button2 = self.font_jersey55.render(
                TEXTS['back'], True, (128, 128, 128))
            self.screen.blit(
                return_button2,
                (return_button_x - 6,
                 return_button_y - 2))

        if self.increase_music_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), self.increase_music_button_rect)

            increase_music_button2 = self.font_jersey75.render(
                TEXTS['+'], True, (128, 128, 128))
            self.screen.blit(
                increase_music_button2,
                (increase_music_button_x - 1,
                 increase_music_button_y - 5))

        if self.reduce_music_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), self.reduce_music_button_rect)

            reduce_music_button2 = self.font_jersey75.render(
                TEXTS['-'], True, (128, 128, 128))
            self.screen.blit(
                reduce_music_button2,
                (reduce_music_button_x - 1,
                 reduce_music_button_y - 5))

        if self.increase_effects_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), self.increase_effects_button_rect)

            increase_effects_button2 = self.font_jersey75.render(
                TEXTS['+'], True, (128, 128, 128))
            self.screen.blit(
                increase_effects_button2,
                (increase_effects_button_x - 1,
                 increase_effects_button_y - 5))

        if self.reduce_effects_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), self.reduce_effects_button_rect)

            reduce_effects_button2 = self.font_jersey75.render(
                TEXTS['-'], True, (128, 128, 128))
            self.screen.blit(
                reduce_effects_button2,
                (reduce_effects_button_x - 1,
                 reduce_effects_button_y - 5))

        if pygame.mouse.get_pressed(
        )[0] and return_button_rect.collidepoint(pos):
            self.click_effect.play(loops=0)
            self.start_window.is_options = False