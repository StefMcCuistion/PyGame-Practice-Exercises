from settings import *

class Game():
    class Player(pg.sprite.Sprite):
        def __init__(self, frames, groups):
            super().__init__(groups)
            self.frames = frames
            self.frame_idx = 0
            self.image = self.frames[self.frame_idx]
            self.rect = self.image.get_frect(center = (W / 2, H / 2))
            self.dir = pg.math.Vector2()
            self.speed = 300

        def update(self, dt):
            keys = pg.key.get_pressed()
            self.dir.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
            self.dir.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
            self.dir = self.dir.normalize() if self.dir else self.dir
            self.rect.center += self.dir * self.speed * dt
    
    # Setup
    pg.init()
    display = pg.display.set_mode((W, H))
    pg.display.set_caption('Vampire Survivor Clone')
    clock = pg.time.Clock()
    running = True

    # Imports
    player_frames = [pg.image.load(join('..', 'images', ))]