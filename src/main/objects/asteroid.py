import random
import pygame
from src.main.core.const import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, img, speed):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(x=SCREEN_WIDTH,
                                        y=random.randrange(0, SCREEN_HEIGHT - ASTEROID_SIZE))
        self.speed = speed

    # відрісовка астероїда за його рухом
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
            self.rect.y = random.randrange(0, SCREEN_HEIGHT - ASTEROID_SIZE)
