from settings import *

class CollisionSprite(pg.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pg.Surface(size)
        self.rect = self.image.get_frect(center = pos)