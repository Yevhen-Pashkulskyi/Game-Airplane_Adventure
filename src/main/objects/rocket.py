import pygame

from src.main.core.const import SCREEN_WIDTH, SCREEN_HEIGHT

class Rocket(pygame.sprite.Sprite):
    def __init__(self, img, pos, speed=5):
        super().__init__()
        self.original_img = img
        self.image = img
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.direction = "up"

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.direction = "left"
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.rect.x += self.speed
        elif keys[pygame.K_UP]:
            self.direction = "up"
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.direction = "down"
            self.rect.y += self.speed

        if self.direction == "up":
            self.image = pygame.transform.rotate(self.original_img, 0)
        elif self.direction == "right":
            self.image = pygame.transform.rotate(self.original_img, -90)
        elif self.direction == "down":
            self.image = pygame.transform.rotate(self.original_img, 180)
        elif self.direction == "left":
            self.image = pygame.transform.rotate(self.original_img, 90)


        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
