from utils.constants import COST_MAP

class Node:
    """
    Represents a node (tile) in a grid for search algorithm visualization.
    Attributes:
        row (int): The row index of the node in the grid.
        col (int): The column index of the node in the grid.
        tile_type (str): The type of tile (e.g., "grass", "water", etc.).
        cost (float): The traversal cost associated with the tile type.
        parent (Node or None): Reference to the parent node in the search path.
        g (float): Cost from the start node to this node.
        h (float): Heuristic cost estimate from this node to the goal.
        f (float): Total cost (g + h).
        explored (bool): Whether the node has been explored (for visualization).
        in_open (bool): Whether the node is in the open set (for visualization).
        in_path (bool): Whether the node is part of the final path (for visualization).
    Methods:
        get_cost_from_tile(tile_type): Returns the traversal cost for a given tile type.
        get_pos(): Returns the (col, row) position tuple of the node.
        __eq__(other): Checks equality based on position.
        __lt__(other): Compares nodes based on total cost f.
        __hash__(): Returns a hash based on the node's position.
    """
    def __init__(self, row, col, tile_type="grass"):
        self.row = row
        self.col = col
        self.tile_type = tile_type
        self.cost = self.get_cost_from_tile(tile_type)

        self.parent = None
        self.g = float('inf')  # cost from start
        self.h = 0             # heuristic
        self.f = float('inf')  # total cost

        # for visualization
        self.explored = False
        self.in_open = False
        self.in_path = False

    @property
    def tile_type(self):
        return self._tile_type

    @tile_type.setter
    def tile_type(self, value):
        self._tile_type = value
        self.cost = self.get_cost_from_tile(value)

    def get_cost_from_tile(self, tile_type):
        return COST_MAP.get(tile_type, 1)

    def get_pos(self):
        return (self.col, self.row)

    def __eq__(self, other):
        return self.get_pos() == other.get_pos()

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.get_pos())
