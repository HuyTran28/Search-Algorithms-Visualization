import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (64, 224, 208)
GREEN = (100, 255, 100)
GRAY = (200, 200, 200)
RED = (255, 100, 100)

def draw_grid(win, grid, width, height):
    win.fill(WHITE)
    rows = grid.rows
    cols = grid.cols
    cell_width = width // cols
    cell_height = height // rows

    for row in grid.grid:
        for node in row:
            color = WHITE  
            if not node.walkable:
                color = BLACK      
            elif node.in_path:
                color = TURQUOISE 
            elif node.explored:
                color = RED 
            elif node.in_open:
                color = GREEN

            pygame.draw.rect(win, color, (node.col * cell_width, node.row * cell_height, cell_width, cell_height))

    # Draw grid lines
    for x in range(0, width, cell_width):
        pygame.draw.line(win, GRAY, (x, 0), (x, height))
    for y in range(0, height, cell_height):
        pygame.draw.line(win, GRAY, (0, y), (width, y))

    pygame.display.update()

