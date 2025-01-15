import pygame
from src.classes.snake.snake import SNAKE
from src.utils.loader import LOADER
from src.classes.sprites.sprites_animator import ANIMATOR
from src.classes.map.painter import PAINTER
from src.classes.map.grid import GRID
from src.classes.generation.generator import GENERATOR
import time


class MAP:
    def __init__(self, w, h, s: pygame.surface.Surface):
        self.width = w
        self.height = h
        self.screen = s

        self.snake = SNAKE(16, self, [15, 15])

        self.snake_head_sprite = LOADER.sprite.load("snake_head.png", (38, 38*4))
        self.snake_tail_sprite = LOADER.sprite.load("snake_tail.png", (38, 38))
        self.background_sprite = LOADER.sprite.load("background.png", (38, 38))
        self.platform_sprite = LOADER.sprite.load("platform.png", (38, 38*5))

        self.snake_head_sprite = ANIMATOR(self.snake_head_sprite, 0.5*33*20)
        self.platform_sprite = ANIMATOR(self.platform_sprite, 5*33.20)

        self.painter = PAINTER(self)
        self.grid = GRID(self)
        self.grid.set_background(self.background_sprite)

    def get_size(self):
        return (self.width, self.height)

    def draw(self):
        self.painter.draw_grid()
        self.painter.draw_snake()

    def generate(self):
        w, h = self.grid.width, self.grid.height
        visited = [(w // 2, h // 2)]
        obj = self.platform_sprite

        for i in range(8):
            GENERATOR.generate(int(time.time()) + i, self.grid.layers[1], visited, obj)
