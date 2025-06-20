from collections import deque
from algorithms.utils import reconstruct_path

def bidirectional_search(problem, step_callback):
    start = problem.start
    goal = problem.goal

    if start == goal:
        yield (2, 0)
        return 
    
    frontier_start = deque([start])
    frontier_goal = deque([goal])

    visited_start = {start: None}
    visited_goal = {goal: None}

    start.g = 0
    goal.g = 0

    explored_count = 0
    meeting_node = None

    while frontier_start and frontier_goal:

        current_s = frontier_start.popleft()
        current_s.explored = True
        current_s.in_open = False
        explored_count += 1
        step_callback()
        yield

        for neighbor in problem.get_neighbors(current_s):
            if neighbor not in visited_start:
                visited_start[neighbor] = current_s
                neighbor.g = current_s.g + neighbor.cost
                frontier_start.append(neighbor)
                neighbor.in_open = True 

                if neighbor in visited_goal:
                    meeting_node = neighbor
                    neighbor.explored = True
                    explored_count += 1
                    step_callback()
                    yield
                    break

        if meeting_node:
            break

        current_g = frontier_goal.popleft()
        current_g.explored = True
        current_g.in_open = False
        explored_count += 1
        step_callback()
        yield

        for neighbor in problem.get_neighbors(current_g):
            if neighbor not in visited_goal:
                visited_goal[neighbor] = current_g
                neighbor.g = current_g.g + neighbor.cost
                frontier_goal.append(neighbor)
                neighbor.in_open = True 

                if neighbor in visited_start:
                    meeting_node = neighbor
                    neighbor.explored = True
                    explored_count += 1
                    step_callback()
                    yield
                    break

        if meeting_node:
            break

    if meeting_node:
        path_start = []
        n = meeting_node
        while n:
            path_start.append(n)
            n = visited_start[n]
        path_start.reverse()

        path_goal = []
        n = visited_goal[meeting_node]
        while n:
            path_goal.append(n)
            n = visited_goal[n]

        path = path_start + path_goal
        cost = sum(node.cost for node in path)

        for node in path:
            node.in_path = True
            step_callback()
            yield

        yield (explored_count, cost)
        return

    yield (explored_count, 0)
