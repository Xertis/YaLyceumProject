import math
import random as rand

DIRECTIONS = (1, 2, 3, 4)

class GENERATOR:
    @staticmethod
    def __place__(x, y, dir):
        match dir:
            case 1:
                return x-2, y
            case 2:
                return x+2, y
            case 3:
                return x, y-2
            case 4:
                return x, y+2
    
    @staticmethod
    def __validate__(mat, x, y):
        return x >= 0 and x < len(mat) and y >= 0 and y < len(mat[1]) and mat[x][y] == 0

    @staticmethod
    def generate(seed: int, mat: list[list], visited: list[tuple], obj=1) -> list[list]:
        
        size = len(visited)
        dirs = list(DIRECTIONS)

        for i in range(size):
            cell = visited[i]

            x, y = cell[0], cell[1]
            rand.seed(seed)
            rand.shuffle(dirs)
            
            new_x, new_y = GENERATOR.__place__(x, y, dirs[0])

            if GENERATOR.__validate__(mat, new_x, new_y):
                mat[new_x][new_y] = obj
                mat[math.floor(x + (new_x - x) / 2)][math.floor(y + (new_y - y) / 2)] = obj

                visited.append((new_x, new_y))