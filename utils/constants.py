import pygame

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 600
ROWS = 40
COLS = 40
CELL_SIZE = GRID_SIZE // COLS
FONT = pygame.font.SysFont(None, 24)

# Colors
# Define a dictionary of colors for easier management
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "GRAY": (150, 150, 150),
    "VISITED": (173, 216, 230),  # Light Blue for visited nodes
    "PATH": (255, 255, 0),       # Yellow for path nodes
    "START_NODE": (0, 200, 0),   # Green for the start node
    "GOAL_NODE": (200, 0, 0)     # Red for the goal node
}

MARKER_COLOR = {
    "in_path": (255, 50, 50),     # red
    "explored": (255, 165, 0),    # orange
    "in_open": (160, 32, 240)     # purple
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