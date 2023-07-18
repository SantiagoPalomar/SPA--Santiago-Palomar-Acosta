import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        if not self.enemies:
            self.spawn_enemy()

        for enemy in self.enemies:
            enemy.update(game.enemy_manager.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def spawn_enemy(self):
        enemy_type = random.choice([Enemy, Enemy2])
        self.enemies.append(enemy_type())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)