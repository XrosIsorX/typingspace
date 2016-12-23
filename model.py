import arcade.key
from random import randint

SHIP_SPAWN = 3
SHIP_SHOT = 3
SHIP_SPAWN_TIME = 3
SHIP_SHOT_TIME = 3

class Model:
    def __init__(self, world, x, y, width, height):
        self.world = world
        self.width = width
        self.height = height
        self.x = x
        self.y = y

class Laser(Model):
    LASER_TIME = 0.2
    def __init__(self, world, x, y, width, height):
        super().__init__(world, x ,y, width, height)
        self.delay_time = 0

    def animate(self, delta_time):
        self.delay_time += delta_time
        if self.delay_time > self.LASER_TIME:
            self.disappear()
            self.delay_time = 0

    def disappear(self):
        self.world.lasers.remove(self)


class Bullet(Model):
    SPEED = 10
    def __init__(self, world, x, y, width, height):
        super().__init__(world, x, y, width, height)

    def animate(self, delta_time):
        self.y -= self.SPEED
        self.hit()

    def hit(self):
        if self.y < 140:
            self.world.bullets.remove(self)
            self.world.hp -= 1

class Spacecraft(Model):
    def __init__(self, world, x, y, width, height):
        super().__init__(world, x, y, width, height)
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
    hp = 5
    score = 0

    def __init__(self, width, height):
        self.word = []
        self.set_word()

        self.width = width
        self.height = height

        self.spawn_time = 0

        self.enemys = []
        self.bullets = []
        self.lasers = []
        self.typing_word = TypingWord(self, self.random_word())

    def random_word(self):
        return self.word[randint(0,len(self.word))-1]

    def set_word(self):
        openfile = open('words.txt')
        lines = openfile.readlines()
        for line in lines:
            item = line.strip()
            self.word.append(item)

    def reset_typing_word(self):
        self.typing_word.word = self.random_word()
        self.typing_word.index = 0

    def update_word(self):
         if len(self.typing_word.word) == self.typing_word.index:
             if len(self.enemys) > 0:
                 self.lasers.append(Laser(self, self.enemys[0].x, self.enemys[0].y, 20, 600))
                 self.enemys.remove(self.enemys[0])
                 self.score += 1
                 self.reset_typing_word()


    def spawn_ship(self):
        if self.spawn_time > SHIP_SPAWN_TIME:
            self.enemys.append(Spacecraft(self, randint(0, 900), randint(400, 600), 64 ,128))
            self.spawn_time = 0

    def update_level(self):
        global SHIP_SPAWN_TIME
        SHIP_SPAWN_TIME = SHIP_SPAWN - ((self.score / 5) * 0.1)
        global SHIP_SHOT_TIME
        SHIP_SHOT_TIME = SHIP_SHOT - ((self.score / 10) * 0.1)

    def animate(self, delta_time):
        self.spawn_ship()
        for ship in self.enemys:
            ship.animate(delta_time)
        for bullet in self.bullets:
            bullet.animate(delta_time)
        for laser in self.lasers:
            laser.animate(delta_time)
        self.update_word()
        self.update_level()

        self.spawn_time += delta_time

    def remove_all_enemys(self):
        length = len(self.enemys)
        for ship in range(length):
            self.enemys.remove(self.enemys[0])

    def remove_all_bullet(self):
        length = len(self.bullets)
        for bullet in range(length):
            self.bullets.remove(self.bullets[0])

    def retry(self):
        self.hp = 5
        global SHIP_SPAWN_TIME
        SHIP_SPAWN_TIME = SHIP_SPAWN
        global SHIP_SHOT_TIME
        SHIP_SHOT_TIME = SHIP_SHOT
        self.remove_all_enemys()
        self.remove_all_bullet()
        spawn_time = 0
        self.reset_typing_word()
        self.score = 0


    def on_key_press(self, key, key_modifiers):
        if chr(key) == self.typing_word.word[self.typing_word.index]:
            self.typing_word.index += 1
        if key == arcade.key.ENTER and self.hp <= 0:
            self.retry()
