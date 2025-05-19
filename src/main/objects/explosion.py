import pygame
import os

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, frames_folder, frame_rate=5):
        super().__init__()
        self.frames = []
        self.load_frames(frames_folder)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=center)
        self.frame_rate = frame_rate
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_rate:
            self.frame_counter = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]

    def load_frames(self, frames):
        for i in range(1,5):
            path = os.path.join(frames,"explosion-80x61.png")
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (80,61))
            self.frames.append(img)
