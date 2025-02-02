from settings import *

class AllSprites(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pg.display.get_surface()

    def draw(self):
        for sprite in self:
            self.display.blit(sprite.image, sprite.rect)