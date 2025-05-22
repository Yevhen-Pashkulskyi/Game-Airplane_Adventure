import os.path
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

        snd_path = os.path.join(os.path.dirname(__file__),
                                "..", "assets", "snd", "big-motor-90117.wav")
        self.motorcycle_sound = pygame.mixer.Sound(snd_path)
        self.motorcycle_sound.set_volume(0.05)
        self.moving = False

    def reset_position(self):
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.direction = "up"
        self.image = self.original_img

    def update(self, keys):
        diagonal_speed = self.speed // 4
        moving_now = False
        dx = dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = "left"
            dx -= self.speed
            moving_now = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = "right"
            dx += self.speed
            moving_now = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = "up"
            dy -= self.speed
            moving_now = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = "down"
            dy += self.speed
            moving_now = True

        if ((keys[pygame.K_UP] or keys[pygame.K_w])
                and (keys[pygame.K_LEFT] or keys[pygame.K_a])):
            self.direction = "up-left"
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s])
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.direction = "down-right"
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s])
                and (keys[pygame.K_LEFT] or keys[pygame.K_a])):
            self.direction = "down-left"
        if ((keys[pygame.K_UP] or keys[pygame.K_w])
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.direction = "up-right"

        self.rect.x += dx
        self.rect.y += dy

        if moving_now and not self.moving:
            self.motorcycle_sound.play(-1)
            self.moving = True
        elif not moving_now and self.moving:
            self.motorcycle_sound.stop()
            self.moving = False

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
