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

        self.spacecraft_sprite = []
        for spacecraft in self.world.enemys:
            self.spacecraft_sprite = ModelSprite('images/ship.png', model = spacecraft)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(640, 360, 1280, 720,
                                              self.background_texture)
        self.spacecraft_sprite.draw()

    def animate(self, delta_time):
        self.world.animate(delta_time)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
