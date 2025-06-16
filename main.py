import pygame

pygame.init()

from core.grid import Grid
from core.problem import Problem 

from gui.interface import Interface, Dropdown
from gui.renderer import draw_grid
from gui.grid_selector import GridSelector

from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROWS, COLS, FONT
from algorithms.algorithms_registry import ALGORITHMS
from utils.action import set_algorithm, regenerate_maze, run_selected

import threading
draw_lock = threading.Lock()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pathfinding Visualization")

def visual_step():
    with draw_lock:
        draw_grid(window, grid, problem.start, problem.goal)

# Interface setup
interface = Interface()

# Create grid
grid = Grid(ROWS, COLS)
grid.generate_maze()

# Set start and goal
problem = Problem(grid, None, None)

# NEW: Initialize the GridSelector, passing it the grid and problem objects
grid_selector = GridSelector(grid, problem)

# Dropdown setup
dropdown = Dropdown(
    rect=(800, 50, 160, 40),
    options=[(name, name) for name in ALGORITHMS.keys()],
    font=FONT,
    on_select=set_algorithm
)

# Interface buttons
interface = Interface()
interface.add_button((800, 240, 160, 40), (100, 100, 200), "Maze", regenerate_maze(grid))
interface.add_button((800, 120, 160, 40), (100, 200, 100), "Run", run_selected(problem, visual_step))

# Main loop
running = True
while running:
    window.fill((240, 240, 240))

    with draw_lock:
        draw_grid(window, grid, problem.start, problem.goal)
    interface.draw(window, FONT)
    dropdown.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid_selector.handle_event(event, event.pos)
            if event.button == 1:
                dropdown.handle_event(event)
                interface.handle_click(event.pos)
    pygame.display.update()
pygame.quit()