import pygame

class SearchResultDisplay:
    def __init__(self, font, pos=(935, 350)):
        self.font = font
        self.pos = pos
        self.result = None

    def update(self, result):
        self.result = result

    def reset(self):
        self.result = None

    def draw(self, screen):
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
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, (0, 0, 0))
            screen.blit(text_surface, (self.pos[0], self.pos[1] + i * 30))