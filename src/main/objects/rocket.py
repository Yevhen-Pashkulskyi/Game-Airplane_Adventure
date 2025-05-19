import math

import pygame

from src.main.core.const import SCREEN_WIDTH, SCREEN_HEIGHT

class Rocket(pygame.sprite.Sprite):
    def __init__(self, img, pos, speed=5):
        super().__init__()
        self.original_img = img
        self.image = img
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.angle = 0

    def update(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        elif keys[pygame.K_RIGHT]:
            dx = self.speed
        elif keys[pygame.K_UP]:
            dy = -self.speed
        elif keys[pygame.K_DOWN]:
            dy = self.speed

        self.rect.x += dx
        self.rect.y += dy

        if dx != 0 or dy != 0:
            self.angle = math.degrees(math.atan2(-dy, dx)) - 90
        # поворот зображення
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # рух в межах екрану
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
