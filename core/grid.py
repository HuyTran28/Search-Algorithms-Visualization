from .node import Node
from random import shuffle
from utils.constants import TILE_WALL, TILE_GRASS

class Grid:
    """
    Represents a 2D grid of nodes for pathfinding and maze generation.
    Attributes:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        grid (list[list[Node]]): 2D list containing Node objects.
    Methods:
        __init__(rows, cols):
            Initializes the grid with the specified number of rows and columns, creating Node objects for each cell.
        reset():
            Resets all nodes in the grid to their initial state, clearing pathfinding and visualization attributes.
        get_node(row, col):
            Returns the Node object at the specified row and column.
        get_neighbors(node):
            Returns a list of neighboring Node objects (up, down, left, right) for the given node.
        generate_maze():
            Generates a random maze using a randomized version of Kruskal's algorithm, modifying node tile types to represent walls and paths.
    """
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
        """
        Generates a random maze within the grid using a randomized version of Kruskal's algorithm.
        The algorithm works as follows:
        1. Fills the entire grid with wall tiles.
        2. Marks every cell at even coordinates as a potential maze cell and initializes a disjoint-set (union-find) structure for them.
        3. Collects all possible walls between adjacent cells (either horizontally or vertically).
        4. Randomly shuffles the list of walls.
        5. Iterates through the shuffled walls, and for each wall, checks if the cells it separates are in different sets.
           - If so, removes the wall and merges the sets, ensuring there is a path between the two cells.
        6. The result is a perfect maze (i.e., a maze with one unique path between any two cells and no cycles).
        This method modifies the grid in-place, setting the appropriate tile types for walls and paths.
        """
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