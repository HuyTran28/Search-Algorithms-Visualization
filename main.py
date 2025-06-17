import pygame
from streamlit import button

pygame.init()

from core.grid import Grid
from core.problem import Problem 

from gui.interface import Interface, Stepper
from gui.renderer import draw_grid
from gui.grid_selector import GridSelector
from gui.search_result_display import SearchResultDisplay

from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROWS, COLS, FONT
from utils.action import set_algorithm, regenerate_maze, run_selected
from utils.locks import draw_lock

from algorithms.algorithms_registry import ALGORITHMS

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pathfinding Visualization")

# Create grid
grid = Grid(ROWS, COLS)
grid.generate_maze()

problem = Problem(grid, None, None)

grid_selector = GridSelector(grid, problem)

stepper = Stepper(
    rect=(800, 50, 450, 60),
    options=[(name, name) for name in ALGORITHMS.keys()],
    font=FONT,
    on_select=set_algorithm
)

result_display = SearchResultDisplay(font=FONT, pos=(935, 350))

# Interface buttons
interface = Interface()
interface.add_button((935, 250, 180, 60), "Maze", regenerate_maze(problem))
interface.add_button((935, 150, 180, 60), "Run", run_selected(window, problem))

# Main loop
algorithm_gen = None
running = True

while running:
    window.fill((240, 240, 240))

    # Advance the algorithm one step per frame if running
    if algorithm_gen is not None:
        try:
            next(algorithm_gen)
        except StopIteration as e:
            algorithm_gen = None  # Algorithm finished
            result_display.update(e.value)
    else:
        # Only draw the grid when not running the algorithm
        with draw_lock:
            draw_grid(window, grid, problem.start, problem.goal)
    interface.draw(window, FONT)
    stepper.draw(window)
    result_display.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (4, 5) or algorithm_gen is not None:
                continue  # Ignore scroll events or clicks while running
            with draw_lock:
                grid_selector.handle_event(event, event.pos)
            if event.button == 1:
                stepper_consumed = stepper.handle_event(event)
                if not stepper_consumed:
                    if interface.get_button_at(event.pos) == "Run":
                        result_display.reset()
                        algorithm_gen = run_selected(window, problem)()
                    interface.handle_click(event.pos)
    pygame.display.update()
pygame.quit()