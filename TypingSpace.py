import arcade

from model import World

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)

        self.background_texture = arcade.load_texture('images/backgroundSpace.jpg')
        self.my_ship_texture = arcade.load_texture('images/myShip.png')
        self.enemy_texture = arcade.load_texture('images/ship.png')
        self.bullet_texture = arcade.load_texture('images/bullet.png')

    def draw_bullet(self):
        for bullet in self.world.bullets:
            arcade.draw_texture_rectangle(bullet.x, bullet.y, bullet.width, bullet.height, self.bullet_texture)

    def draw_enemy(self):
        for ship in self.world.enemys:
            arcade.draw_texture_rectangle(ship.x, ship.y, ship.width, ship.height, self.enemy_texture)

    def draw_status(self):
        arcade.draw_text(str(self.world.spawn_time), self.width - 550, self.height - 30, arcade.color.WHITE, 20)

    def draw_word(self):
        for i in range(len(self.world.typing_word.word)):
            if self.world.typing_word.index > i:
                self.picture_name = 'images/' + self.world.typing_word.word[i] + 'R' + '.png'
            else:
                self.picture_name = 'images/' + self.world.typing_word.word[i] + '.png'
            self.picture_word = arcade.load_texture(self.picture_name)
            arcade.draw_texture_rectangle(100 + (i * 50), 100, 50, 50, self.picture_word)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_texture)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, 75, SCREEN_WIDTH, 150, self.my_ship_texture)

        self.draw_enemy()
        self.draw_bullet()
        self.draw_status()
        self.draw_word()

    def animate(self, delta_time):
        self.world.animate(delta_time)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
