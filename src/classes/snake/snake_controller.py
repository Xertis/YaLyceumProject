import pygame
import math
import time
from pygame import surface, Rect
from src.utils.loader import LOADER

MOVE_EFFECT_PATH = 'move_effect.wav'
MUSIC_PATH = "Fluffing-a-Duck (start window sound).mp3"


class CONTROLLER:
    def __init__(self, map, radius, speed, start_window):
        self.map = map
        self.radius = radius
        self.speed = speed
        self.start = 0
        self.start_window = start_window

        self.move_effect = LOADER.sound.load(MOVE_EFFECT_PATH)

    def collision(self, pos):
        snake = Rect(
            pos[0] - self.radius,
            pos[1] - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        size = self.map.grid.grid_size
        step = size // 2

        width, height = self.map.grid.width, self.map.grid.height

        grid_pos = math.floor(pos[0] / size), math.floor(pos[1] / size)

        for y in range(grid_pos[1] - 2, grid_pos[1] + 2):
            for x in range(grid_pos[0] - 2, grid_pos[0] + 2):

                if (x < 0 or x >= width or y < 0 or y >= height) or isinstance(
                        self.map.grid.layers[1][x][y], float):
                    continue

                x1, y1 = x * size, y * size

                obj = Rect(
                    x1,
                    y1,
                    size,
                    size
                )

                if snake.colliderect(obj):
                    return True

        return False

    def snake_move(self, pos, speed=None):
        self.move_effect.set_volume(pygame.mixer.Channel(1).get_volume())
        keys = pygame.key.get_pressed()
        move_x, move_y = 0, 0

        if speed is None:
            speed = self.speed

        speed *= 10

        if keys[pygame.K_a]:
            move_x = -speed
        if keys[pygame.K_d]:
            move_x = speed
        if keys[pygame.K_w]:
            move_y = -speed
        if keys[pygame.K_s]:
            move_y = speed
        if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
            if time.time() - self.start > 1:
                self.start = time.time() - 0.5
                self.move_effect.play(loops=0)
        if keys[pygame.K_ESCAPE]:
            self.start_window.is_play = False
            self.start_window.is_pause = True
            channel = pygame.mixer.Channel(0)
            channel.unpause()

        if_collision = self.collision((move_x + pos[0], move_y + pos[1]))

        if not if_collision:
            pos[0] += move_x
            pos[1] += move_y

        pos[0], pos[1] = int(pos[0]), int(pos[1])
        
        return pos
