import pygame

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
GRID_SIZE = 768
ROWS = 40
COLS = 40
CELL_SIZE = GRID_SIZE // COLS

# Font
FONT = pygame.font.Font("assets/fonts/kenney_pixel.ttf", 40)

# Colors
COLORS = {
    "WHITE": (240, 240, 240),
    "BLACK": (0, 0, 0),
    "GRAY": (150, 150, 150),
    "LIGHT_GRAY": (200, 200, 200),
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
STEPPER_RECT = (800, 50, 450, 60)
RESULT_DISPLAY_POS = (935, 350)
MAZE_BUTTON_RECT = (935, 250, 180, 60)
RUN_BUTTON_RECT = (935, 150, 180, 60)

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