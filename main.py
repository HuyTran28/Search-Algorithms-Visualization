import pygame
from core.grid import Grid
from core.problem import Problem
from gui.renderer import draw_grid
from algorithms.base import search  # unified search

def visual_step():
    draw_grid(win, grid, WIDTH, HEIGHT)

# Grid size and window setup
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
    
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualization")

# Create grid and define start/goal
grid = Grid(ROWS, COLS)
start = grid.get_node(5, 5)
goal = grid.get_node(25, 25)
problem = Problem(grid, start, goal)

# Optional: Add obstacles
for i in range(10, 20):
    grid.get_node(15, i).walkable = False

# Run search and get result with stats
result = search(problem, algorithm="astar", draw_fn=lambda: visual_step())

# Print search statistics
# if result.path:
#     print("✅ Path found!")
# else:
#     print("❌ No path found.")

# print(f"🔍 Nodes explored: {result.explored_count}")
# print(f"💰 Path cost: {result.path_cost}")
# print(f"⏱️ Time taken: {result.time_ms:.2f} ms")
# print(f"🧠 Memory used: {result.memory_kb:.2f} KB")

# Keep window open until closed by user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()