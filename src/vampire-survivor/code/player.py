from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_idx = 0
        self.image = self.frames[self.frame_idx]
        self.rect = self.image.get_frect(center = pos)
        self.dir = pg.math.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pg.key.get_pressed()
        self.dir.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.dir.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        self.dir = self.dir.normalize() if self.dir else self.dir
        self.rect.center += self.dir * self.speed * dt
        if self.dir:
            self.frame_idx += 5 * dt
        else: 
            self.frame_idx = 0
        self.image = self.frames[int(self.frame_idx) % len(self.frames)]


    
