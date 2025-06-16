from algorithms.utils import reconstruct_path
from collections import deque

def bfs(problem, step_callback):
    start = problem.start
    goal = problem.goal

    frontier = deque([start])
    explored = set()
    explored_count = 0

    start.g = 0

    while frontier:
        current = frontier.popleft()
        explored.add(current)
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
            if neighbor not in explored and neighbor not in frontier:
                neighbor.parent = current
                neighbor.g = current.g + neighbor.cost
                frontier.append(neighbor)
                neighbor.in_open = True

        step_callback()

    return None, explored_count, 0
