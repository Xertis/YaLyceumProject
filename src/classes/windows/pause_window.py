import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TEXTS
from src.utils.loader import LOADER

FONT_PATH = "Jersey10-Regular.ttf"
CLICK_EFFECT_PATH = "click_effect.wav"
START_WINDOW_MUSIC_PATH = "Fluffing-a-Duck (start window sound).mp3"
GAME_MUSIC_PATH = 'game_music.mp3'

class PAUSE:
    def __init__(self, scr, start_window, map_win):
        self.screen = scr
        self.start_window = start_window
        self.map_window = map_win

        self.font_jersey65 = LOADER.font.load(FONT_PATH, 65)
        self.font_jersey60 = LOADER.font.load(FONT_PATH, 60)
        self.font_jersey80 = LOADER.font.load(FONT_PATH, 80)
        self.apple = LOADER.sprite.load("apple.png", (38, 38))
        self.settings = LOADER.sprite.load("settings.png", (40, 40))
        self.settings2 = LOADER.sprite.load("settings.png", (45, 45))

        self.click_effect = LOADER.sound.load(CLICK_EFFECT_PATH)

        self.start_window_music = pygame.mixer.Channel(0)
        self.music = LOADER.sound.load(START_WINDOW_MUSIC_PATH)
        self.game_music = pygame.mixer.Channel(0)
        self.music2 = LOADER.sound.load(GAME_MUSIC_PATH)

    def draw(self):
        self.click_effect.set_volume(pygame.mixer.Channel(1).get_volume())
        pause_rect = pygame.Rect(SCREEN_WIDTH - 650, SCREEN_HEIGHT - 500, 500, 350)
        pygame.draw.rect(self.screen, (240, 143, 104), pause_rect)

        self.screen.blit(self.apple, (500, 414))
        self.screen.blit(self.apple, (326, 170))
        self.screen.blit(self.settings, (570, 130))
        settings_rect = pygame.Rect(SCREEN_WIDTH - 232, SCREEN_HEIGHT - 475, 45, 45)

        left_vignette = pygame.Rect(pause_rect.width - 350, pause_rect.height - 255, 18, 370)
        pygame.draw.rect(self.screen, (0, 121, 13), left_vignette)

        right_vignette = pygame.Rect(pause_rect.width + 135, pause_rect.height - 255, 18, 370)
        pygame.draw.rect(self.screen, (0, 121, 13), right_vignette)

        upper_vignette = pygame.Rect(pause_rect.width - 350, pause_rect.height - 255, 500, 18)
        pygame.draw.rect(self.screen, (0, 121, 13), upper_vignette)

        lower_vignette = pygame.Rect(pause_rect.width - 350, pause_rect.height + 100, 500, 18)
        pygame.draw.rect(self.screen, (0, 121, 13), lower_vignette)

        exit_question = self.font_jersey80.render(TEXTS["exit?"], True, (0, 70, 0))
        exit_question_width = exit_question.get_width()
        exit_question_x = (pause_rect.width - exit_question_width) / 1.1
        exit_question_y = pause_rect.height * 0.5

        no_button = self.font_jersey60.render(TEXTS['no'], True, (64, 64, 64))
        no_button_width = no_button.get_width()
        no_button_x = (pause_rect.width - no_button_width) / 1.8
        no_button_y = pause_rect.height * 0.9

        yes_button = self.font_jersey60.render(TEXTS['yes'], True, (64, 64, 64))
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
            pygame.draw.rect(self.screen, (240, 143, 104), no_button_rect)
            no_button2 = self.font_jersey65.render(TEXTS['no'], True, (128, 128, 128))
            self.screen.blit(no_button2, (no_button_x - 2, no_button_y - 3))
            if pygame.mouse.get_pressed()[0] == True and no_button_rect.collidepoint(pos):
                self.click_effect.play(loops=0)
                self.start_window.is_play = True
                self.start_window.is_pause = False

        if yes_button_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), yes_button_rect)
            yes_button2 = self.font_jersey65.render(TEXTS['yes'], True, (128, 128, 128))
            self.screen.blit(yes_button2, (yes_button_x - 2, yes_button_y - 3))
            if pygame.mouse.get_pressed()[0] == True and yes_button_rect.collidepoint(pos):
                self.click_effect.play(loops=0)
                self.game_music.stop()
                self.start_window_music.play(self.music, loops=-1)
                self.start_window.is_pause = False
                self.map_window.snake.tail = [
                                    [0, 0],
                                    [0, 0],
                                    [0, 0]
                ]
                self.map_window.snake.pos = [15, 15]
                self.map_window.snake.score = 0

        if settings_rect.collidepoint(pos):
            pygame.draw.rect(self.screen, (240, 143, 104), settings_rect)
            self.screen.blit(self.settings2, (567, 127))
            if pygame.mouse.get_pressed()[0] == True and settings_rect.collidepoint(pos):
                self.start_window.is_options = True
                self.map_window.generate()

