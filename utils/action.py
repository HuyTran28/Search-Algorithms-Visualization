from algorithms.base import search
from gui.renderer import draw_grid

from utils.locks import draw_lock, search_lock

selected_algorithm = {"name": "A*"} 

def set_algorithm(name):
    selected_algorithm["name"] = name

def visual_step(window, problem):
    with draw_lock:
        draw_grid(window, problem.grid, problem.start, problem.goal)

def run_selected(window, problem):
    def run():
        if problem.start is None or problem.goal is None:
            return
        problem.grid.reset()
        return search(problem, algorithm=selected_algorithm["name"], draw_fn=lambda: visual_step(window, problem))
    return run

def regenerate_maze(problem):
    def regenerate():
        if not search_lock.acquire(blocking=False):
            return 
        try:
            problem.grid.reset()
            problem.start = None
            problem.goal = None
            problem.grid.generate_maze()
        finally:
            search_lock.release()
    return regenerate