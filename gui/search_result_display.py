from utils.constants import COLORS
import pygame

class SearchResultDisplay:
    """
    A class to display search algorithm results on a graphical interface.
    Attributes:
        font: The font object used to render text.
        pos (tuple): The (x, y) position on the screen where the results are displayed.
        result: The current search result to display.
    Methods:
        __init__(font, pos):
            Initializes the display with a font and position.
        update(result):
            Updates the display with a new search result.
        reset():
            Clears the current search result.
        draw(window):
            Renders the search result information (nodes explored, total cost, time, memory)
            onto the provided window surface, if a result is available.
    """
    def __init__(self, font, pos):
        self.font = font
        self.pos = pos
        self.bg_image = pygame.image.load("assets/ui/search_result_bg.png").convert_alpha()
        self.result = None

    def update(self, result):
        self.result = result

    def reset(self):
        self.result = None

    def draw(self, window):
        if self.result is None:
            return

        # Format time: show in seconds if >= 1000 ms
        if self.result.time_ms >= 1000:
            time_str = f"Time: {self.result.time_ms / 1000:.2f} s"
        else:
            time_str = f"Time: {self.result.time_ms:.2f} ms"

        lines = [
            f"Nodes explored: {self.result.explored_count}",
            f"Total cost: {self.result.path_cost}",
            time_str,
            f"Memory: {self.result.memory_kb:.1f} KB",
        ]

        # Calculate text surfaces
        line_height = self.font.get_height()
        padding_x = 20
        padding_y = 15
        spacing = 5

        text_surfaces = [self.font.render(line, True, COLORS["BLACK"]) for line in lines]
        width = max(ts.get_width() for ts in text_surfaces) + padding_x * 2
        height = len(text_surfaces) * (line_height + spacing) - spacing + padding_y * 2

        frame = self.bg_image
        corner_size = 12  # depends on your frame design

        # Extract the 9 patches
        tl = frame.subsurface((0, 0, corner_size, corner_size))  # top-left
        tr = frame.subsurface((frame.get_width() - corner_size, 0, corner_size, corner_size))  # top-right
        bl = frame.subsurface((0, frame.get_height() - corner_size, corner_size, corner_size))  # bottom-left
        br = frame.subsurface((frame.get_width() - corner_size, frame.get_height() - corner_size, corner_size, corner_size))  # bottom-right

        top = frame.subsurface((corner_size, 0, frame.get_width() - 2 * corner_size, corner_size))
        bottom = frame.subsurface((corner_size, frame.get_height() - corner_size, frame.get_width() - 2 * corner_size, corner_size))
        left = frame.subsurface((0, corner_size, corner_size, frame.get_height() - 2 * corner_size))
        right = frame.subsurface((frame.get_width() - corner_size, corner_size, corner_size, frame.get_height() - 2 * corner_size))

        center = frame.subsurface((corner_size, corner_size, frame.get_width() - 2 * corner_size, frame.get_height() - 2 * corner_size))

        target = pygame.Surface((width, height), pygame.SRCALPHA)

        # Corners
        target.blit(tl, (0, 0))
        target.blit(tr, (width - corner_size, 0))
        target.blit(bl, (0, height - corner_size))
        target.blit(br, (width - corner_size, height - corner_size))

        # Edges
        target.blit(pygame.transform.scale(top, (width - 2 * corner_size, corner_size)), (corner_size, 0))
        target.blit(pygame.transform.scale(bottom, (width - 2 * corner_size, corner_size)), (corner_size, height - corner_size))
        target.blit(pygame.transform.scale(left, (corner_size, height - 2 * corner_size)), (0, corner_size))
        target.blit(pygame.transform.scale(right, (corner_size, height - 2 * corner_size)), (width - corner_size, corner_size))

        # Center
        target.blit(pygame.transform.scale(center, (width - 2 * corner_size, height - 2 * corner_size)), (corner_size, corner_size))

        # Finally blit to screen
        window.blit(target, self.pos)

        # Draw text centered horizontally within the box
        for i, text_surface in enumerate(text_surfaces):
            x = self.pos[0] + (width - text_surface.get_width()) // 2
            y = self.pos[1] + padding_y + i * (line_height + spacing)
            window.blit(text_surface, (x, y))