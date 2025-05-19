import os
import random
import pygame

from objects.asteroid import Asteroid
from objects.bonus import Bonus
from objects.explosion import Explosion
from objects.rocket import Rocket
from src.main.core.const import *

# первірка шляху до файлів
try:
    game_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    IMG_DIR = os.path.join(game_dir, "assets", "img")
    snd_dir = os.path.join(game_dir, "assets", "snd")

except pygame.error as e:
    print(e)
    pygame.quit()
    exit()

class Game:
    def __init__(self):
        # розміри для створення вікна
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # назва вікна
        pygame.display.set_caption("Airplane Adventure")
        pygame.display.set_icon(
            pygame.image.load(os.path.join(IMG_DIR, "icon_10x16.png"))
        )
        # змінна для вірної швидкості гри
        self.clock = pygame.time.Clock()
        # змінна для циклу гри
        self.running = True
        try:
        # Завантаження зображень
            self.rocket_img = pygame.image.load(os.path.join(IMG_DIR, "rocket_40x64.png"))
            self.asteroid_img = pygame.image.load(os.path.join(IMG_DIR, "asteroid_48x50.png"))
            self.bonus_img = pygame.image.load(os.path.join(IMG_DIR, "bonus_49x50.png"))
            self.background_img = pygame.image.load(os.path.join(IMG_DIR, "background_1100x691.png"))

            # завантаження звуків
            self.coin_sound = pygame.mixer.Sound(os.path.join(snd_dir, "coin-257878.wav"))
            self.boom_sound = pygame.mixer.Sound(os.path.join(snd_dir, "cinematic-boom-171285.wav"))
        except pygame.error as e:
            print(e)
            pygame.quit()
            exit()

        self.boom_sound.set_volume(0.2)
        self.coin_sound.set_volume(0.2)
        # pygame.mixer.music.load(os.path.join(snd_dir, "background-music-109766.mp3"))
        # pygame.mixer.music.set_volume(0.2)
        # pygame.mixer.music.play(loops=-1, start=0.0)
        # pygame.mixer.music.set_volume(0.2)

        # Створення спрайтів
        self.rocket = Rocket(self.rocket_img, (100, SCREEN_HEIGHT // 2))
        self.rocket_group = pygame.sprite.GroupSingle(self.rocket)

        self.asteroids = pygame.sprite.Group()
        self.bonuses = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        # додаємо 1 астероїд
        self.asteroids.add(Asteroid(self.asteroid_img, speed=5))
        # додаємо 1 бонус
        self.bonuses.add(Bonus(self.bonus_img, speed=5))

        self.score = 0
        self.last_score = self.score
        self.lives = 10
        self.level = 1
        # об'єкт шрифта для відображення всього тексту в грі
        self.font = pygame.font.SysFont(None, 40)

    # керування події при натисканні клавіш
    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                self.running = False

        self.rocket_group.update(keys)

    # це функція обновляє всі зміни в кадрі
    def update(self):
        self.asteroids.update()
        self.bonuses.update()

        # Колізії з астероїдами
        # зберігається список з штовхнувшимися об'єктами
        collided = pygame.sprite.spritecollide(self.rocket, self.asteroids, False)
        if collided:
            self.lives -= 1
            self.rocket.rect.center = (100, SCREEN_HEIGHT // 2)

            for asteroid in collided:
                self.boom_sound.play()
                self.explosions.add(Explosion(asteroid.rect.center, IMG_DIR))
                # скидання позиції астероїда
                asteroid.rect.x = SCREEN_WIDTH
                asteroid.rect.y = random.randrange(0, SCREEN_HEIGHT - ASTEROID_SIZE)
            if self.lives <= 0:
                self.running = False

        # зіткнення ракети та бонусів
        hits = pygame.sprite.spritecollide(self.rocket, self.bonuses, dokill=True)
        for _ in hits:
            self.score += 1
            self.coin_sound.play()
            self.bonuses.add(Bonus(self.bonus_img, speed=5 + self.score // 10))

        # Підвищення рівня та нові астероїди
        if self.score >= self.last_score + 10 and len(self.asteroids) < 5:
            self.level += 1
            self.asteroids.add(Asteroid(self.asteroid_img, speed=5 + self.score // 10))
            self.rocket.speed += 1
            self.last_score = self.score

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))
        self.rocket_group.draw(self.screen)
        self.asteroids.draw(self.screen)
        self.bonuses.draw(self.screen)
        self.explosions.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score} "
                                      f"Lives: {self.lives} "
                                      f"Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.explosions.update()
            self.draw()

        pygame.quit()
