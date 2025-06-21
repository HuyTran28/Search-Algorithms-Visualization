def reconstruct_path(end_node):
    """
    Reconstructs the path from the end node to the start node by following parent links.

    Args:
        end_node: The node at the end of the path, which should have a 'parent' attribute
                  pointing to its predecessor and a 'cost' attribute representing the cost
                  to reach this node from its parent.

    Returns:
        tuple: A tuple containing:
            - path (list): The list of nodes from the start node to the end node.
            - cost (float): The total cost of the reconstructed path.
    """
    path = []
    cost = 0
    current = end_node
    while current.parent:
        path.append(current)
        cost += current.cost
        current = current.parent
    path.reverse()
    return path, cost