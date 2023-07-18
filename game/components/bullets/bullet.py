import pygame
from pygame.sprite import Sprite
from game.components import bullets, spaceship

from game.utils.constants import BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):
    SPEED = 20 
    BULLETS = {ENEMY_TYPE: BULLET_ENEMY}

    def __init__(self, owner):
        super().__init__()
        self.owner = owner
        self.image = pygame.transform.scale(self.BULLETS[self.owner], (10, 30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.bullet_manager.remove_bullet(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)