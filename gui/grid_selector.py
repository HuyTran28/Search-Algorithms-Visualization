from utils.constants import COLORS, FONT, CELL_SIZE, ROWS, COLS 

class GridSelector:
    def __init__(self, grid, problem):
        self.grid = grid
        self.problem = problem

    def handle_event(self, event, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        
        if 0 <= mouse_x < COLS * CELL_SIZE and \
           0 <= mouse_y < ROWS * CELL_SIZE:
            
            clicked_col = mouse_x // CELL_SIZE
            clicked_row = mouse_y // CELL_SIZE
            clicked_node = self.grid.get_node(clicked_row, clicked_col)

            if clicked_node:
                self.problem.grid.reset()
                if event.button == 1:  # Left mouse button
                    self.problem.start = clicked_node
                elif event.button == 3:  # Right mouse button
                    self.problem.goal = clicked_node
                
                return True
        return False