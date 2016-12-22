import arcade.key
from random import randint

MODE_STAMINA = 0
MODE_DEFENSE = 1

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class typingWord(Model):
    def __init__(self, world, x, y, word):
        super().__init__(world, x, y)
        self.word = word
        self.index = 0

class Spacecraft(typingWord):
    def __init__(self, world, x, y, word):
        super().__init__(world, x, y, word)

    def shot(self):
        self.x = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.mode = []
        self.mode.append(typingWord(self, 100, 100, "stamina"))
        self.mode.append(typingWord(self, 200, 100, "defense"))
        self.enemys = []
        self.enemys.append(Spacecraft(self, 100, 100, "Hello"))

    def animate(self, delta_time):
        self.x = delta_time
