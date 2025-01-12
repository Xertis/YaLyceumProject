import pygame

class DrawStartWindow:
    def __init__(self, scr, map):
        self.is_play = False
        self.screen = scr
        self.map = map
        self.font_jersey100 = pygame.font.Font('res/fonts/Jersey10-Regular.ttf', 100)
        self.font_jersey40 = pygame.font.Font('res/fonts/Jersey10-Regular.ttf', 60)
        self.draw()

    def draw(self):
        pygame.Surface.fill(self.screen, 'black')
        name_of_game = self.font_jersey100.render('Gravity Snake', False, (178, 102, 255))
        start_button = self.font_jersey40.render('Start game', True, (229, 204, 255))
        rating_button = self.font_jersey40.render('Rating', True, (229, 204, 255))
        self.screen.blit(name_of_game, (160, 50))
        self.screen.blit(start_button, (280, 200))
        self.screen.blit(rating_button, (333, 300))

        start_button_rect = pygame.Rect(275, 195, 250, 70)
        rating_button_rect = pygame.Rect(328, 295, 250, 70)

        pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(pos):
            rect = pygame.Rect(275, 195, 250, 70)
            pygame.draw.rect(self.screen, 'black', rect)
            font = pygame.font.Font('res/fonts/Jersey10-Regular.ttf', 65)
            start_button2 = font.render('Start game', True, (229, 204, 255))
            self.screen.blit(start_button2, (270, 197))

        if rating_button_rect.collidepoint(pos):
            rect = pygame.Rect(328, 295, 250, 70)
            pygame.draw.rect(self.screen, 'black', rect)
            font = pygame.font.Font('res/fonts/Jersey10-Regular.ttf', 65)
            rating_button2 = font.render('Rating', True, (229, 204, 255))
            self.screen.blit(rating_button2, (328, 297))

        if pygame.mouse.get_pressed()[0] == True and start_button_rect.collidepoint(pos):
            self.is_play = True
            self.map.draw()
