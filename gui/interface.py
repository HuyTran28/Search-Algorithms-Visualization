import pygame
from utils.constants import COLORS, BUTTON_PARTS

class Interface:
    """
    A class to manage and render interactive buttons in a graphical user interface using pygame.
    Attributes:
        buttons (list): A list of dictionaries, each representing a button with its properties.
        images (dict): A dictionary mapping button part names to their corresponding pygame.Surface images.
    Methods:
        __init__():
            Initializes the Interface, loading button part images and preparing the button list.
        add_button(rect, text, action):
            Adds a new button to the interface.
            Args:
                rect (tuple or pygame.Rect): The position and size of the button.
                text (str): The label to display on the button.
                action (callable): The function to call when the button is clicked.
        handle_click(pos):
            Handles a mouse click event, triggering the action of the button under the given position.
            Args:
                pos (tuple): The (x, y) position of the mouse click.
        draw(window, font):
            Draws all buttons on the given window surface, updating their visual state based on mouse interaction.
            Args:
                window (pygame.Surface): The surface to draw the buttons on.
                font (pygame.font.Font): The font to use for button text.
    """
    def __init__(self):
        self.buttons = []
        self.images = {part: BUTTON_PARTS[part].convert_alpha() for part in BUTTON_PARTS}

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

    def draw(self, window, font):
        mouse_pos = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()

        for button in self.buttons:
            hovered = button["rect"].collidepoint(mouse_pos)
            button["hovered"] = hovered

            # Button press animation (e.g., 150 ms)
            is_pressed = button["pressed"] and current_time - button["press_time"] < 150
            if not is_pressed:
                button["pressed"] = False

            draw_button(
                window,
                button["rect"],
                button["text"],
                font,
                self.images,
                hovered=hovered,
                pressed=is_pressed
            )

class Stepper:
    """
    A UI component for selecting between multiple options using left and right arrow buttons.
    Attributes:
        rect (pygame.Rect): The rectangle defining the position and size of the stepper.
        options (list): A list of tuples representing selectable options. Each tuple should be (display_text, value).
        font (pygame.font.Font): The font used to render the option labels and arrows.
        on_select (callable): A callback function called with the value of the selected option when changed.
        index (int): The current selected option index.
        images (dict): A dictionary of button part images used for rendering.
    Methods:
        handle_event(event):
            Handles pygame events, updating the selected option when the left or right arrow is clicked.
        draw(window):
            Draws the stepper component (arrows and label) onto the given window surface.
        draw_arrow_rect(window, rect, arrow_left, hovered=False, pressed=False):
            Draws an arrow button (left or right) at the specified rectangle, with visual feedback for hover and press states.
    """
    def __init__(self, rect, options, font, on_select):
        self.rect = pygame.Rect(rect)
        self.options = options
        self.font = font
        self.on_select = on_select
        self.index = 0

        self.images = {part: BUTTON_PARTS[part].convert_alpha() for part in BUTTON_PARTS}

        btn_size = rect[3]
        self.left_rect = pygame.Rect(rect[0], rect[1], btn_size, btn_size)
        self.right_rect = pygame.Rect(rect[0] + rect[2] - btn_size, rect[1], btn_size, btn_size)
        self.label_rect = pygame.Rect(
            self.left_rect.right,
            rect[1],
            rect[2] - 2 * btn_size,
            btn_size
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.left_rect.collidepoint(event.pos):
                self.index = (self.index - 1) % len(self.options)
                self.on_select(self.options[self.index][1])
            elif self.right_rect.collidepoint(event.pos):
                self.index = (self.index + 1) % len(self.options)
                self.on_select(self.options[self.index][1])

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        hovered_left = self.left_rect.collidepoint(mouse_pos)
        hovered_right = self.right_rect.collidepoint(mouse_pos)

        self.draw_arrow_rect(window, self.left_rect, arrow_left=True, hovered=hovered_left, pressed=hovered_left and mouse_pressed)
        self.draw_arrow_rect(window, self.right_rect, arrow_left=False, hovered=hovered_right, pressed=hovered_right and mouse_pressed)

        draw_button(
            window,
            self.label_rect,
            text=self.options[self.index][0],
            font=self.font,
            images=self.images,
            hovered=False,
            pressed=False
        )

    def draw_arrow_rect(self, window, rect, arrow_left, hovered=False, pressed=False):
        scale = 0.95 if pressed else 1.0
        size = (int(rect.width * scale), int(rect.height * scale))
        arrow_img = self.images["arrow"]
        arrow_img_scaled = pygame.transform.scale(arrow_img, size)
        arrow_pos = (
            rect.centerx - size[0] // 2,
            rect.centery - size[1] // 2
        )
        window.blit(arrow_img_scaled, arrow_pos)

        if hovered:
            hover_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            hover_surf.fill((40, 40, 40, 60))
            window.blit(hover_surf, rect.topleft)

        symbol = "<" if arrow_left else ">"
        arrow_surf = self.font.render(symbol, True, COLORS["BLACK"])
        arrow_rect = arrow_surf.get_rect(center=rect.center)
        window.blit(arrow_surf, arrow_rect)

def scale_button_parts(images, width, height):
    """Scale left, center, right button parts to fit the given width and height."""
    left_base = images["left"]
    right_base = images["right"]
    center_base = images["center"]

    left_width = max(1, int(left_base.get_width() * height / left_base.get_height()))
    right_width = max(1, int(right_base.get_width() * height / right_base.get_height()))
    total_min_width = left_width + right_width + 1

    if width < total_min_width:
        width = total_min_width

    center_width = width - left_width - right_width

    left_scaled = pygame.transform.scale(left_base, (left_width, height))
    right_scaled = pygame.transform.scale(right_base, (right_width, height))
    center_scaled = pygame.transform.scale(center_base, (center_width, height))

    return left_scaled, center_scaled, right_scaled, width

def draw_button(window, rect, text, font, images, hovered=False, pressed=False):
    """Draw a button with left, center, right images and centered text."""
    scale = 0.95 if pressed else 1.0
    width = int(rect.width * scale)
    height = int(rect.height * scale)
    x = rect.centerx - width // 2
    y = rect.centery - height // 2

    left_scaled, center_scaled, right_scaled, width = scale_button_parts(images, width, height)

    # Apply hover tint
    if hovered:
        tint = (40, 40, 40)
        left_scaled.fill(tint, special_flags=pygame.BLEND_RGB_ADD)
        center_scaled.fill(tint, special_flags=pygame.BLEND_RGB_ADD)
        right_scaled.fill(tint, special_flags=pygame.BLEND_RGB_ADD)

    # Draw button parts
    window.blit(left_scaled, (x, y))
    window.blit(center_scaled, (x + left_scaled.get_width(), y))
    window.blit(right_scaled, (x + left_scaled.get_width() + center_scaled.get_width(), y))

    # Draw centered text with shadow
    text_surface_shadow = font.render(text, True, (40, 0, 0))
    text_surface_main = font.render(text, True, COLORS["WHITE"])
    text_rect = text_surface_main.get_rect(center=(x + width // 2, y + height // 2))
    window.blit(text_surface_shadow, (text_rect.x + 1, text_rect.y + 1))
    window.blit(text_surface_main, text_rect)
