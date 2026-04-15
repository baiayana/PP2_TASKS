import pygame
import time
import os


class MickeysClock:
    """
    Right hand = minutes
    Left hand = seconds
    """

    def __init__(self, screen, center, hand_image_path):
        self.screen = screen
        self.center = center

        try:
            original = pygame.image.load(hand_image_path).convert_alpha()

            # Размер руки
            self.base_hand = pygame.transform.smoothscale(original, (90, 180))

            # Если исходная картинка смотрит не туда, можно сразу повернуть
            # Попробуй 180, если рука вверх ногами
            self.base_hand = pygame.transform.rotate(self.base_hand, 180)

        except FileNotFoundError:
            self.base_hand = self._create_placeholder_hand()

        self.font_large = pygame.font.SysFont("Arial", 64, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 24)

        # Цвета
        self.text_color = (214, 51, 108)       # dark pink
        self.label_color = (186, 85, 211)      # soft purple-pink
        self.center_dot_color = (255, 105, 180)  # hot pink

    def _create_placeholder_hand(self):
        surf = pygame.Surface((40, 140), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 255, 255), (15, 20, 10, 80))
        pygame.draw.circle(surf, (255, 255, 255), (20, 20), 12)
        return surf

    def _get_rotation_angle(self, value, max_value):
        # 0 -> вверх, движение по часовой стрелке
        return -(value / max_value) * 360

    def _draw_rotated_hand(self, image, angle, pivot):
        """
        Вращаем картинку вокруг точки pivot.
        pivot = место, где рука крепится к центру часов.
        """
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=pivot)
        self.screen.blit(rotated, rect)

    def draw(self):
        now = time.localtime()
        minutes = now.tm_min
        seconds = now.tm_sec

        min_angle = self._get_rotation_angle(minutes, 60) 
        sec_angle = self._get_rotation_angle(seconds, 60) 

        # Минутная рука больше
        minute_hand = pygame.transform.smoothscale(self.base_hand, (100, 200))

        # Секундная чуть меньше и зеркальная
        second_hand = pygame.transform.flip(
            pygame.transform.smoothscale(self.base_hand, (80, 170)),
            True,
            False
        )

        # Если после запуска всё ещё смотрит криво, пробуй:
        # min_angle += 180
        # sec_angle += 180

        rotated_min = pygame.transform.rotate(minute_hand, min_angle)
        rect_min = rotated_min.get_rect(center=self.center)
        self.screen.blit(rotated_min, rect_min)

        rotated_sec = pygame.transform.rotate(second_hand, sec_angle)
        rect_sec = rotated_sec.get_rect(center=self.center)
        self.screen.blit(rotated_sec, rect_sec)

        # Центральная точка
        pygame.draw.circle(self.screen, self.center_dot_color, self.center, 7)

        # Цифровое время
        time_str = time.strftime("%M:%S", now)
        text_surf = self.font_large.render(time_str, True, self.text_color)
        text_rect = text_surf.get_rect(center=(self.center[0], self.center[1] - 230))
        self.screen.blit(text_surf, text_rect)

        # Подписи
        label_min = self.font_small.render("Big hand = minutes", True, self.label_color)
        label_sec = self.font_small.render("Small hand = seconds", True, self.label_color)

        self.screen.blit(label_min, label_min.get_rect(center=(self.center[0], self.center[1] + 220)))
        self.screen.blit(label_sec, label_sec.get_rect(center=(self.center[0], self.center[1] + 250)))