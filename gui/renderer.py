import pygame
from utils.constants import COLORS
from utils.constants import TILE_IMAGES, COLORS, MARKER_COLOR, CELL_SIZE


def draw_grid(screen, grid, start_node=None, goal_node=None):
    for row in grid.grid:
        for node in row:
            x = node.col * CELL_SIZE
            y = node.row * CELL_SIZE

            # Draw base terrain color
            if node.tile_type == "wall" and node.in_path:
                tile_img = TILE_IMAGES.get("broken-wall")
            else:
                tile_img = TILE_IMAGES.get(node.tile_type)

            if tile_img:
                screen.blit(tile_img, (x, y))

            if node.in_path:
                overlay = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                overlay.fill(MARKER_COLOR["in_path"])
                screen.blit(overlay, (x, y))
            elif node.explored:
                overlay = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                overlay.fill(MARKER_COLOR["explored"])
                screen.blit(overlay, (x, y))
            elif node.in_open:
                overlay = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                overlay.fill(MARKER_COLOR["in_open"])
                screen.blit(overlay, (x, y))
            
            # Draw start and goal markers
            if start_node is not None and node == start_node:
                tile_img = TILE_IMAGES.get("start")
                if tile_img:
                    screen.blit(tile_img, (x, y))
            if goal_node is not None and node == goal_node:
                tile_img = TILE_IMAGES.get("goal")
                if tile_img:
                    screen.blit(tile_img, (x, y))

            # Draw grid border
            pygame.draw.rect(screen, COLORS["LIGHT_GRAY"], (x, y, CELL_SIZE, CELL_SIZE), 1)