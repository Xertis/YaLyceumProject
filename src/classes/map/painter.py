from pygame import surface
import numpy as np
from src.classes.snake.snake import SNAKE
from src.utils.loader import LOADER
from src.classes.sprites.sprites_animator import ANIMATOR


class PAINTER:
    def __init__(self, map):
        self.map = map

    def draw_snake(self):
        for segment in self.map.snake.tail:
            LOADER.sprite.place(
                segment,
                self.map.snake_tail_sprite,
                self.map.screen,
                0)

        self.map.snake_head_sprite.place(
            self.map.snake.pos, self.map.screen, 0)

    def draw_score(self):
        score_text = LOADER.font.load("Jersey10-Regular.ttf", 30).render(
            f"Apples {self.map.snake.score}",
            True,
            (255, 255, 255)
        )
        self.map.screen.blit(score_text, (10, 10))

    def draw_rating(self, scores):
        y = 100
        for i, score in enumerate(scores[:10], 1):
            text = LOADER.font.load("Jersey10-Regular.ttf", 40).render(
                f"{i}. {score}",
                True,
                (255, 255, 255)
            )
            self.map.screen.blit(text, (100, y))
            y += 50
    def draw_grid(self):
        size = self.map.grid.grid_size
        step = + size // 2

        for layer in self.map.grid.layers:
            for y in range(self.map.grid.height):
                for x in range(self.map.grid.width):
                    sprite = layer[x][y]
                    pos = self.map.grid.pos_conv([x, y])

                    if isinstance(sprite, surface.Surface):
                        LOADER.sprite.place(pos, sprite, self.map.screen)
                    elif isinstance(sprite, ANIMATOR):
                        sprite.place(pos, self.map.screen)
