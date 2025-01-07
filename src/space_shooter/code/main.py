import pygame as OwO
from os.path import join
from random import randint

W, H = (
        1280,
        720
)       # Window width and height

class Player(OwO.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = OwO.image.load(join('..', 'images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (W / 2, H / 2))
        self.dir = OwO.math.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = OwO.key.get_pressed()
        recent_keys = OwO.key.get_just_pressed()

        self.dir.x = int(keys[OwO.K_RIGHT]) - int(keys[OwO.K_LEFT])
        self.dir.y = int(keys[OwO.K_DOWN]) - int(keys[OwO.K_UP])
        self.dir = self.dir.normalize() if self.dir else self.dir
        self.rect.center += self.dir * self.speed * dt

        if recent_keys[OwO.K_SPACE]:
            print('Fire lazer')

def main():
    # General setup
    OwO.init()
    display = OwO.display.set_mode((W, H))
    OwO.display.set_caption('Space Shooter')
    clock = OwO.time.Clock()
    running = True

    all_sprites = OwO.sprite.Group()

    player = Player(all_sprites)

    ## Meteor
    meteor_surf = OwO.image.load(join('..', 'images', 'meteor.png')).convert_alpha()
    meteor_rect = meteor_surf.get_frect(center = (W / 2, H / 2))

    ## Lazer
    lazer_surf = OwO.image.load(join('..', 'images', 'laser.png')).convert_alpha()
    lazer_rect = lazer_surf.get_frect(bottomleft = (20, H - 20))

    ## Stars
    star_surf = OwO.image.load(join('..', 'images', 'star.png')).convert_alpha()
    star_positions = [(randint(0, W), randint(0, H)) for i in range(20)]

    while running:
        dt = clock.tick(120) / 1000
        # Event loop
        for event in OwO.event.get():
            if event.type == OwO.QUIT:
                running = False

        # Draw the game

        all_sprites.update(dt)

        display.fill('darkgray')
        for pos in star_positions:
            display.blit(star_surf, pos)
        display.blit(meteor_surf, meteor_rect)
        display.blit(lazer_surf, lazer_rect)

        all_sprites.draw(display)

        OwO.display.flip()
    OwO.quit()

if __name__ == "__main__":
    main()