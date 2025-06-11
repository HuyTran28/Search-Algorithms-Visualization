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

class Dropdown:
    def __init__(self, rect, options, font, on_select):
        self.rect = pygame.Rect(rect)
        self.options = options  # list of (label, value)
        self.font = font
        self.on_select = on_select
        self.expanded = False
        self.selected = options[0]  # (label, value)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.expanded = not self.expanded
            elif self.expanded:
                for i, (label, value) in enumerate(self.options):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        self.selected = (label, value)
                        self.on_select(value)
                        self.expanded = False
                        break
                else:
                    self.expanded = False

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        label_surface = self.font.render(self.selected[0], True, (0, 0, 0))
        screen.blit(label_surface, label_surface.get_rect(center=self.rect.center))

        if self.expanded:
            for i, (label, _) in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, (220, 220, 220), option_rect)
                option_surface = self.font.render(label, True, (0, 0, 0))
                screen.blit(option_surface, option_surface.get_rect(center=option_rect.center))