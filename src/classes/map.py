import pygame
import numpy as np
from noise import snoise2
from src.classes.snake.snake import SNAKE


class MAP:
    def __init__(self, w, h, s: pygame.surface.Surface):
        self.width = w
        self.height = h
        self.screen = s
        self.snake = SNAKE(15, self, [15, 15])
        self.background = np.zeros((self.height, self.width))

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
            pygame.draw.circle(self.screen, "red", segment, self.snake.radius)

        pygame.draw.circle(self.screen, "white", self.snake.pos, self.snake.radius)
    
    def generate(self, seed, conf=None):
        if conf is None:
            conf = {
                "scale": 0.005,
                "octaves": 6,
                "persistence": 0.5,
                "lacunarity": 2.0
            }

        scale = conf["scale"]
        octaves = conf["octaves"]
        persistence = conf["persistence"]
        lacunarity = conf["lacunarity"]
        
        for y in range(self.height):
            for x in range(self.width):
                noise_level = snoise2(
                    x * scale,
                    y * scale, 
                    base=seed,
                    octaves=octaves, 
                    persistence=persistence, 
                    lacunarity=lacunarity
                )
                self.background[y][x] = noise_level