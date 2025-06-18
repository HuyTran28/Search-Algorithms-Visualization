from algorithms.utils import reconstruct_path

def dls(problem, step_callback, depth_limit):
    start = problem.start
    goal = problem.goal

    start.g = 0
    start.explored = True

    def recursive_dls(node, depth, explored_count):
        if problem.is_goal(node):
            return node, explored_count

        if depth <= 0:
            return None, explored_count
            
        for neighbor in problem.get_neighbors(node):
            if neighbor.explored:
                continue

            neighbor.parent = node
            neighbor.g = node.g + neighbor.cost
            neighbor.explored = True

            step_callback()
            yield

            result, explored_count = yield from recursive_dls(neighbor, depth - 1, explored_count + 1)
            if result is not None:
                return result, explored_count

            neighbor.explored = False
            neighbor.parent = None

            step_callback()
            yield

        return None, explored_count

    result, explored_count = yield from recursive_dls(start, depth_limit, 0)
    if result is not None:
        path, cost = reconstruct_path(result)
        for node in path:
            node.in_path = True
            step_callback()
            yield
        goal.in_path = True
        yield (explored_count, cost)
        return path, explored_count, cost

    yield (explored_count, 0)
    return path, explored_count, 0

def ids(problem, step_callback, max_depth=1000):
    total_explored_count = 1
    for depth in range(max_depth):
        path, explored_count, cost = yield from dls(problem, step_callback, depth)
        total_explored_count += explored_count
        if path is not None:
            yield (total_explored_count, cost)
            return
    yield (total_explored_count, 0)
