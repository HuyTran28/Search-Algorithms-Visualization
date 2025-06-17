import pygame

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
GRID_SIZE = 768
ROWS = 40
COLS = 40
CELL_SIZE = GRID_SIZE // COLS
FONT = pygame.font.Font("assets/fonts/kenney_pixel.ttf", 40)

COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "GRAY": (150, 150, 150),
    "LIGHT_GRAY": (200, 200, 200),
    "CRIMSON": (220, 20, 60, 120),
    "DARK_ORANGE": (255, 140, 0, 90),
    "LIME_GREEN": (50, 205, 50, 90),
}

MARKER_COLOR = {
    "in_path": COLORS["CRIMSON"],
    "explored": COLORS["DARK_ORANGE"],
    "in_open": COLORS["LIME_GREEN"]
}

# Button settings
BUTTON_WIDTH = 160
BUTTON_HEIGHT = 40
BUTTON_COLOR = {
    "run": (100, 200, 100),
    "clear": (200, 100, 100),
    "maze": (100, 100, 200),
    "dropdown": (180, 180, 255)
}

TILE_IMAGES = {
    "grass": pygame.image.load("assets/tiles/grass.png"),
    "wall": pygame.image.load("assets/tiles/wall.png"),
    "start": pygame.image.load("assets/tiles/start.png"),
    "goal": pygame.image.load("assets/tiles/goal.png"),
    "broken-wall": pygame.image.load("assets/tiles/broken_wall.png")
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
