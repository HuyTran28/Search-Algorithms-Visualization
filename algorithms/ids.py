from algorithms.utils import reconstruct_path

def dls(problem, step_callback, depth_limit):
    start = problem.start
    goal = problem.goal

    start.g = 0
    start.explored = True

    def recursive_dls(node, depth, explored_count):
        if node == goal:
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

            result, explored_count = recursive_dls(neighbor, depth - 1, explored_count + 1)
            if result is not None:
                return result, explored_count

            neighbor.explored = False
            neighbor.parent = None

            step_callback()

        return None, explored_count

    result, explored_count = recursive_dls(start, depth_limit, 0)
    if result is not None:
        path, cost = reconstruct_path(result)
        for node in path:
            node.in_path = True
            step_callback()
        goal.in_path = True
        return path, explored_count, cost

    return None, explored_count, 0

def ids(problem, step_callback, max_depth=1000):
    for depth in range(max_depth):
        result = dls(problem, step_callback, depth)
        if result[0] is not None:
            return result
    return None, 0, 0
