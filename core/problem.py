class Problem:
    """
    Represents a search problem on a grid.
    Attributes:
        grid: The grid object representing the search space.
        start: The starting node for the search (default: None).
        goal: The goal node for the search (default: None).
    Methods:
        is_goal(node):
            Checks if the given node is the goal node.
        get_neighbors(node):
            Returns the neighboring nodes of the given node using the grid's method.
    """
    def __init__(self, grid):
        self.grid = grid
        self.start = None
        self.goal = None

    def is_goal(self, node):
        return node.get_pos() == self.goal.get_pos()

    def get_neighbors(self, node):
        return self.grid.get_neighbors(node)
