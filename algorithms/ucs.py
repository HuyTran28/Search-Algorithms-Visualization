import heapq
from algorithms.utils import reconstruct_path

def UCS(problem, step_callback):
    start = problem.start
    goal = problem.goal

    frontier = []
    heapq.heappush(frontier, (start.g, start))
    frontier_hash = {start}

    start.g = 0

    explored_count = 0
    while frontier:
        current_g, current = heapq.heappop(frontier)
        frontier_hash.remove(current)

        current.explored = True
        explored_count += 1
        step_callback()

        if problem.is_goal(current):
            path, cost = reconstruct_path(current)
            for node in path:
                node.in_path = True
                step_callback()
            return path, explored_count, cost
        
        for neighbor in problem.get_neighbors(current):
            tentative_g = current.g + neighbor.cost

            if tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.parent = current

                if neighbor not in frontier_hash:
                    heapq.heappush(frontier, (neighbor.g, neighbor))
                    frontier_hash.add(neighbor)
                    neighbor.in_open = True

        step_callback()

    return None, explored_count, 0
