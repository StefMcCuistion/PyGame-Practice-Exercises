from settings import *

class AllSprites(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pg.display.get_surface()
        self.offset = pg.Vector2(0, 0)

    def draw(self, target_pos):
        self.offset.x = -target_pos[0] + W / 2
        self.offset.y = -target_pos[1] + H / 2
        for sprite in self:
            self.display.blit(sprite.image, sprite.rect.topleft + self.offset)