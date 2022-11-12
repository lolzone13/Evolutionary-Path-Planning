# DDDDDRRUUR
import random

class Path_Map:
    def __init__(self, rows=10, cols=10):
        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 8, 8, 0, ],
            [0, 4, 4, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 4, 0, 4, 0, 0, 0, 1, 1, 0, ],
            [0, 0, 0, 6, 6, 0, 0, 3, 3, 0, ],
            [0, 4, 0, 6, 6, 0, 0, 5, 5, 0, ],
            [0, 2, 3, 4, 4, 0, 0, 7, 7, 0, ],
            [0, 4, 7, 2, 2, 6, 0, 8, 8, 0, ],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, ],
            [0, 0, 4, 4, 4, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, ],
        ]

        self.start = [4, 4]
        self.end = [3, 8]
        self.min_path_length = abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1])
        self.rows = rows
        self.columns = cols
        self.max_path_length = rows * cols
    def generate_map(self):
        return self.map
    

    def create_map(self):
        self.map = []
        for i in range(self.rows):
            l = []
            for j in range(self.cols):
                l.append(random.randint(0,10))
            self.map.append(l)
        return self.map