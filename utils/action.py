import threading
from algorithms.base import search

selected_algorithm = {"name": "astar"} 

def set_algorithm(name):
    def _set():
        selected_algorithm["name"] = name
        print(f"Selected algorithm: {name}")
    return _set

def run_selected(problem, draw_fn):
    problem.grid
    def run():
        search(problem, algorithm=selected_algorithm["name"], draw_fn=draw_fn)
    return lambda: threading.Thread(target=run).start()

def regenerate_maze(grid):
    return lambda: grid.generate_maze()