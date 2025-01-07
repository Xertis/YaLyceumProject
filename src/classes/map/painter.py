from pygame import surface
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

    def draw_grid(self):
        size = self.map.grid.grid_size

        for layer in self.map.grid.layers:
            for y in range(self.map.grid.height):
                for x in range(self.map.grid.width):
                    sprite = layer[x][y]
                    pos = (x * size, y * size)

                    if isinstance(sprite, surface.Surface):
                        LOADER.place(pos, sprite, self.map.screen)
                    elif isinstance(sprite, ANIMATOR):
                        sprite.place(pos, self.map.screen)

