import pygame
import numpy as np
from src.classes.snake.snake import SNAKE
from src.classes.sprites.sprites_loader import LOADER
from src.classes.sprites.sprites_animator import ANIMATOR
from src.classes.map.painter import PAINTER


class MAP:
    def __init__(self, w, h, s: pygame.surface.Surface):
        self.width = w
        self.height = h
        self.screen = s

        self.grid_size = 20
        self.grid = np.zeros((w // self.grid_size, h // self.grid_size))

        self.snake = SNAKE(16, self, [15, 15])
        self.background = np.zeros((self.height, self.width))

        self.snake_head_sprite = LOADER.load("snake_head.png", (38, 38*4))
        self.snake_tail_sprite = LOADER.load("snake_tail.png", (38, 38))

        self.snake_head_sprite = ANIMATOR(self.snake_head_sprite, True)

        self.painter = PAINTER(self)

    def get_size(self):
        return (self.width, self.height)

    def draw(self):
        self.screen.fill("black")

        self.painter.draw_snake()

    def generate(self, seed, conf=None):
        pass
