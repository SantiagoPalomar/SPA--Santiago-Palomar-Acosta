from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE


class BulletManager:
    def __init__(self):
        self.enemy_bullets = []

    def update(self):
        for enemy_bullet in self.enemy_bullets: 
            enemy_bullet.update(self.enemy_bullets)
    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets: 
            enemy_bullet.draw(screen)
                                
    def add_bullet(self, spaceship):
        if spaceship.type == ENEMY_TYPE and  not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))