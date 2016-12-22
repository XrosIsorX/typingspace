import arcade.key
from random import randint

MODE_STAMINA = 0
MODE_DEFENSE = 1

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Spacecraft(Model):
    def __init__(self, world, x, y, width, height):
        super().__init__(world, x, y)
        self.width = width
        self.height = height

    def shot(self):
        self.x = 0

class typingWord():
    def __init__(self, world, word):
        self.word = word
        self.index = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.count_time = 0

        self.enemys = []
        self.typing_word = typingWord(self, 'ABC')

    # def update_word(self):
    #     if
    # # def typing(self):
    # #

    def spawn_ship(self):
        if self.count_time > 1:
            self.enemys.append(Spacecraft(self, randint(0, 900), randint(400, 600), 64 ,128))
            self.count_time = 0

    def animate(self, delta_time):
        self.spawn_ship()

        self.count_time += delta_time
