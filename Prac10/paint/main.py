import pygame
import sys
import math

pygame.init()

# Window settings
WIDTH, HEIGHT = 1000, 700
TOOLBAR_H = 80
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

font = pygame.font.SysFont("Arial", 22)

# Current tool and settings
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
    "brush": pygame.Rect(320, 20, 90, 35),
    "rect": pygame.Rect(420, 20, 90, 35),
    "circle": pygame.Rect(520, 20, 90, 35),
    "eraser": pygame.Rect(620, 20, 90, 35),
    "clear": pygame.Rect(720, 20, 90, 35),
}

def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_H))

    # Draw color buttons
    for i, rect in enumerate(color_rects):
        pygame.draw.rect(screen, colors[i], rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Draw tool buttons
    for name, rect in tool_buttons.items():
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text = font.render(name.capitalize(), True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 6))

    # Current tool text
    info = font.render(f"Tool: {tool}", True, BLACK)
    screen.blit(info, (850, 25))

def draw_line(surface, color, start, end, width):
    pygame.draw.line(surface, color, start, end, width)

while True:
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_H))
    draw_toolbar()

    # Preview for rectangle and circle while dragging
    if drawing and tool in ["rect", "circle"] and start_pos:
        mx, my = pygame.mouse.get_pos()
        preview_x = min(start_pos[0], mx)
        preview_y = min(start_pos[1], my - TOOLBAR_H)
        preview_w = abs(mx - start_pos[0])
        preview_h = abs((my - TOOLBAR_H) - start_pos[1])

        if tool == "rect":
            pygame.draw.rect(
                screen,
                color,
                (preview_x, preview_y + TOOLBAR_H, preview_w, preview_h),
                2
            )
        elif tool == "circle":
            radius = int(math.hypot(mx - start_pos[0], (my - TOOLBAR_H) - start_pos[1]))
            pygame.draw.circle(screen, color, (start_pos[0], start_pos[1] + TOOLBAR_H), radius, 2)

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

            # Click on drawing area
            else:
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

                if tool == "brush":
                    draw_line(canvas, color, last_pos, current_pos, brush_size)
                    last_pos = current_pos
                elif tool == "eraser":
                    draw_line(canvas, WHITE, last_pos, current_pos, brush_size * 2)
                    last_pos = current_pos

        if event.type == pygame.MOUSEBUTTONUP and drawing:
            mx, my = event.pos
            if my > TOOLBAR_H:
                end_pos = (mx, my - TOOLBAR_H)

                if tool == "rect":
                    rect = pygame.Rect(
                        min(start_pos[0], end_pos[0]),
                        min(start_pos[1], end_pos[1]),
                        abs(end_pos[0] - start_pos[0]),
                        abs(end_pos[1] - start_pos[1]),
                    )
                    pygame.draw.rect(canvas, color, rect, 2)

                elif tool == "circle":
                    radius = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.circle(canvas, color, start_pos, radius, 2)

            drawing = False
            start_pos = None
            last_pos = None

    pygame.display.flip()
    clock.tick(60)