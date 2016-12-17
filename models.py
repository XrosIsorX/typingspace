import arcade.key
import math
from random import randint

DIRECTION_UP = 0
DIRECTION_LEFT = 1
DIRECTION_DOWN = 2
DIRECTION_RIGHT = 3

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) \
                and (abs(self.y - other.y) <= hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0

        self.ship = Ship(self, 100, 100)
        self.gold = Gold(self, 100, 400)

    def animate(self, delta):
        self.ship.animate(delta)

        if self.ship.hit(self.gold, 10):
            self.gold.random_location()
            self.score += 1

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.ship.switch_direction(DIRECTION_UP)

        if key == arcade.key.DOWN:
            self.ship.switch_direction(DIRECTION_DOWN)

        if key == arcade.key.LEFT:
            self.ship.switch_direction(DIRECTION_LEFT)

        if key == arcade.key.RIGHT:
            self.ship.switch_direction(DIRECTION_RIGHT)

class Ship(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

        self.direction = DIRECTION_UP
        self.speed = 5

    def switch_direction(self, direction):
        self.angle = direction * 90

    def animate(self, delta):
        if self.x > self.world.width:
            self.x = 0
        if self.x < 0:
            self.x = self.world.width

        if self.y > self.world.height:
            self.y = 0
        if self.y < 0:
            self.y = self.world.height

        self.x -= self.speed * math.sin( self.angle / 180 * math.pi)
        self.y += self.speed * math.cos(self.angle / 180 * math.pi)

class Gold(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    def random_location(self    ):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)
