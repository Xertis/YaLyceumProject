import copy
import numpy as np

class GRID:
    def __init__(self, map):
        self.map = map

        self.grid_size = 38

        self.width = int(self.map.width*1 // self.grid_size + 1)
        self.height = int(self.map.height*1 // self.grid_size + 1)

        grid = np.zeros((self.width, self.height)).tolist()

        self.layers = [
            copy.deepcopy(grid), 
            copy.deepcopy(grid), 
            copy.deepcopy(grid)
        ]

    def set_background(self, sprite):
        for y in range(self.height):
            for x in range(self.width):
                self.layers[0][x][y] = sprite

    def set(self, layer, x, y, sprite):
        self.layers[layer][x][y] = sprite

    def pos_conv(self, pos):
        x, y = pos[0], pos[1]
        step = self.grid_size // 2

        return (x * self.grid_size + step, y * self.grid_size + step)