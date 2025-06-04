import pygame

class Interface:
    def __init__(self):
        self.buttons = []

    def add_button(self, rect, color, text, action):
        self.buttons.append({
            "rect": pygame.Rect(rect),
            "color": color,
            "text": text,
            "action": action
        })

    def handle_click(self, pos):
        for button in self.buttons:
            if button["rect"].collidepoint(pos):
                button["action"]()

    def draw(self, win, font):
        for button in self.buttons:
            pygame.draw.rect(win, button["color"], button["rect"])
            text_surface = font.render(button["text"], True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button["rect"].center)
            win.blit(text_surface, text_rect)
