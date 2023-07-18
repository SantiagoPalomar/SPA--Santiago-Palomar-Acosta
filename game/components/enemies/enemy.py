import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets import bullet_manager

from game.utils.constants import BULLET_ENEMY, ENEMY_1, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


LEFT = "left"
RIGHT = "right"

class Enemy(Sprite):
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 6
    SPEED_Y = 6

    def __init__(self):
        super().__init__()
        self.type = ENEMY_TYPE
        self.image = pygame.transform.scale(ENEMY_1, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 50)
        self.moving_index = 0

        self.shooting_time = random.randint(30, 50)

    def update(self, bullet_manager):
        self.rect.y += self.speed_y
        self.shoot(bullet_manager)
        if self.movement == RIGHT:
            self.rect.x += self.speed_x
        else:
            self.rect.x -= self.speed_x

        self.update_movement()

    def update_movement(self):
        self.moving_index += 1
        if self.rect.right >= SCREEN_WIDTH:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = BULLET_ENEMY(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += current_time + random.randint(30, 50)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

