import pygame
import sys
from pygame.locals import *
import random
import os

pygame.init()
pygame.mixer.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Paths
BASE_DIR = os.path.dirname(__file__)
PLAYER_PATH = os.path.join(BASE_DIR, "images", "Player.png")
ENEMY_PATH = os.path.join(BASE_DIR, "images", "Enemy.png")
COIN_PATH = os.path.join(BASE_DIR, "images", "Coin.png")
ROAD_PATH = os.path.join(BASE_DIR, "images", "AnimatedStreet.png")
BG_MUSIC_PATH = os.path.join(BASE_DIR, "sounds", "background.wav")
CRASH_SOUND_PATH = os.path.join(BASE_DIR, "sounds", "crash.wav")

# Load background
background = pygame.image.load(ROAD_PATH).convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Background positions
bg_y1 = 0
bg_y2 = -SCREEN_HEIGHT
bg_speed = 5

# Sounds
pygame.mixer.music.load(BG_MUSIC_PATH)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound(CRASH_SOUND_PATH)
crash_sound.set_volume(0.8)

# Fonts
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 40)
small_font = pygame.font.SysFont("Verdana", 22)

# Game variables
coin_count = 0
game_over = False

# Event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 5000)

# Speeds
enemy_speed = 5
coin_speed = 4


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ENEMY_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, enemy_speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(COIN_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-300, -50)
        )

    def move(self):
        self.rect.move_ip(0, coin_speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PLAYER_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == INC_SPEED and not game_over:
            enemy_speed += 1
            coin_speed += 1
            bg_speed += 1

        # Close window when Enter is pressed after game over
        if game_over and event.type == KEYDOWN:
            if event.key == K_RETURN:
                pygame.quit()
                sys.exit()

    if not game_over:
        P1.update()
        E1.move()
        C1.move()

        # Move scrolling background
        bg_y1 += bg_speed
        bg_y2 += bg_speed

        if bg_y1 >= SCREEN_HEIGHT:
            bg_y1 = -SCREEN_HEIGHT
        if bg_y2 >= SCREEN_HEIGHT:
            bg_y2 = -SCREEN_HEIGHT

        # Collision with enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            game_over = True
            pygame.mixer.music.stop()
            crash_sound.play()

        # Collision with coin
        if pygame.sprite.spritecollideany(P1, coins):
            coin_count += 1
            C1.reset()

    # Draw background
    DISPLAYSURF.blit(background, (0, bg_y1))
    DISPLAYSURF.blit(background, (0, bg_y2))

    # Draw objects
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)

    if not game_over:
        C1.draw(DISPLAYSURF)

    # Draw coin counter
    coin_text = font.render("Coins: " + str(coin_count), True, BLACK)
    DISPLAYSURF.blit(coin_text, (280, 20))

    # Game over text
    if game_over:
        over_text = big_font.render("GAME OVER", True, RED)
        info_text = small_font.render("Press Enter to Exit", True, BLACK)
        DISPLAYSURF.blit(over_text, (75, 220))
        DISPLAYSURF.blit(info_text, (95, 280))

    pygame.display.update()
    FramePerSec.tick(FPS)