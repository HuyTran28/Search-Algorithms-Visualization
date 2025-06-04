class Problem:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def is_goal(self, node):
        return node.get_pos() == self.goal.get_pos()

    def get_neighbors(self, node):
        return self.grid.get_neighbors(node)
