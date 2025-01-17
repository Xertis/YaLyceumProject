import pygame
import math
from pygame import surface, Rect


class CONTROLLER:
    def __init__(self, map, radius, speed):
        self.map = map
        self.radius = radius
        self.speed = speed

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

        for y in range(grid_pos[1]-2, grid_pos[1]+2):
            for x in range(grid_pos[0]-2, grid_pos[0]+2):

                if (x  < 0 or x >= width or y < 0 or y >= height) or isinstance(self.map.grid.layers[1][x][y], float):
                    continue
                
                x1, y1 = x * size + step, y * size + step


                obj = Rect(
                    x1-size // 2, 
                    y1-size // 2, 
                    size,
                    size
                )

                if snake.colliderect(obj):
                    return True

        return False

    def snake_move(self, pos, speed=None):
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

        if_collision = self.collision((move_x + pos[0], move_y + pos[1]))

        if not if_collision:
            pos[0] += move_x
            pos[1] += move_y

        pos[0], pos[1] = int(pos[0]), int(pos[1])

        return pos
