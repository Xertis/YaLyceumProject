import pygame
from src.constants import SCREEN_NAME, TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils.loader import LOADER

FONT_PATH = "Jersey10-Regular.ttf"

class RATING:
    def __init__(self, scr, start_window):
        self.screen = scr
        self.start_window = start_window

        self.font_jersey50 = LOADER.font.load(FONT_PATH, 50)
        self.font_jersey55 = LOADER.font.load(FONT_PATH, 55)

    def draw(self):
        pygame.Surface.fill(self.screen, "black")

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

        pos = pygame.mouse.get_pos()

        if return_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', return_button_rect)

            return_button2 = self.font_jersey55.render(
                TEXTS['return'], True, (229, 204, 255))
            self.screen.blit(
                return_button2,
                (return_button_x - 6,
                 return_button_y - 2))

        if pygame.mouse.get_pressed(
        )[0] and return_button_rect.collidepoint(pos):
            self.start_window.is_rating = False