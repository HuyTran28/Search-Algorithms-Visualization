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