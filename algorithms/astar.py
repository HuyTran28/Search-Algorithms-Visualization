import heapq

def heuristic(n1, n2):
    return abs(n1.row - n2.row) + abs(n1.col - n2.col)

def reconstruct_path(end_node):
    path = []
    cost = 0
    current = end_node
    while current.parent:
        path.append(current)
        cost += 1
        current = current.parent
    path.reverse()
    return path, cost

def astar(problem, step_callback):
    start = problem.start
    goal = problem.goal

    open_set = []
    heapq.heappush(open_set, (0, start))
    open_set_hash = {start}

    start.g = 0
    start.f = heuristic(start, goal)

    explored_count = 0

    while open_set:
        current = heapq.heappop(open_set)[1]
        open_set_hash.remove(current)

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
            if not neighbor.walkable:
                continue

            tentative_g = current.g + 1
            if tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (neighbor.f, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.in_open = True
                    step_callback()

    return None, explored_count, 0
