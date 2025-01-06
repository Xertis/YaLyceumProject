import pygame
import numpy as np
from src.classes.snake.snake import SNAKE
from src.classes.sprites.sprites_loader import LOADER
from src.classes.sprites.sprites_animator import ANIMATOR


class PAINTER:
    def __init__(self, map):
        self.map = map

    def draw_snake(self):
        for segment in self.map.snake.tail:
            LOADER.place(segment, self.map.snake_tail_sprite, self.map.screen, 0)

        self.map.snake_head_sprite.place(self.map.snake.pos, self.map.screen, 0)

