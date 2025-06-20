from utils.constants import CELL_SIZE, ROWS, COLS, TILE_WALL


class GridSelector:
    def __init__(self, problem):
        self.problem = problem

    def handle_event(self, event, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        max_x, max_y = COLS * CELL_SIZE, ROWS * CELL_SIZE

        if not (0 <= mouse_x < max_x and 0 <= mouse_y < max_y):
            return

        clicked_col = mouse_x // CELL_SIZE
        clicked_row = mouse_y // CELL_SIZE
        clicked_node = self.problem.grid.get_node(clicked_row, clicked_col)

        if not clicked_node or clicked_node.tile_type == TILE_WALL:
            return

        self.problem.grid.reset()
        if event.button == 1:  # Left mouse button
            self.problem.start = clicked_node
        elif event.button == 3:  # Right mouse button
            self.problem.goal = clicked_node