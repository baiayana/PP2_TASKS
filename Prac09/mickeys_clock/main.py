import pygame
import sys
import os
import math
from clock import MickeysClock

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
FPS = 1

# Цвета
BG_COLOR = (255, 240, 245)        # very light pink
RING_COLOR = (214, 51, 108)       # dark pink
INNER_COLOR = (255, 250, 252)     # almost white pink
HOUR_TICK_COLOR = (199, 21, 133)  # deep pink
MINUTE_TICK_COLOR = (255, 182, 193)  # light pink
TITLE_COLOR = (199, 21, 133)      # deep pink
HINT_COLOR = (186, 85, 211)       # soft purple-pink

HAND_IMAGE_PATH = os.path.join("images", "mickey_hand.png")


def draw_clock_face(screen, center, radius=180):
    pygame.draw.circle(screen, RING_COLOR, center, radius, 6)
    pygame.draw.circle(screen, INNER_COLOR, center, radius - 6)

    for i in range(60):
        angle_rad = math.radians(i * 60 - 90)

        if i % 5 == 0:
            inner = radius - 24
            outer = radius - 8
            color = HOUR_TICK_COLOR
            width = 3
        else:
            inner = radius - 14
            outer = radius - 8
            color = MINUTE_TICK_COLOR
            width = 1

        x1 = center[0] + inner * math.cos(angle_rad)
        y1 = center[1] + inner * math.sin(angle_rad)
        x2 = center[0] + outer * math.cos(angle_rad)
        y2 = center[1] + outer * math.sin(angle_rad)

        pygame.draw.line(screen, color, (int(x1), int(y1)), (int(x2), int(y2)), width)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock_tick = pygame.time.Clock()

    center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    mickey_clock = MickeysClock(screen, center, HAND_IMAGE_PATH)

    title_font = pygame.font.SysFont("Arial", 36, bold=True)
    hint_font = pygame.font.SysFont("Arial", 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

        screen.fill(BG_COLOR)

        title = title_font.render("Mickey's Clock", True, TITLE_COLOR)
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 40)))

        draw_clock_face(screen, center)

        mickey_clock.draw()

        hint = hint_font.render("Press Q to quit", True, HINT_COLOR)
        screen.blit(hint, (10, SCREEN_HEIGHT - 30))

        pygame.display.flip()
        clock_tick.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()