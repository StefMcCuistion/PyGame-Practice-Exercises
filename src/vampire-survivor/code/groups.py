from settings import *

class AllSprites(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pg.display.get_surface()
        self.offset = pg.Vector2(0, 0)

    def draw(self, target_pos):
        self.offset.x = -target_pos[0] + W / 2
        self.offset.y = -target_pos[1] + H / 2

        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        obj_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        for layer in [ground_sprites, obj_sprites]:
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                self.display.blit(sprite.image, sprite.rect.topleft + self.offset)