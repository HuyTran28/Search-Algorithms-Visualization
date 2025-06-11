class Node:
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
        cost_map = {
            "grass": 1,
            "wall": 10
        }
        return cost_map.get(tile_type, 1)

    def get_pos(self):
        return (self.col, self.row)

    def __eq__(self, other):
        return self.get_pos() == other.get_pos()

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.get_pos())
