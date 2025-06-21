import pygame
from utils.constants import TILE_IMAGES, COLORS, MARKER_COLOR, CELL_SIZE, TILE_GRASS, TILE_WALL, TILE_BROKEN_WALL

def draw_grid(window, grid, start_node=None, goal_node=None):
    """
    Draws the grid and overlays onto the given Pygame window surface.
    Args:
        window (pygame.Surface): The Pygame surface to draw the grid on.
        grid (Grid): The grid object containing nodes to be rendered.
        start_node (Node, optional): The node representing the start position. Defaults to None.
        goal_node (Node, optional): The node representing the goal position. Defaults to None.
    Details:
        - Renders each node's base tile image according to its type.
        - Overlays visual markers for nodes that are in the path, explored, or in the open set.
        - Draws special markers for the start and goal nodes if provided.
        - Draws a light gray border around each cell for grid visibility.
    """
    overlay_cache = {}

    def get_overlay(color_key):
        if color_key not in overlay_cache:
            surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            surf.fill(MARKER_COLOR[color_key])
            overlay_cache[color_key] = surf
        return overlay_cache[color_key]

    for row in grid.grid:
        for node in row:
            x, y = node.col * CELL_SIZE, node.row * CELL_SIZE

            # Draw base tile
            tile_key = TILE_BROKEN_WALL if node.tile_type == TILE_WALL and node.in_path else node.tile_type
            tile_img = TILE_IMAGES.get(tile_key)
            if tile_img:
                window.blit(tile_img, (x, y))

            # Draw overlays for path, explored, open
            if node.in_path:
                window.blit(get_overlay("in_path"), (x, y))
            elif node.explored:
                window.blit(get_overlay("explored"), (x, y))
            elif node.in_open:
                window.blit(get_overlay("in_open"), (x, y))

            # Draw start and goal markers
            if start_node is not None and node == start_node:
                start_img = TILE_IMAGES.get("start")
                if start_img:
                    window.blit(start_img, (x, y))
            if goal_node is not None and node == goal_node:
                goal_img = TILE_IMAGES.get("goal")
                if goal_img:
                    window.blit(goal_img, (x, y))

            # Draw grid border
            pygame.draw.rect(window, COLORS["LIGHT_GRAY"], (x, y, CELL_SIZE, CELL_SIZE), 1)