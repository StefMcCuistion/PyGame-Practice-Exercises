from settings import *
from player import Player
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game():
    def __init__(self):
        # Setup
        pg.init()
        self.display = pg.display.set_mode((W, H))
        pg.display.set_caption('Vampire Survivor Clone')
        self.clock = pg.time.Clock()
        self.running = True

        # Imports
        self.player_up_frames = [pg.image.load(join('..', 'images', 'player', 'up', f'{i}.png')).convert_alpha() for i in range(4)]
        self.player_right_frames = [pg.image.load(join('..', 'images', 'player', 'right', f'{i}.png')).convert_alpha() for i in range(4)]
        self.player_down_frames = [pg.image.load(join('..', 'images', 'player', 'down', f'{i}.png')).convert_alpha() for i in range(4)]
        self.player_left_frames = [pg.image.load(join('..', 'images', 'player', 'left', f'{i}.png')).convert_alpha() for i in range(4)]

        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pg.sprite.Group()

        # Sprites
        self.setup()
        self.player = Player((W / 2, H / 2), self.player_down_frames, self.all_sprites, self.collision_sprites)


    def setup(self):
        map = load_pygame(join('..', 'data', 'maps', 'world.tmx'))
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
        for box in map.get_layer_by_name('Collisions'):
            CollisionSprite((box.x, box.y), pg.Surface((box.width, box.height)), self.collision_sprites)

    def run(self):

        while self.running:
            dt = self.clock.tick() / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False

            # Update
            self.all_sprites.update(dt)

            # Draw the game
            self.display.fill('gray')
            self.all_sprites.draw(self.display)
            pg.display.flip()

        pg.quit()

if __name__ == '__main__':
    game = Game()
    game.run()