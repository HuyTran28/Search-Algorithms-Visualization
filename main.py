import pygame
from core.grid import Grid
from core.problem import Problem
from gui.renderer import draw_grid
from algorithms.base import search  # unified search

def visual_step():
    draw_grid(win, grid, CELL_SIZE)

# Grid size and window setup
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualization")

# Create grid
grid = Grid(ROWS, COLS)

# Set start and goal
start = grid.get_node(5, 5)
goal = grid.get_node(25, 25)
problem = Problem(grid, start, goal)

# Apply terrain map
def set_tile(node, tile_type):
    node.tile_type = tile_type
    node.cost = node.get_cost_from_tile(tile_type)
    node.walkable = tile_type != "wall"

# Sand area
for y in range(10, 20):
    for x in range(10, 15):
        set_tile(grid.get_node(y, x), "sand")

# Water area
for y in range(5, 10):
    for x in range(20, 25):
        set_tile(grid.get_node(y, x), "water")

# Wall
for i in range(0, 10):
    set_tile(grid.get_node(15, i), "wall")

# Set start and goal (override any terrain if needed)
set_tile(start, "grass")
set_tile(goal, "grass")

# Run search
result = search(problem, algorithm="astar", draw_fn=visual_step)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
