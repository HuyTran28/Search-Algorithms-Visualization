class Node:
    def __init__(self, row, col, walkable=True):
        self.row = row
        self.col = col
        self.walkable = walkable
        self.neighbors = []
        self.parent = None

        self.g = float("inf")
        self.h = 0
        self.f = float("inf")

        # Visualization states
        self.in_open = False
        self.explored = False
        self.in_path = False

    def get_pos(self):
        return self.row, self.col

    def __lt__(self, other):
        return self.f < other.f