import math
import copy
from pygame import Rect

DIRECTIONS = (
    (0, 1),  # Вниз
    (0, -1), # Вверх
    (1, 0),  # Вправо
    (-1, 0), # Влево
)

class GRAVITATION:
    def __init__(self, controller):
        self.controller = controller
        self.map = controller.map
        self.dir = 2    #0 - вниз, 1 - вверх, 2 - вправо, 3 - влево
        self.fall_speed = 1

    def __collision__(self, segment, platform):
        size = self.map.grid.grid_size
        step = size // 2

        x1, y1 = platform[0] * size, platform[1] * size

        segment = Rect(
            segment[0] - self.map.snake.radius,
            segment[1] - self.map.snake.radius,
            self.map.snake.radius * 2,
            self.map.snake.radius * 2
        )

        _platform = Rect(
            x1-1,
            y1-1,
            size+2,
            size+2
        )

        return segment.colliderect(_platform)

    def __check_holding__(self):
        tail = copy.deepcopy(self.map.snake.tail)
        head = copy.deepcopy(self.map.snake.pos)
        tail.append(head)

        grid_size = self.map.grid.grid_size

        width, height = self.map.grid.width, self.map.grid.height

        for segment in tail:
            grid_pos = math.floor(segment[0] / grid_size), math.floor(segment[1] / grid_size)

            for y in range(grid_pos[1] - 2, grid_pos[1] + 2):
                for x in range(grid_pos[0] - 2, grid_pos[0] + 2):
                    if (x < 0 or x >= width or y < 0 or y >= height) or isinstance(
                            self.map.grid.layers[1][x][y], float):
                        continue

                    if self.__collision__(segment, (x, y)):
                        return True
        return False

    def set_direction(self, direction):
        self.dir = direction

    def fall(self):
        if self.__check_holding__():
            return False
        
        tail = self.map.snake.tail
        head = self.map.snake.pos
        
        dir = DIRECTIONS[self.dir]

        head[0] += self.fall_speed * dir[0]
        head[1] += self.fall_speed * dir[1]

        for segment in tail:
            segment[0] += self.fall_speed * dir[0]
            segment[1] += self.fall_speed * dir[1]

        return True