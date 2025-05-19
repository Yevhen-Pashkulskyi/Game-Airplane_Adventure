import random

import pygame

from src.main.core.const import *

class Bonus(pygame.sprite.Sprite):
    def __init__(self, img, speed):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(x= random.randint(0, SCREEN_HEIGHT - BONUS_SIZE))
        self.speed = speed
# рух бонусів
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, SCREEN_HEIGHT - BONUS_SIZE)

