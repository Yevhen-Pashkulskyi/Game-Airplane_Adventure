from math import sqrt

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
        diagonal_speed = self.speed // 4
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
            self.rect.y -= diagonal_speed
            self.rect.x -= diagonal_speed
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s])
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.direction = "down-right"
            self.rect.y += diagonal_speed
            self.rect.x += diagonal_speed
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s])
                and (keys[pygame.K_LEFT] or keys[pygame.K_a])):
            self.direction = "down-left"
            self.rect.y += diagonal_speed
            self.rect.x -= diagonal_speed
        if ((keys[pygame.K_UP] or keys[pygame.K_w])
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.direction = "up-right"
            self.rect.x += diagonal_speed
            self.rect.y -= diagonal_speed

        angle_map ={
            "up":0,
            "up-left":45,
            "up-right":-45,
            "down-left":135,
            "down-right":-135,
            "down":180,
            "right":-90,
            "left":90
        }
        self.image = pygame.transform.rotate(self.original_img, angle_map[self.direction])

        self.rect = self.image.get_rect(center=self.rect.center)
        # предели єкрана
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
