from .node import Node
from random import shuffle
from utils.constants import TILE_WALL, TILE_GRASS

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]

    def reset(self):
        for row in self.grid:
            for node in row:
                node.parent = None
                node.g = float("inf")
                node.h = 0
                node.f = float("inf")
                node.explored = False
                node.in_open = False
                node.in_path = False

    def get_node(self, row, col):
        return self.grid[row][col]

    def get_neighbors(self, node):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        neighbors = []
        for dr, dc in directions:
            r, c = node.row + dr, node.col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                neighbors.append(self.grid[r][c])
        return neighbors

    def generate_maze(self):
        # Fill grid with walls
        for row in self.grid:
            for node in row:
                node.tile_type = TILE_WALL

        parent = {}

        def find(pos):
            # Path compression
            while parent[pos] != pos:
                parent[pos] = parent[parent[pos]]
                pos = parent[pos]
            return pos

        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_b] = root_a
                return True
            return False

        walls = []
        # Initialize cells and collect possible walls between cells
        for r in range(0, self.rows, 2):
            for c in range(0, self.cols, 2):
                node = self.grid[r][c]
                node.tile_type = TILE_GRASS
                pos = (r, c)
                parent[pos] = pos
                # Add horizontal and vertical walls between cells
                for dr, dc in [(0, 2), (2, 0)]:
                    nr, nc = r + dr, c + dc
                    if nr < self.rows and nc < self.cols:
                        walls.append(((r, c), (nr, nc)))

        shuffle(walls)

        for (r1, c1), (r2, c2) in walls:
            if union((r1, c1), (r2, c2)):
                # Remove wall between (r1, c1) and (r2, c2)
                wr, wc = (r1 + r2) // 2, (c1 + c2) // 2
                self.grid[wr][wc].tile_type = TILE_GRASS
                self.grid[r2][c2].tile_type = TILE_GRASS