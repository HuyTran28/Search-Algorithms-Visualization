import threading
from algorithms.base import search

selected_algorithm = {"name": "A*"} 
search_lock = threading.Lock() 

def set_algorithm(name):
    selected_algorithm["name"] = name

def run_selected(problem, draw_fn):
    def run():
        if not search_lock.acquire(blocking=False):
            return  # Another search is running
        try:
            problem.grid.reset()
            search(problem, algorithm=selected_algorithm["name"], draw_fn=draw_fn)
        finally:
            search_lock.release()
    return lambda: threading.Thread(target=run).start()

def regenerate_maze(problem):
    def regenerate():
        if not search_lock.acquire(blocking=False):
            return  # Another search is running
        try:
            problem.grid.reset()
            problem.start = None
            problem.goal = None
            problem.grid.generate_maze()
        finally:
            search_lock.release()
    return regenerate