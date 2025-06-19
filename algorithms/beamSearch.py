from algorithms.utils import reconstruct_path

def heuristic(node, goal):
    return abs(node.row - goal.row) + abs(node.col - goal.col)  # Manhattan distance

def beam_search(problem, step_callback, beam_width=2):
    start = problem.start
    goal = problem.goal

    start.g = 0
    start.h = heuristic(start, goal)

    frontier = [start]
    explored = set()
    explored_count = 0

    while frontier:
        new_frontier = []

        for current in frontier:
            if current in explored:
                continue

            current.explored = True
            current.in_open = False
            explored.add(current)
            explored_count += 1

            step_callback()
            yield

            if problem.is_goal(current):
                path, cost = reconstruct_path(current)
                for node in path:
                    node.in_path = True
                    node.explored = False
                    step_callback()
                    yield
                goal.in_path = True
                yield (explored_count, cost)
                return

            neighbors = []
            for neighbor in problem.get_neighbors(current):
                if neighbor not in explored and neighbor not in frontier:
                    neighbor.parent = current
                    neighbor.g = current.g + neighbor.cost
                    neighbor.h = heuristic(neighbor, goal)
                    neighbors.append(neighbor)
                    neighbor.in_open = True

            # Keep only top `beam_width` neighbors
            neighbors.sort(key=lambda n: n.h)
            new_frontier.extend(neighbors[:beam_width])

        # Limit the next frontier to the best `beam_width` nodes globally
        new_frontier.sort(key=lambda n: n.h)
        frontier = new_frontier[:beam_width]

        step_callback()
        yield

    yield (explored_count, 0)
