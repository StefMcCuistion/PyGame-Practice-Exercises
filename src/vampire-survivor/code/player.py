from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.load_imgs()
        self.state, self.frame_idx = 'down', 0
        self.image = pg.image.load(join('..', 'images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-60, -90)

        # Movement
        self.dir = pg.math.Vector2()
        self.speed = 300
        self.collision_sprites = collision_sprites

    def load_imgs(self):
        self.frames = {'left':[], 'right':[], 'up':[], 'down':[], }

        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('..', 'images', 'player', state)):
                if file_names:
                    for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pg.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)
        print(self.frames)

    def animate(self, dt):
        # get state
        if self.dir.x != 0: 
            self.state = 'right' if self.dir.x > 0 else 'left'
        if self.dir.y != 0:
            self.state = 'down' if self.dir.y > 0 else 'up'

        # animate
        self.frame_idx += 5 * dt
        self.image = self.frames[self.state][int(self.frame_idx) % len(self.frames[self.state])]

    def update(self, dt):
        self.input()
        self.movement(dt)
        self.animate(dt)

    def movement(self, dt):
        self.hitbox.x += self.dir.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox.y += self.dir.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, dir):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox):
                if dir == 'horizontal':
                    if self.dir.x > 0: self.hitbox.right = sprite.rect.left
                    if self.dir.x < 0: self.hitbox.left = sprite.rect.right
                if dir == 'vertical':
                    if self.dir.y > 0: self.hitbox.bottom = sprite.rect.top
                    if self.dir.y < 0: self.hitbox.top = sprite.rect.bottom

    def input(self):
        keys = pg.key.get_pressed()
        self.dir.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.dir.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        self.dir = self.dir.normalize() if self.dir else self.dir


    
