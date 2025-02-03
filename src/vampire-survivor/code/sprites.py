from settings import *

class Sprite(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprite(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Gun(pg.sprite.Sprite):
    def __init__(self, player, groups):
        # player connection
        self.player = player
        self.distance = 140
        self.player_dir = pg.Vector2(1, 0)

        # sprite setup
        super().__init__(groups)
        self.gun_surf = pg.image.load(join('..', 'images', 'gun', 'gun.png')).convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center = self.player.rect.center + self.player_dir * self.distance)

    def get_dir(self):
        mouse_pos = pg.Vector2(pg.mouse.get_pos())
        player_pos = pg.Vector2(W / 2, H / 2)
        self.player_dir = (mouse_pos - player_pos).normalize()

    def update(self, _):
        self.get_dir()
        self.rect.center = self.player.rect.center + self.player_dir * self.distance