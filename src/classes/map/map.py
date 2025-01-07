import pygame
import numpy as np
from src.classes.snake.snake import SNAKE
from src.classes.sprites.sprites_loader import LOADER
from src.classes.sprites.sprites_animator import ANIMATOR
from src.classes.map.painter import PAINTER
from src.classes.map.grid import GRID
from random import randint


class MAP:
    def __init__(self, w, h, s: pygame.surface.Surface):
        self.width = w
        self.height = h
        self.screen = s

        self.snake = SNAKE(16, self, [15, 15])

        self.snake_head_sprite = LOADER.load("snake_head.png", (38, 38*4))
        self.snake_tail_sprite = LOADER.load("snake_tail.png", (38, 38))
        self.background_sprite = LOADER.load("background.png", (38, 38*4))
        self.platform_sprite = LOADER.load("platform.png", (38, 38))

        self.snake_head_sprite = ANIMATOR(self.snake_head_sprite, 0.5*33*20)
        self.background_sprite = ANIMATOR(self.background_sprite, 50*33.20)

        self.painter = PAINTER(self)
        self.grid = GRID(self)
        self.grid.set_background(self.background_sprite)

    def get_size(self):
        return (self.width, self.height)

    def draw(self):
        self.painter.draw_grid()
        self.painter.draw_snake()

    def generate(self):
        # ТЕСТ ГЕНЕРАЦИИ, НЕ ИТОГОВЫЙ ВАРИАНТ
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                z = randint(0, 2)

                if z == 0:
                    self.grid.set(1, x, y, self.platform_sprite)
