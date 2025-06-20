from algorithms.base import search
from gui.renderer import draw_grid

selected_algorithm = {"name": "A*"} 

def set_algorithm(name):
    selected_algorithm["name"] = name

def visual_step(window, problem):
    draw_grid(window, problem.grid, problem.start, problem.goal)

def run_selected(window, problem):
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
    wx, wy = window_size
    vx, vy = virtual_size
    x = int(pos[0] * vx / wx)
    y = int(pos[1] * vy / wy)
    return (x, y)