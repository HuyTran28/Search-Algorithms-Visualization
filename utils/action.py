from algorithms.base import search
from gui.renderer import draw_grid

selected_algorithm = {"name": "A*"} 

def set_algorithm(name):
    selected_algorithm["name"] = name

def visual_step(window, problem):
    draw_grid(window, problem.grid, problem.start, problem.goal)

def run_selected(window, problem):
    """
    Creates a function that runs the selected search algorithm on the given problem and visualizes each step.

    Args:
        window: The window or surface object used for visualization.
        problem: An object representing the search problem, which must have 'start', 'goal', and 'grid' attributes.

    Returns:
        function: A function that, when called, resets the problem's grid and runs the selected search algorithm,
        visualizing each step using the provided window. If the problem's start or goal is not set, the function returns None.
    """
    def run():
        if problem.start is None or problem.goal is None:
            return
        problem.grid.reset()
        return search(
            problem,
            algorithm=selected_algorithm["name"],
            draw_fn=lambda: visual_step(window, problem)
        )
    return run

def regenerate_maze(problem):
    def regenerate():
        problem.grid.reset()
        problem.start = None
        problem.goal = None
        problem.grid.generate_maze()
    return regenerate

def map_window_to_virtual(pos, window_size, virtual_size):
    """
    Maps a position from window coordinates to virtual surface coordinates.

    Args:
        pos (tuple): The (x, y) position in window coordinates.
        window_size (tuple): The (width, height) of the window.
        virtual_size (tuple): The (width, height) of the virtual surface.

    Returns:
        tuple: The (x, y) position mapped to virtual surface coordinates.
    """
    wx, wy = window_size
    vx, vy = virtual_size
    x = int(pos[0] * vx / wx)
    y = int(pos[1] * vy / wy)
    return (x, y)