import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TEXTS
from src.utils.loader import LOADER

FONT_PATH = "Jersey10-Regular.ttf"

class PAUSE:
    def __init__(self, scr, start_window):
        self.screen = scr
        self.start_window = start_window

        self.font_jersey65 = LOADER.font.load(FONT_PATH, 65)
        self.font_jersey60 = LOADER.font.load(FONT_PATH, 60)
        self.font_jersey80 = LOADER.font.load(FONT_PATH, 80)

    def draw(self):
        pause_rect = pygame.Rect(SCREEN_WIDTH - 650, SCREEN_HEIGHT - 500, 500, 350)
        pygame.draw.rect(self.screen, 'black', pause_rect)

        left_vignette = pygame.Rect(pause_rect.width - 350, pause_rect.height - 255, 18, 370)
        pygame.draw.rect(self.screen, (178, 102, 255), left_vignette)

        right_vignette = pygame.Rect(pause_rect.width + 135, pause_rect.height - 255, 18, 370)
        pygame.draw.rect(self.screen, (178, 102, 255), right_vignette)

        upper_vignette = pygame.Rect(pause_rect.width - 350, pause_rect.height - 255, 500, 18)
        pygame.draw.rect(self.screen, (178, 102, 255), upper_vignette)

        lower_vignette = pygame.Rect(pause_rect.width - 350, pause_rect.height + 100, 500, 18)
        pygame.draw.rect(self.screen, (178, 102, 255), lower_vignette)

        exit_question = self.font_jersey80.render(TEXTS["exit?"], True, (178, 102, 255))
        exit_question_width = exit_question.get_width()
        exit_question_x = (pause_rect.width - exit_question_width) / 1.1
        exit_question_y = pause_rect.height * 0.5

        no_button = self.font_jersey60.render(TEXTS['no'], True, (229, 204, 255))
        no_button_width = no_button.get_width()
        no_button_x = (pause_rect.width - no_button_width) / 1.8
        no_button_y = pause_rect.height * 0.9

        yes_button = self.font_jersey60.render(TEXTS['yes'], True, (229, 204, 255))
        yes_button_width = yes_button.get_width()
        yes_button_x = (pause_rect.width - yes_button_width) / 0.87
        yes_button_y = pause_rect.height * 0.9

        self.screen.blit(exit_question, (exit_question_x, exit_question_y))
        self.screen.blit(no_button, (no_button_x, no_button_y))
        self.screen.blit(yes_button, (yes_button_x, yes_button_y))

        no_button_rect = pygame.Rect(no_button_x - 10, no_button_y + 10, no_button_width + 14, 45)
        yes_button_rect = pygame.Rect(yes_button_x - 10, yes_button_y + 10, yes_button_width + 14, 50)

        pos = pygame.mouse.get_pos()
        if no_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', no_button_rect)
            no_button2 = self.font_jersey65.render(TEXTS['no'], True, (229, 204, 255))
            self.screen.blit(no_button2, (no_button_x - 2, no_button_y - 3))

        if yes_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, 'black', yes_button_rect)
            yes_button2 = self.font_jersey65.render(TEXTS['yes'], True, (229, 204, 255))
            self.screen.blit(yes_button2, (yes_button_x - 2, yes_button_y - 3))

        if pygame.mouse.get_pressed()[0] == True and no_button_rect.collidepoint(pos):
            pygame.mixer.Channel(0).pause()
            self.start_window.is_play = True
            self.start_window.is_pause = False

        if pygame.mouse.get_pressed()[0] == True and yes_button_rect.collidepoint(pos):
            self.start_window.is_pause = False