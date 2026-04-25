import pygame
import sys
import math

pygame.init()

# Window settings
WIDTH, HEIGHT = 1200, 750
TOOLBAR_H = 90
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H))
canvas.fill((255, 255, 255))

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
RED = (220, 60, 60)
GREEN = (60, 180, 90)
BLUE = (70, 120, 220)
YELLOW = (240, 220, 70)
GRAY = (220, 220, 220)

font = pygame.font.SysFont("Arial", 18)

# Current tool settings
tool = "brush"
color = BLACK
drawing = False
start_pos = None
last_pos = None
brush_size = 6

# Color buttons
colors = [BLACK, RED, GREEN, BLUE, YELLOW]
color_rects = [pygame.Rect(20 + i * 50, 20, 35, 35) for i in range(len(colors))]

# Tool buttons
tool_buttons = {
    "brush": pygame.Rect(320, 15, 110, 30),
    "rect": pygame.Rect(440, 15, 110, 30),
    "circle": pygame.Rect(560, 15, 110, 30),
    "eraser": pygame.Rect(680, 15, 110, 30),
    "clear": pygame.Rect(800, 15, 110, 30),
    "square": pygame.Rect(320, 50, 110, 30),
    "rtriangle": pygame.Rect(440, 50, 110, 30),
    "etriangle": pygame.Rect(560, 50, 110, 30),
    "rhombus": pygame.Rect(680, 50, 110, 30),
}


def draw_toolbar():
    # Draw toolbar background
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_H))

    # Draw color selection buttons
    for i, rect in enumerate(color_rects):
        pygame.draw.rect(screen, colors[i], rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Draw tool buttons
    for name, rect in tool_buttons.items():
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text = font.render(name.capitalize(), True, BLACK)
        screen.blit(text, (rect.x + 8, rect.y + 6))

    # Draw current tool name
    info = font.render(f"Tool: {tool}", True, BLACK)
    screen.blit(info, (950, 30))


def draw_line(surface, color, start, end, width):
    pygame.draw.line(surface, color, start, end, width)


def get_rect_data(start_pos, end_pos):
    x1, y1 = start_pos
    x2, y2 = end_pos
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    return x, y, w, h


def draw_square(surface, color, start_pos, end_pos, width=2):
    x, y, w, h = get_rect_data(start_pos, end_pos)
    side = min(w, h)
    pygame.draw.rect(surface, color, (x, y, side, side), width)


def draw_right_triangle(surface, color, start_pos, end_pos, width=2):
    x1, y1 = start_pos
    x2, y2 = end_pos
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surface, color, points, width)


def draw_equilateral_triangle(surface, color, start_pos, end_pos, width=2):
    x1, y1 = start_pos
    x2, y2 = end_pos
    side = abs(x2 - x1)
    if side == 0:
        return

    height = int((math.sqrt(3) / 2) * side)

    if y2 >= y1:
        p1 = (x1, y1 + height)
        p2 = (x1 + side, y1 + height)
        p3 = (x1 + side // 2, y1)
    else:
        p1 = (x1, y1)
        p2 = (x1 + side, y1)
        p3 = (x1 + side // 2, y1 - height)

    pygame.draw.polygon(surface, color, [p1, p2, p3], width)


def draw_rhombus(surface, color, start_pos, end_pos, width=2):
    x, y, w, h = get_rect_data(start_pos, end_pos)
    points = [
        (x + w // 2, y),
        (x + w, y + h // 2),
        (x + w // 2, y + h),
        (x, y + h // 2)
    ]
    pygame.draw.polygon(surface, color, points, width)


while True:
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_H))
    draw_toolbar()

    # Preview for shapes while dragging
    if drawing and tool in ["rect", "circle", "square", "rtriangle", "etriangle", "rhombus"] and start_pos:
        mx, my = pygame.mouse.get_pos()
        end_pos = (mx, my - TOOLBAR_H)

        if tool == "rect":
            x, y, w, h = get_rect_data(start_pos, end_pos)
            pygame.draw.rect(screen, color, (x, y + TOOLBAR_H, w, h), 2)

        elif tool == "circle":
            radius = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
            pygame.draw.circle(screen, color, (start_pos[0], start_pos[1] + TOOLBAR_H), radius, 2)

        elif tool == "square":
            preview = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H), pygame.SRCALPHA)
            draw_square(preview, color, start_pos, end_pos, 2)
            screen.blit(preview, (0, TOOLBAR_H))

        elif tool == "rtriangle":
            preview = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H), pygame.SRCALPHA)
            draw_right_triangle(preview, color, start_pos, end_pos, 2)
            screen.blit(preview, (0, TOOLBAR_H))

        elif tool == "etriangle":
            preview = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H), pygame.SRCALPHA)
            draw_equilateral_triangle(preview, color, start_pos, end_pos, 2)
            screen.blit(preview, (0, TOOLBAR_H))

        elif tool == "rhombus":
            preview = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H), pygame.SRCALPHA)
            draw_rhombus(preview, color, start_pos, end_pos, 2)
            screen.blit(preview, (0, TOOLBAR_H))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            # Click on toolbar
            if my <= TOOLBAR_H:
                for i, rect in enumerate(color_rects):
                    if rect.collidepoint(mx, my):
                        color = colors[i]

                for name, rect in tool_buttons.items():
                    if rect.collidepoint(mx, my):
                        if name == "clear":
                            canvas.fill(WHITE)
                        else:
                            tool = name
            else:
                # Start drawing on canvas
                drawing = True
                start_pos = (mx, my - TOOLBAR_H)
                last_pos = (mx, my - TOOLBAR_H)

                if tool == "brush":
                    pygame.draw.circle(canvas, color, start_pos, brush_size // 2)
                elif tool == "eraser":
                    pygame.draw.circle(canvas, WHITE, start_pos, brush_size)

        if event.type == pygame.MOUSEMOTION and drawing:
            mx, my = event.pos
            if my > TOOLBAR_H:
                current_pos = (mx, my - TOOLBAR_H)

                # Free drawing brush
                if tool == "brush":
                    draw_line(canvas, color, last_pos, current_pos, brush_size)
                    last_pos = current_pos

                # Eraser draws white
                elif tool == "eraser":
                    draw_line(canvas, WHITE, last_pos, current_pos, brush_size * 2)
                    last_pos = current_pos

        if event.type == pygame.MOUSEBUTTONUP and drawing:
            mx, my = event.pos
            if my > TOOLBAR_H:
                end_pos = (mx, my - TOOLBAR_H)

                if tool == "rect":
                    x, y, w, h = get_rect_data(start_pos, end_pos)
                    pygame.draw.rect(canvas, color, (x, y, w, h), 2)

                elif tool == "circle":
                    radius = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.circle(canvas, color, start_pos, radius, 2)

                elif tool == "square":
                    draw_square(canvas, color, start_pos, end_pos, 2)

                elif tool == "rtriangle":
                    draw_right_triangle(canvas, color, start_pos, end_pos, 2)

                elif tool == "etriangle":
                    draw_equilateral_triangle(canvas, color, start_pos, end_pos, 2)

                elif tool == "rhombus":
                    draw_rhombus(canvas, color, start_pos, end_pos, 2)

            drawing = False
            start_pos = None
            last_pos = None

    pygame.display.flip()
    clock.tick(60)