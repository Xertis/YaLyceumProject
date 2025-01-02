import pygame
import numpy as np
from src.classes.snake.snake import SNAKE
from src.classes.sprites.sprites_loader import LOADER
from src.classes.sprites.sprites_animator import ANIMATOR


class MAP:
    def __init__(self, w, h, s: pygame.surface.Surface):
        self.width = w
        self.height = h
        self.screen = s
        self.snake = SNAKE(15, self, [15, 15])
        self.background = np.zeros((self.height, self.width))

        self.snake_head_sprite = LOADER.load("snake_head.png", (38, 38*4))
        self.snake_tail_sprite = LOADER.load("snake_tail.png", (38, 38))

        self.snake_head_sprite = ANIMATOR(self.snake_head_sprite, True)

    def get_size(self):
        return (self.width, self.height)

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                noise_value = self.background[y][x]
                if noise_value > 0.2:
                    self.screen.set_at((x, y), "green")

        self.screen.fill("black")

        for segment in self.snake.tail:
            LOADER.place(segment, self.snake_tail_sprite, self.screen, 0)

        self.snake_head_sprite.place(self.snake.pos, self.screen, 0)

    def generate(self, seed, conf=None):
        pass
