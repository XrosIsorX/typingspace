import arcade.key
from random import randint

MODE_STAMINA = 0
MODE_DEFENSE = 1

class typingWord:
    def __init__(self, word, x, y):
        self.word = word
        self.x = x
        self.y = y
        self.index = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.mode = []
        self.mode.append(typingWord("stamina", 100,100))
        self.mode.append(typingWord("defense", 200,100))

    def animate(self, delta_time):
        self.x = delta_time
