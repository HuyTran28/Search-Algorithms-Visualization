from algorithms.utils import reconstruct_path

def dfs(problem, step_callback):
    start = problem.start
    goal = problem.goal
    explored_count = [0]  # Use list to allow modification in nested scope
    path_found = [False]  # Flag to stop recursion when goal is found

    def df(node):
        if path_found[0]:
            return

        node.explored = True
        explored_count[0] += 1
        step_callback()
        yield

        if problem.is_goal(node):
            path_found[0] = True
            return

        for neighbor in problem.get_neighbors(node):
            if not neighbor.explored and not path_found[0]:
                neighbor.parent = node
                neighbor.g = node.g + neighbor.cost
                yield from df(neighbor)

        # Backtrack (only clear highlight if not part of final path)
        if not path_found[0]:
            node.explored = False
            step_callback()
            yield

    start.g = 0
    yield from df(start)

    if path_found[0]:
        path, cost = reconstruct_path(goal)
        for node in path:
            node.in_path = True
            step_callback()
            yield
        yield (explored_count[0], cost)
        return

    yield (None, explored_count[0], 0)
    
