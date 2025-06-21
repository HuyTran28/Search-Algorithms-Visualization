import pygame
"""
This module defines constants and assets for the Search Algorithms Visualization application.
Attributes:
    SCREEN_WIDTH (int): Width of the application window in pixels.
    SCREEN_HEIGHT (int): Height of the application window in pixels.
    GRID_SIZE (int): Size of the grid area in pixels.
    ROWS (int): Number of rows in the grid.
    COLS (int): Number of columns in the grid.
    CELL_SIZE (int): Size of each cell in the grid in pixels.
    FONT (pygame.font.Font): Font object used for rendering text.
    COLORS (dict): Dictionary mapping color names to RGBA tuples.
    BG_COLOR (tuple): Background color of the application.
    MARKER_COLOR (dict): Dictionary mapping marker types to color tuples.
    STEPPER_RECT (tuple): Rectangle for the stepper UI component.
    RESULT_DISPLAY_POS (tuple): Position for displaying results.
    MAZE_BUTTON_RECT (tuple): Rectangle for the maze generation button.
    RUN_BUTTON_RECT (tuple): Rectangle for the run button.
    TILE_WALL (str): Identifier for wall tiles.
    TILE_GRASS (str): Identifier for grass tiles.
    TILE_BROKEN_WALL (str): Identifier for broken wall tiles.
    TILE_IMAGES (dict): Dictionary mapping tile types to their loaded and scaled pygame images.
    BUTTON_PARTS (dict): Dictionary mapping button UI parts to their loaded pygame images.
    COST_MAP (dict): Dictionary mapping tile types to their traversal costs.
"""

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
GRID_SIZE = 760
ROWS = 40
COLS = 40
CELL_SIZE = GRID_SIZE // COLS

# Font
FONT = pygame.font.Font("assets/fonts/kenney_pixel.ttf", 40)

# Colors
COLORS = {
    "WHITE": (240, 240, 240, 255),
    "BLACK": (0, 0, 0, 255),
    "GRAY": (150, 150, 150, 255),
    "LIGHT_GRAY": (200, 200, 200, 255),
    "CRIMSON": (220, 20, 60, 90),
    "DODGER_BLUE": (138, 43, 226, 90),
    "LIME_GREEN": (50, 205, 50, 90),
}

BG_COLOR = COLORS["WHITE"]

MARKER_COLOR = {
    "in_path": COLORS["CRIMSON"],
    "explored": COLORS["DODGER_BLUE"],
    "in_open": COLORS["LIME_GREEN"]
}

# UI Layout
STEPPER_RECT = (800, 150, 450, 60)
RESULT_DISPLAY_POS = (900, 450)
MAZE_BUTTON_RECT = (935, 350, 180, 60)
RUN_BUTTON_RECT = (935, 250, 180, 60)

# Tile types
TILE_WALL = "wall"
TILE_GRASS = "grass"
TILE_BROKEN_WALL = "broken-wall"

# Tile images
TILE_IMAGES = {
    TILE_GRASS: pygame.image.load("assets/tiles/grass.png"),
    TILE_WALL: pygame.image.load("assets/tiles/wall.png"),
    "start": pygame.image.load("assets/tiles/start.png"),
    "goal": pygame.image.load("assets/tiles/goal.png"),
    TILE_BROKEN_WALL: pygame.image.load("assets/tiles/broken_wall.png")
}

for key in TILE_IMAGES:
    TILE_IMAGES[key] = pygame.transform.scale(TILE_IMAGES[key], (CELL_SIZE, CELL_SIZE))

# Button UI assets
BUTTON_PARTS = {
    "left": pygame.image.load("assets/ui/button_left.png"),
    "center": pygame.image.load("assets/ui/button_center.png"),
    "right": pygame.image.load("assets/ui/button_right.png"),
    "arrow": pygame.image.load("assets/ui/button_arrow.png")
}

# Tile cost map
COST_MAP = {
    TILE_GRASS: 1,
    TILE_WALL: 10
}