import pygame
import random
import sys

pygame.init()

# Window settings
CELL = 20
COLS = 30
ROWS = 20
WIDTH = COLS * CELL
HEIGHT = ROWS * CELL

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Colors
BLACK = (20, 20, 20)
GREEN = (50, 180, 90)
DARK_GREEN = (30, 120, 60)
RED = (220, 60, 60)
WHITE = (240, 240, 240)

font = pygame.font.SysFont("Arial", 26)

# Snake settings
snake = [(5, 10), (4, 10), (3, 10)]
direction = (1, 0)
next_direction = (1, 0)

score = 0
level = 1
speed = 8
game_over = False


def random_food():
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos


food = random_food()


def draw_cell(position, color):
    x, y = position
    pygame.draw.rect(screen, color, (x * CELL, y * CELL, CELL, CELL))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Close game when Enter is pressed after game over
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()
                sys.exit()

        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                next_direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                next_direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                next_direction = (1, 0)

    if not game_over:
        direction = next_direction

        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Border collision
        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            game_over = True

        # Self collision
        elif new_head in snake:
            game_over = True

        else:
            snake.insert(0, new_head)

            # Food collision
            if new_head == food:
                score += 1
                level = score // 4 + 1
                speed = 8 + (level - 1) * 2
                food = random_food()
            else:
                snake.pop()

    screen.fill(BLACK)

    # Draw snake
    for i, part in enumerate(snake):
        if i == 0:
            draw_cell(part, GREEN)
        else:
            draw_cell(part, DARK_GREEN)

    # Draw food
    draw_cell(food, RED)

    # Draw score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Game over text
    if game_over:
        over_text = font.render("GAME OVER", True, WHITE)
        info_text = font.render("Press Enter to Exit", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - 90, HEIGHT // 2 - 30))
        screen.blit(info_text, (WIDTH // 2 - 120, HEIGHT // 2 + 10))

    pygame.display.update()
    clock.tick(speed)