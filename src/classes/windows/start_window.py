import pygame
from src.constants import SCREEN_NAME, TEXTS, SCREEN_WIDTH, SCREEN_HEIGHT

FONT_PATH = "res/fonts/Jersey10-Regular.ttf"

class DrawStartWindow:
    def __init__(self, scr, map):
        self.is_play = False
        self.screen = scr
        self.map = map
        self.font_jersey100 = pygame.font.Font(FONT_PATH, 100)
        self.font_jersey40 = pygame.font.Font(FONT_PATH, 60)
        self.draw()

    def draw(self):
        pygame.Surface.fill(self.screen, 'black')

        name_of_game = self.font_jersey100.render(SCREEN_NAME, False, (178, 102, 255))
        start_button = self.font_jersey40.render(TEXTS['start'], True, (229, 204, 255))
        rating_button = self.font_jersey40.render(TEXTS['rating'], True, (229, 204, 255))

        name_width = name_of_game.get_width()
        name_x = (SCREEN_WIDTH - name_width) / 2
        name_y = SCREEN_HEIGHT * 0.1

        start_button_width = start_button.get_width()
        start_button_x = (SCREEN_WIDTH - start_button_width) / 2
        start_button_y = SCREEN_HEIGHT * 0.4

        rating_button_width = rating_button.get_width()
        rating_button_x = (SCREEN_WIDTH - rating_button_width) / 2
        rating_button_y = SCREEN_HEIGHT * 0.5

        self.screen.blit(start_button, (start_button_x, start_button_y))
        self.screen.blit(rating_button, (rating_button_x, rating_button_y))
        self.screen.blit(name_of_game, (name_x, name_y))

        start_button_rect = pygame.Rect(start_button_x - 10, start_button_y - 5, start_button_width + 20, 70)
        rating_button_rect = pygame.Rect(rating_button_x - 10, rating_button_y - 5, rating_button_width + 20, 70)

        pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', start_button_rect)
            font = pygame.font.Font(FONT_PATH, 65)
            start_button2 = font.render(TEXTS['start'], True, (229, 204, 255))
            self.screen.blit(start_button2, (start_button_x - 15, start_button_y - 3))

        if rating_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', rating_button_rect)
            font = pygame.font.Font(FONT_PATH, 65)
            rating_button2 = font.render(TEXTS['rating'], True, (229, 204, 255))
            self.screen.blit(rating_button2, (rating_button_x - 10, rating_button_y - 3))

        if pygame.mouse.get_pressed()[0] == True and start_button_rect.collidepoint(pos):
            self.is_play = True
            self.map.draw()
