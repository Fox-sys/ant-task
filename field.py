import numpy as np


class Field:
    def __init__(self, size):
        self.size = size
        self._field = np.ones((size, size), dtype=np.uint8)

    def get_color(self, x, y):
        return self._field[x, y]

    def change_color(self, x, y):
        self._field[x, y] = int(not self._field[x, y])

    def get_field(self):
        return self._field
