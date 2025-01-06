from src.classes.snake.snake_controller import CONTROLLER
from scipy.spatial import distance


class SNAKE:
    def __init__(self, radius, map, pos):
        self.pos = pos
        self.old_pos = [0, 0]
        self.radius = radius
        self.controller = CONTROLLER(radius, 10)
        self.tail = [[0, 105], [0, 105], [0, 105], [0, 105], [0, 105], [0, 105], [0, 105], [0, 105], [
            0, 105]]  # Для теста хвоста, в идеале, сегменты должны добавляться после съеденного яблока
        self.map = map

    def tail_move(self):
        pos = self.old_pos

        old_x, old_y = pos[0], pos[1]

        i = 0
        while i < len(self.tail):
            cell = self.tail[i]
            cell_x = cell[0]
            cell_y = cell[1]

            if distance.euclidean(cell, [old_x, old_y]) < self.radius * 1.7:
                break

            self.tail[i] = [old_x, old_y]
            old_x, old_y = cell_x, cell_y
            i += 1

    def move(self, speed=None):
        pos = self.controller.snake_move(self.pos[:], speed)

        map_size = self.map.get_size()

        pos[0] = max(self.radius, min(pos[0], map_size[0] - self.radius))
        pos[1] = max(self.radius, min(pos[1], map_size[1] - self.radius))

        # Самая простая реализацию обработки столкновений головы змейки с телом
        for i in range(1, len(self.tail)):
            segment = self.tail[i]

            if distance.euclidean(segment, pos) < self.radius*2-1.5:
                return

        if distance.euclidean(self.old_pos, pos) > self.radius // 2:
            self.old_pos = self.pos[:]

        self.pos = pos
        self.tail_move()
