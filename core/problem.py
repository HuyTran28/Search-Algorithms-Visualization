class Problem:
    def __init__(self, grid):
        self.grid = grid
        self.start = None
        self.goal = None

    def is_goal(self, node):
        return node.get_pos() == self.goal.get_pos()

    def get_neighbors(self, node):
        return self.grid.get_neighbors(node)
