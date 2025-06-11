import pygame
from utils.constants import COLORS

COLOR_MAP = {
    "grass": (255, 255, 255),
    "sand": (255, 255, 100),
    "water": (100, 100, 255),
    "wall": (0, 0, 0)
}

MARKER_COLOR = {
    "in_path": (255, 50, 50),     # red dot
    "explored": (255, 165, 0),    # orange dot
    "in_open": (160, 32, 240)     # purple dot
}

def draw_grid(screen, grid, cell_size, start_node=None, goal_node=None):
    for row in grid.grid:
        for node in row:
            x = node.col * cell_size
            y = node.row * cell_size

            # Draw base terrain color
            base_color = COLOR_MAP.get(node.tile_type, (255, 255, 255))
            pygame.draw.rect(screen, base_color, (x, y, cell_size, cell_size))

            # Draw marker dot or outline in center of cell
            center_x = x + cell_size // 2
            center_y = y + cell_size // 2
            radius = cell_size // 6

            if node.in_path:
                pygame.draw.circle(screen, MARKER_COLOR["in_path"], (center_x, center_y), radius)
            elif node.explored:
                pygame.draw.circle(screen, MARKER_COLOR["explored"], (center_x, center_y), radius)
            elif node.in_open:
                pygame.draw.circle(screen, MARKER_COLOR["in_open"], (center_x, center_y), radius)

            # Draw start and goal nodes on top of everything else for clear visibility
            # Check if start_node/goal_node is not None before comparing
            if start_node is not None and node == start_node:
                pygame.draw.rect(screen, COLORS["START_NODE"], (x, y, cell_size, cell_size)) # Green for start node
            if goal_node is not None and node == goal_node:
                pygame.draw.rect(screen, COLORS["GOAL_NODE"], (x, y, cell_size, cell_size)) # Red for goal node

            # Draw grid border
            pygame.draw.rect(screen, (200, 200, 200), (x, y, cell_size, cell_size), 1)