from .node import Node

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]

    def reset(self):
        for row in self.grid:
            for node in row:
                node.walkable = True
                node.parent = None
                node.g = float("inf")
                node.h = 0
                node.f = float("inf")

    def get_node(self, row, col):
        return self.grid[row][col]

    def get_neighbors(self, node):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-way movement
        for dr, dc in directions:
            r, c = node.row + dr, node.col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                neighbor = self.grid[r][c]
                if neighbor.walkable:
                    neighbors.append(neighbor)
        return neighbors
