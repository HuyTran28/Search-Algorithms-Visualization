import heapq
from algorithms.utils import reconstruct_path

def Manhattan_distance(n1, n2):
    return abs(n1.row - n2.row) + abs(n1.col - n2.col)

def astar(problem, step_callback):
    start = problem.start
    goal = problem.goal

    frontier = []
    heapq.heappush(frontier, (0, start))
    frontier_hash = {start}

    start.g = 0
    start.f = Manhattan_distance(start, goal)

    explored_count = 0

    while frontier:
        current = heapq.heappop(frontier)[1]
        frontier_hash.remove(current)

        current.explored = True
        explored_count += 1

        step_callback()

        if problem.is_goal(current):
            path, cost = reconstruct_path(current)
            for node in path:
                node.in_path = True
                step_callback()
            goal.in_path = True
            return path, explored_count, cost

        for neighbor in problem.get_neighbors(current):
            tentative_g = current.g + neighbor.cost
            if tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = Manhattan_distance(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in frontier_hash:
                    heapq.heappush(frontier, (neighbor.f, neighbor))
                    frontier_hash.add(neighbor)
                    neighbor.in_open = True
        step_callback()

    return None, explored_count, 0
