import pygame

from src.main.core.const import SCREEN_WIDTH, SCREEN_HEIGHT

class Rocket(pygame.sprite.Sprite):
    def __init__(self, img, pos, speed=5):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
