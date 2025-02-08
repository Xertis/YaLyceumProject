from src.utils.loader import LOADER
from pygame import Rect
from random import randint as rand


class APPLE:
    def __init__(self, map):
        self.map = map
        self.pos = (0, 0)
        self.sprite = LOADER.sprite.load("apple.png", (38, 38))

    def __count_neighbours__(self, pos):
        width, height = self.map.grid.width, self.map.grid.height
        count = 0

        for y in range(pos[1] - 1, pos[1] + 1):
            for x in range(pos[0] - 1, pos[0] + 1):
                if (x < 0 or x >= width or y < 0 or y >= height) or isinstance(
                        self.map.grid.layers[1][x][y], float):
                    continue

                count += 1

        return count

    def place(self):
            
        while True:
            width, height = self.map.grid.width-1, self.map.grid.height-1
            x, y = rand(0, width), rand(0, height)
            if self.map.grid.layers[1][x][y] == 0.0 and self.__count_neighbours__((x, y)) > 0:
                self.pos = (x, y)
                self.map.grid.set(2, x, y, self.sprite)
                break

    def collision(self):
        snake_pos = self.map.snake.pos
        size = self.map.grid.grid_size
        step = size // 2

        x1, y1 = self.pos[0] * size + step, self.pos[1] * size + step

        snake = Rect(
            snake_pos[0] - self.map.snake.radius,
            snake_pos[1] - self.map.snake.radius,
            self.map.snake.radius,
            self.map.snake.radius
        )

        apple = Rect(
            x1 - size // 2,
            y1 - size // 2,
            size,
            size
        )

        if snake.colliderect(apple):
            return True
        
        return False
    
    def eating(self):
        if_collision = self.collision()

        if if_collision:
            pos = self.pos
            self.map.grid.set(2, pos[0], pos[1], 0.0)
            self.map.snake.tail.append(self.map.snake.tail[-1])
            self.map.snake.score += 1  # Увеличиваем счет
            self.place()
