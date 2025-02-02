from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, frames, groups, collision_sprites):
        super().__init__(groups)
        self.frames = frames
        self.frame_idx = 0
        self.image = self.frames[self.frame_idx]
        self.rect = self.image.get_frect(center = pos)

        # Movement
        self.dir = pg.math.Vector2()
        self.speed = 300
        self.collision_sprites = collision_sprites

    def update(self, dt):
        self.input()
        self.movement(dt)
        if self.dir:
            self.frame_idx += 5 * dt
        else: 
            self.frame_idx = 0
        self.image = self.frames[int(self.frame_idx) % len(self.frames)]

    def movement(self, dt):
        self.rect.x += self.dir.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.dir.y * self.speed * dt
        self.collision('vertical')

    def collision(self, dir):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if dir == 'horizontal':
                    if self.dir.x > 0: self.rect.right = sprite.rect.left

    def input(self):
        keys = pg.key.get_pressed()
        self.dir.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.dir.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        self.dir = self.dir.normalize() if self.dir else self.dir


    
