import math
import random as rand

DIRECTIONS = (1, 2, 3, 4)


class GENERATOR:
    @staticmethod
    def __place__(x, y, dir):
        match dir:
            case 1:
                return x - 2, y
            case 2:
                return x + 2, y
            case 3:
                return x, y - 2
            case 4:
                return x, y + 2

    @staticmethod
    def __validate__(mat, x, y):
        return x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and mat[x][y] == 0

    @staticmethod
    def generate(
            seed: int,
            mat: list[list],
            visited: list[tuple],
            obj=1) -> list[list]:

        rand.seed(seed)
        dirs = list(DIRECTIONS)

        x, y = visited[0]
        mat[x][y] = obj

        max_steps_in_direction = 2
        current_direction = None
        steps_in_current_direction = 0

        while True:
            rand.shuffle(dirs)

            new_direction = None
            for dir in dirs:
                if dir != current_direction:
                    new_x, new_y = GENERATOR.__place__(x, y, dir)
                    if GENERATOR.__validate__(mat, new_x, new_y):
                        new_direction = dir
                        break

            if new_direction is None:
                break

            if new_direction != current_direction:
                steps_in_current_direction = 0
                current_direction = new_direction

            new_x, new_y = GENERATOR.__place__(x, y, current_direction)
            mat[new_x][new_y] = obj
            mat[math.floor(x + (new_x - x) / 2)][math.floor(y + (new_y - y) / 2)] = obj
            visited.append((new_x, new_y))

            x, y = new_x, new_y

            steps_in_current_direction += 1

            if steps_in_current_direction >= max_steps_in_direction:
                current_direction = None

        return mat