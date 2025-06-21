import pygame.time
from algorithms.algorithms_registry import ALGORITHMS
from core.result import SearchResult
import time, tracemalloc

def search(problem, algorithm="A*", draw_fn=None):
    """
    Executes a search algorithm on the given problem, supporting step-by-step visualization.
    Args:
        problem: The problem instance to solve. Must be compatible with the selected algorithm.
        algorithm (str, optional): The name of the search algorithm to use (e.g., "A*"). Defaults to "A*".
        draw_fn (callable): A function to call for visualization at each step. Required.
    Yields:
        None: Yields control at each step of the algorithm for visualization.
    Returns:
        SearchResult: An object containing the number of explored nodes, the cost of the solution,
                      the elapsed time in milliseconds, and the peak memory usage in kilobytes.
    Raises:
        ValueError: If draw_fn is not provided or if the specified algorithm is unknown.
    """
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

