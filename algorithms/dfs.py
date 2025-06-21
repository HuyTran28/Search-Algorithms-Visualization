from algorithms.utils import reconstruct_path

def dfs(problem, step_callback):
    start = problem.start
    goal = problem.goal

    stack = [start]
    explored_count = 0

    start.g = 0
    start.parent = None

    while stack:
        node = stack.pop()
        if node.explored:
            continue

        node.explored = True
        explored_count += 1
        step_callback()
        yield

        if problem.is_goal(node):
            path, cost = reconstruct_path(goal)
            for node in path:
                node.in_path = True
                step_callback()
                yield
            yield (explored_count, cost)
            return

        neighbors = problem.get_neighbors(node)
        for neighbor in reversed(neighbors):
            if not neighbor.explored:
                neighbor.parent = node
                neighbor.g = node.g + neighbor.cost
                stack.append(neighbor)

    yield (explored_count, 0)
