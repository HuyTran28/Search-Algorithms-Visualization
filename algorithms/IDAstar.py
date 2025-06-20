from algorithms.utils import reconstruct_path

def Manhattan_distance(n1, n2):
    return abs(n1.row - n2.row) + abs(n1.col - n2.col)

def DFS_Contour(problem, node, f_limit, step_callback, explored_count):
    explored_count += 1
    if node.f > f_limit:
        return None, node.f, explored_count
    
    if problem.is_goal(node):
        return node, node.f, explored_count
    
    f_next = float('inf')
    for neighbor in problem.get_neighbors(node):
        if neighbor.explored:
            continue
        neighbor.parent = node
        neighbor.g = node.g + neighbor.cost
        neighbor.h = Manhattan_distance(neighbor, problem.goal)
        neighbor.f = neighbor.g + neighbor.h
        neighbor.explored = True

        step_callback()
        yield

        result, f_new, explored_count = yield from DFS_Contour(problem, neighbor, f_limit, step_callback, explored_count)
        if result is not None:
            return result, f_limit, explored_count
        f_next = min(f_next, f_new)

        neighbor.explored = False
        neighbor.parent = None

        step_callback()
        yield

    return None, f_next, explored_count

def IDAstar(problem, step_callback, f_max=100000):
    start = problem.start
    goal = problem.goal

    start.g = 0
    start.h = Manhattan_distance(start, goal)
    start.f = start.g + start.h
    start.explored = True

    f_limit = start.f
    total_explored_count = 1

    while True:
        result, new_limit, explored_count = yield from DFS_Contour(problem, start, f_limit, step_callback, 0)
        total_explored_count += explored_count

        if result is not None:
            path, cost = reconstruct_path(result)
            for node in path:
                node.in_path = True
                step_callback()
                yield
            yield (total_explored_count, cost)
            return
        if new_limit == f_max:
            yield (total_explored_count, 0)
            return
        f_limit = new_limit
        