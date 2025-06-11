from utils.constants import COLORS, FONT, CELL_SIZE, ROWS, COLS 

class GridSelector:
    def __init__(self, grid, problem):
        self.grid = grid
        self.problem = problem

    def handle_event(self, event, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        
        # Check if the click is within the grid area (left side of the screen)
        # Note: We use COLS * CELL_SIZE for the grid width, as defined in constants.
        if 0 <= mouse_x < COLS * CELL_SIZE and \
           0 <= mouse_y < ROWS * CELL_SIZE:
            
            clicked_col = mouse_x // CELL_SIZE
            clicked_row = mouse_y // CELL_SIZE
            clicked_node = self.grid.get_node(clicked_row, clicked_col)

            if clicked_node: # Ensure a valid node was clicked (e.g., not out of bounds if constants changed)
                if event.button == 1: # Left mouse button
                    self.problem.start = clicked_node
                elif event.button == 3: # Right mouse button
                    self.problem.goal = clicked_node
                
                return True
        return False