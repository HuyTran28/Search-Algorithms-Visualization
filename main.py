import pygame

pygame.init()

# --- Imports ---
from core.grid import Grid
from core.problem import Problem 

from gui.interface import Interface, Stepper
from gui.renderer import draw_grid
from gui.grid_selector import GridSelector
from gui.search_result_display import SearchResultDisplay

from utils.constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, ROWS, COLS, FONT,
    BG_COLOR, STEPPER_RECT, RESULT_DISPLAY_POS,
    MAZE_BUTTON_RECT, RUN_BUTTON_RECT
)
from utils.action import set_algorithm, regenerate_maze, run_selected, map_window_to_virtual

from algorithms.algorithms_registry import ALGORITHMS

# --- Window Setup ---
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pathfinding Visualization")
virtual_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# --- Object Instantiation ---
grid = Grid(ROWS, COLS)
grid.generate_maze()

problem = Problem(grid)

grid_selector = GridSelector(problem)

stepper = Stepper(
    rect=STEPPER_RECT,
    options=[(name, name) for name in ALGORITHMS.keys()],
    font=FONT,
    on_select=set_algorithm
)

result_display = SearchResultDisplay(font=FONT, pos=RESULT_DISPLAY_POS)

# Interface buttons
interface = Interface()
interface.add_button(MAZE_BUTTON_RECT, "Maze", lambda: regenerate_maze(problem))

def on_run_click():
    """
    Handles the event when the 'Run' button is clicked.

    This function resets the result display and initializes the algorithm generator
    based on the currently selected algorithm and problem. It updates the global
    'algorithm_gen' variable with the generator returned by the selected algorithm.

    Globals:
        algorithm_gen: The generator object for the selected algorithm.

    Side Effects:
        Resets the result display and updates the global algorithm generator.
    """
    global algorithm_gen
    result_display.reset()
    algorithm_gen = run_selected(virtual_surface, problem)()

interface.add_button(RUN_BUTTON_RECT, "Run", on_run_click)

# --- Main Loop ---
algorithm_gen = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (4, 5) or algorithm_gen is not None:
                continue  # Ignore scroll events or clicks while running
            map_pos = map_window_to_virtual(event.pos, window.get_size(), virtual_surface.get_size())
            grid_selector.handle_event(event, map_pos)
            stepper.handle_event(event)
            interface.handle_click(map_pos)

    window.fill(BG_COLOR)
    virtual_surface.fill(BG_COLOR)

    # Advance the algorithm one step per frame if running
    if algorithm_gen is not None:
        try:
            next(algorithm_gen)
        except StopIteration as e:
            algorithm_gen = None  # Algorithm finished
            result_display.update(e.value)
    else:
        draw_grid(virtual_surface, grid, problem.start, problem.goal)
    interface.draw(virtual_surface, FONT)
    stepper.draw(virtual_surface)
    result_display.draw(virtual_surface)

    current_width, current_height = window.get_size()
    scaled_surface = pygame.transform.smoothscale(virtual_surface, (current_width, current_height))
    window.blit(scaled_surface, (0, 0))
    pygame.display.update()
    
pygame.quit()