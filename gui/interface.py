import pygame

from utils.constants import COLORS

class Interface:
    def __init__(self):
        self.buttons = []
        from utils.constants import BUTTON_PARTS
        self.images = { part: BUTTON_PARTS[part].convert_alpha() for part in BUTTON_PARTS }

    def get_button_at(self, pos):
        for button in self.buttons:
            if button["rect"].collidepoint(pos):
                return button["text"]
        return None

    def add_button(self, rect, text, action):
        self.buttons.append({
            "rect": pygame.Rect(rect),
            "text": text,
            "action": action,
            "hovered": False,
            "pressed": False,
            "press_time": 0
        })

    def handle_click(self, pos):
        for button in self.buttons:
            if button["rect"].collidepoint(pos):
                button["pressed"] = True
                button["press_time"] = pygame.time.get_ticks()
                button["action"]()

    def draw(self, win, font):
        mouse_pos = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()

        for button in self.buttons:
            hovered = button["rect"].collidepoint(mouse_pos)
            button["hovered"] = hovered

            # Check if button is still in pressed animation window (e.g., 150 ms)
            is_pressed = button["pressed"] and current_time - button["press_time"] < 150
            if not is_pressed:
                button["pressed"] = False

            self.draw_button(
                win,
                button["rect"],
                button["text"],
                font,
                self.images,
                hovered=hovered,
                pressed=is_pressed
            )

    def draw_button(self, win, rect, text, font, images, hovered=False, pressed=False):
        scale = 0.95 if pressed else 1.0

        # Final size based on rect and press scale
        width = int(rect.width * scale)
        height = int(rect.height * scale)

        x = rect.centerx - width // 2
        y = rect.centery - height // 2

        # Fixed width of left and right 
        left_base = images["left"]
        right_base = images["right"]
        center_base = images["center"]

        # Scale left and right to match rect height
        left_scaled = pygame.transform.scale(left_base, (int(left_base.get_width() * height / left_base.get_height()), height))
        right_scaled = pygame.transform.scale(right_base, (int(right_base.get_width() * height / right_base.get_height()), height))
        
        # Calculate center width
        center_width = width - left_scaled.get_width() - right_scaled.get_width()
        center_scaled = pygame.transform.scale(center_base, (center_width, height))

        # Apply hover tint
        if hovered:
            tint = (40, 40, 40)
            left_scaled.fill(tint, special_flags=pygame.BLEND_RGB_ADD)
            center_scaled.fill(tint, special_flags=pygame.BLEND_RGB_ADD)
            right_scaled.fill(tint, special_flags=pygame.BLEND_RGB_ADD)

        # Draw button parts
        win.blit(left_scaled, (x, y))
        win.blit(center_scaled, (x + left_scaled.get_width(), y))
        win.blit(right_scaled, (x + left_scaled.get_width() + center_scaled.get_width(), y))

        # Draw centered text with shadow
        text_surface_shadow = font.render(text, True, (40, 0, 0))
        text_surface_main = font.render(text, True, COLORS["WHITE"])
        text_rect = text_surface_main.get_rect(center=(x + width // 2, y + height // 2))
        win.blit(text_surface_shadow, (text_rect.x + 1, text_rect.y + 1))
        win.blit(text_surface_main, text_rect)


class Stepper:
    def __init__(self, rect, options, font, on_select, images=None):
        self.rect = pygame.Rect(rect)
        self.options = options
        self.font = font
        self.on_select = on_select
        self.index = 0  # Start with the first option

        if images is None:
            from utils.constants import BUTTON_PARTS
            self.images = {part: BUTTON_PARTS[part].convert_alpha() for part in BUTTON_PARTS}
        else:
            self.images = images

        self.left_rect = pygame.Rect(rect[0], rect[1], rect[3], rect[3])  # Square button left
        self.right_rect = pygame.Rect(rect[0] + rect[2] - rect[3], rect[1], rect[3], rect[3])  # Square button right
        self.label_rect = pygame.Rect(
            self.left_rect.right,
            rect[1],
            rect[2] - 2 * rect[3],
            rect[3]
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.left_rect.collidepoint(event.pos):
                self.index = (self.index - 1) % len(self.options)
                self.on_select(self.options[self.index][1])
                return True
            elif self.right_rect.collidepoint(event.pos):
                self.index = (self.index + 1) % len(self.options)
                self.on_select(self.options[self.index][1])
                return True
        return False

    def draw_button_style(self, win, rect, text=""):
        width = int(rect.width)
        height = int(rect.height)
        x = rect.centerx - width // 2
        y = rect.centery - height // 2

        left_base = self.images["left"]
        right_base = self.images["right"]
        center_base = self.images["center"]

        # --- Step 1: Scale side parts relative to height ---
        left_width = max(1, int(left_base.get_width() * height / left_base.get_height()))
        right_width = max(1, int(right_base.get_width() * height / right_base.get_height()))

        total_min_width = left_width + right_width + 1  # +1 for center width

        if width < total_min_width:
            # Force width to fit minimum safe size
            width = total_min_width
            x = rect.centerx - width // 2

        center_width = width - left_width - right_width

        left_scaled = pygame.transform.scale(left_base, (left_width, height))
        right_scaled = pygame.transform.scale(right_base, (right_width, height))
        center_scaled = pygame.transform.scale(center_base, (center_width, height))

        
        win.blit(left_scaled, (x, y))
        win.blit(center_scaled, (x + left_scaled.get_width(), y))
        win.blit(right_scaled, (x + left_scaled.get_width() + center_scaled.get_width(), y))

        # --- Step 2: Draw arrow or label ---
        text_surface_shadow = self.font.render(text, True, (40, 0, 0))
        text_surface_main = self.font.render(text, True, COLORS["WHITE"])
        text_rect = text_surface_main.get_rect(center=(x + width // 2, y + height // 2))
        win.blit(text_surface_shadow, (text_rect.x + 1, text_rect.y + 1))
        win.blit(text_surface_main, text_rect)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        hovered_left = self.left_rect.collidepoint(mouse_pos)
        hovered_right = self.right_rect.collidepoint(mouse_pos)
       
        # Draw custom arrow buttons
        self.draw_arrow_button(screen, self.left_rect, arrow_left=True, hovered=hovered_left)
        self.draw_arrow_button(screen, self.right_rect, arrow_left=False, hovered=hovered_right)

        # Draw center button-style label
        self.draw_button_style(screen, self.label_rect, text=self.options[self.index][0])


    def draw_arrow_button(self, screen, rect, arrow_left, hovered=False):
        # Draw the arrow background image
        arrow_img = self.images["arrow"]
        arrow_img_scaled = pygame.transform.scale(arrow_img, (rect.width, rect.height))
        screen.blit(arrow_img_scaled, rect.topleft)

        # Optional: apply a hover tint
        if hovered:
            hover_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            hover_surf.fill((40, 40, 40, 60))
            screen.blit(hover_surf, rect.topleft)

        # Draw the arrow symbol
        symbol = "<" if arrow_left else ">"
        arrow_surf = self.font.render(symbol, True, COLORS["BLACK"])
        arrow_rect = arrow_surf.get_rect(center=rect.center)
        screen.blit(arrow_surf, arrow_rect)