import pygame
from pygame import mixer
from core.game import Game

if __name__ == "__main__":
    pygame.init()
    # mixer.init()
    game = Game()
    game.run()
