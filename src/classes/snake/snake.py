from src.classes.snake.snake_controller import CONTROLLER
from scipy.spatial import distance
from src.classes.snake.snake_gravitation import GRAVITATION


class SNAKE:
    def __init__(self, radius, map, pos, start_window):
        self.pos = pos
        self.old_pos = [0, 0]
        self.radius = radius
        self.controller = CONTROLLER(map, radius, 10, start_window)
        self.gravitation = GRAVITATION(self.controller)
        self.tail = [
            [0, 0],
            [0, 0],
            [0, 0]
        ]
        self.map = map

    def tail_move(self):
        pos = self.old_pos

        old_x, old_y = pos[0], pos[1]
        interpolation_factor = 0.15

        i = 0

        while i < len(self.tail):
            cell = self.tail[i]
            cell_x = cell[0]
            cell_y = cell[1]

            dist = distance.euclidean(cell, [old_x, old_y])

            if dist < self.radius * 1.75:
                break

            new_x = cell_x + (old_x - cell_x) * interpolation_factor
            new_y = cell_y + (old_y - cell_y) * interpolation_factor

            self.tail[i] = [new_x, new_y]

            old_x, old_y = cell_x, cell_y
            i += 1

    def move(self, speed=None):
        pos = self.controller.snake_move(self.pos[:], speed)

        map_size = self.map.get_size()

        pos[0] = max(self.radius, min(pos[0], map_size[0] - self.radius))
        pos[1] = max(self.radius, min(pos[1], map_size[1] - self.radius))

        if distance.euclidean(self.old_pos, pos) > self.radius // 2:
            self.old_pos = self.pos[:]

        self.pos = pos
        self.tail_move()
        self.gravitation.fall()
