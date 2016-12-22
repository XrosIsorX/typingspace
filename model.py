import arcade.key
from random import randint

SHIP_SPAWN_TIME = 2
SHIP_SHOT_TIME = 2

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Bullet(Model):
    SPEED = 10
    def __init__(self, world, x, y, width, height):
        super().__init__(world, x, y)
        self.width = width
        self.height = height

    def animate(self, delta_time):
        self.y -= self.SPEED
        self.hit()

    def hit(self):
        if self.y < 140:
            self.world.bullets.remove(self)
            self.world.hp -= 1


class Spacecraft(Model):
    def __init__(self, world, x, y, width, height):
        super().__init__(world, x, y)
        self.width = width
        self.height = height
        self.shot_time = 0

    def animate(self, delta_time):
        self.shot_time += delta_time
        if self.shot_time > SHIP_SHOT_TIME:
            self.shot()
            self.shot_time = 0

    def shot(self):
        self.world.bullets.append(Bullet(self.world, self.x, self.y, 11, 23))

class TypingWord():
    def __init__(self, world, word):
        self.word = word
        self.index = 0

class World:
    hp = 3

    def __init__(self, width, height):
        self.word = []
        self.set_word()

        self.width = width
        self.height = height

        self.spawn_time = 0

        self.enemys = []
        self.bullets = []
        random = randint(0,len(self.word)-1)
        self.typing_word = TypingWord(self, self.random_word())

    def random_word(self):
        return self.word[randint(0,len(self.word))-1]

    def set_word(self):
        openfile = open('word.txt')
        lines = openfile.readlines()
        for line in lines:
            item = line.strip()
            self.word.append(item)

    def update_word(self):
         if len(self.typing_word.word) == self.typing_word.index:
             if len(self.enemys) > 0:
                 self.enemys.remove(self.enemys[0])
                 self.typing_word.word = self.random_word()
                 self.typing_word.index = 0

    def spawn_ship(self):
        if self.spawn_time > SHIP_SPAWN_TIME:
            self.enemys.append(Spacecraft(self, randint(0, 900), randint(400, 600), 64 ,128))
            self.spawn_time = 0

    def animate(self, delta_time):
        self.spawn_ship()
        for ship in self.enemys:
            ship.animate(delta_time)
        for bullet in self.bullets:
            bullet.animate(delta_time)
        self.update_word()

        self.spawn_time += delta_time

    def on_key_press(self, key, key_modifiers):
        if chr(key) == self.typing_word.word[self.typing_word.index]:
            self.typing_word.index += 1
