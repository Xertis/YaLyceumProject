import numpy as np

class GRID:
    def __init__(self, map):
        self.map = map

        self.grid_size = 38

        self.width = int(self.map.width*1.5 // self.grid_size)
        self.height = int(self.map.height*1.5 // self.grid_size)

        grid = np.zeros((self.width, self.height)).tolist()

        self.layers = [
            grid[:][:], 
            grid[:][:], 
            grid[:][:]
        ]

    def set_background(self, sprite):
        for y in range(self.height):
            for x in range(self.width):
                self.layers[0][x][y] = sprite

    def set(self, layer, x, y, sprite):
        self.layers[layer][x][y] = sprite