import pygame.time
from algorithms.algorithms_registry import ALGORITHMS
from core.result import SearchResult
import time, tracemalloc

def search(problem, algorithm="A*", draw_fn=None):
    if draw_fn is None:
        raise ValueError("draw_fn is required for visualization")

    algo_fn = ALGORITHMS.get(algorithm)
    if not algo_fn:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    def step_callback():
        draw_fn()
        pygame.time.delay(20)

    tracemalloc.start()
    start_time = time.perf_counter()

    # Get the generator from the algorithm
    gen = algo_fn(problem, step_callback)
    explored_count = cost = None
    for result in gen:
        if result is None:
            yield  # Step through the algorithm
            continue
        explored_count, cost = result
        yield

    elapsed = (time.perf_counter() - start_time) * 1000
    mem_kb = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()

    # Return the result at the end
    return SearchResult(explored_count, cost, elapsed, mem_kb)

