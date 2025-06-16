import pygame
from utils.constants import COLORS
from utils.constants import TILE_IMAGES, COLORS, MARKER_COLOR, CELL_SIZE

for key in TILE_IMAGES:
    TILE_IMAGES[key] = pygame.transform.scale(TILE_IMAGES[key], (CELL_SIZE, CELL_SIZE))

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

            # Draw marker dot or outline in center of cell
            center_x = x + CELL_SIZE // 2
            center_y = y + CELL_SIZE // 2
            radius = CELL_SIZE // 6

            if node.in_path:
                pygame.draw.circle(screen, MARKER_COLOR["in_path"], (center_x, center_y), radius)
            elif node.explored:
                pygame.draw.circle(screen, MARKER_COLOR["explored"], (center_x, center_y), radius)
            elif node.in_open:
                pygame.draw.circle(screen, MARKER_COLOR["in_open"], (center_x, center_y), radius)

            # Draw start and goal nodes on top of everything else for clear visibility
            # Check if start_node/goal_node is not None before comparing
            if start_node is not None and node == start_node:
                tile_img = TILE_IMAGES.get("start")
                if tile_img:
                    screen.blit(tile_img, (x, y))
            if goal_node is not None and node == goal_node:
                tile_img = TILE_IMAGES.get("goal")
                if tile_img:
                    screen.blit(tile_img, (x, y))

            # Draw grid border
            pygame.draw.rect(screen, (200, 200, 200), (x, y, CELL_SIZE, CELL_SIZE), 1)