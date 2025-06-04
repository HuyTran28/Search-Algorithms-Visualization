import pygame.time
from . import astar
from core.result import SearchResult
import time, tracemalloc

def search(problem, algorithm="astar", draw_fn=None):
    if draw_fn is None:
        raise ValueError("draw_fn is required for visualization")
    
    alg_map = {
        "astar": astar.astar,
    }

    algo_fn = alg_map.get(algorithm)
    if not algo_fn:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    def step_callback():
        pygame.time.delay(20)
        draw_fn()

    tracemalloc.start()
    start_time = time.perf_counter()

    path, explored_count, cost = algo_fn(problem, step_callback)

    elapsed = (time.perf_counter() - start_time) * 1000
    mem_kb = tracemalloc.get_traced_memory()[0] / 1024
    tracemalloc.stop()

    return SearchResult(path, explored_count, cost, elapsed, mem_kb)

