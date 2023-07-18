import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets import bullet_manager

from game.utils.constants import BULLET_ENEMY, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH


LEFT = "left"
RIGHT = "right"

class Enemy2(Sprite):
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 5

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement = "diagonal"
        self.move_x = random.randint(30, 50)
        self.moving_index = 0
        self.shooting_time = random.randint(30, 50)

    def update(self, bullet_manager):
        if self.movement == "diagonal":
            self.update_diagonal()
        elif self.movement == "down":
            self.update_down()

        self.rect.y += self.speed_y

    def update_diagonal(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right >= SCREEN_WIDTH or self.rect.x <= 0:
            self.movement = "down"

    def update_down(self):
        self.rect.y += self.speed_y

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = BULLET_ENEMY(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += current_time + random.randint(30, 50)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))