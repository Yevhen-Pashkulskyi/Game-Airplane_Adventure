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
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = "left"
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = "right"
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = "up"
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = "down"
            self.rect.y += self.speed
        if ((keys[pygame.K_UP] or keys[pygame.K_w])
                and (keys[pygame.K_LEFT] or keys[pygame.K_a])):
            self.direction = "up-left"
            self.rect.y -= self.speed/8
            self.rect.x -= self.speed/8
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s])
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.direction = "down-right"
            self.rect.y += self.speed/8
            self.rect.x += self.speed/8
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s])
                and (keys[pygame.K_LEFT] or keys[pygame.K_a])):
            self.direction = "down-left"
            self.rect.y += self.speed/8
            self.rect.x -= self.speed/8
        if ((keys[pygame.K_UP] or keys[pygame.K_w])
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.direction = "up-right"
            self.rect.x += self.speed/8
            self.rect.y -= self.speed/8


        if self.direction == "up":
            self.image = pygame.transform.rotate(self.original_img, 0)
        if self.direction == "up-left":
            self.image = pygame.transform.rotate(self.original_img, 45)
        if self.direction == "up-right":
            self.image = pygame.transform.rotate(self.original_img, -45)
        if self.direction == "down-left":
            self.image = pygame.transform.rotate(self.original_img, 135)
        if self.direction == "down-right":
            self.image = pygame.transform.rotate(self.original_img, -135)
        if self.direction == "down":
            self.image = pygame.transform.rotate(self.original_img, 180)
        if self.direction == "right":
            self.image = pygame.transform.rotate(self.original_img, -90)
        if self.direction == "left":
            self.image = pygame.transform.rotate(self.original_img, 90)


        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
