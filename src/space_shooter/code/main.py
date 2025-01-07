import pygame as OwO
from os.path import join
from random import randint, uniform

def main():
    class Player(OwO.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = OwO.image.load(join('..', 'images', 'player.png')).convert_alpha()
            self.rect = self.image.get_frect(center = (W / 2, H / 2))
            self.dir = OwO.math.Vector2()
            self.speed = 300

            # Cooldown
            self.can_shoot = True
            self.lazer_shoot_time = 0
            self.cooldown_duration = 400

        def lazer_timer(self):
            if not self.can_shoot:
                current_time = OwO.time.get_ticks()
                if current_time - self.laser_shoot_time >= self.cooldown_duration:
                    self.can_shoot = True

        def update(self, dt):
            keys = OwO.key.get_pressed()
            recent_keys = OwO.key.get_just_pressed()

            self.dir.x = int(keys[OwO.K_RIGHT]) - int(keys[OwO.K_LEFT])
            self.dir.y = int(keys[OwO.K_DOWN]) - int(keys[OwO.K_UP])
            self.dir = self.dir.normalize() if self.dir else self.dir
            self.rect.center += self.dir * self.speed * dt

            if recent_keys[OwO.K_SPACE] and self.can_shoot:
                Lazer(lazer_surf, self.rect.midtop, all_sprites)
                self.can_shoot = False
                self.laser_shoot_time = OwO.time.get_ticks()

            self.lazer_timer()

    class Star(OwO.sprite.Sprite):
        def __init__(self, groups, surf):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_frect(center = (randint(0, W), randint(0, H)))

    class Lazer(OwO.sprite.Sprite):
        def __init__(self, surf, pos, groups):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_frect(midbottom = pos)

        def update(self, dt):
            self.rect.centery -= 400 * dt
            if self.rect.bottom < 0: self.kill()

    class Meteor(OwO.sprite.Sprite):
        def __init__(self, surf, pos, groups):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_frect(center = pos)
            self.creation_time = OwO.time.get_ticks()
            self.lifespan = 3500
            self.dir = OwO.math.Vector2(uniform(-0.5, 0.5), 1)
            self.speed = randint(400, 500)

        def update(self, dt):
            self.rect.center += self.dir * self.speed * dt
            current_time = OwO.time.get_ticks()
            if self.lifespan < current_time - self.creation_time:
                self.kill()

            

    # General setup
    W, H = (
            1280,
            720
    )       # Window width and height
    OwO.init()
    all_sprites = OwO.sprite.Group()
    display = OwO.display.set_mode((W, H))
    OwO.display.set_caption('Space Shooter')
    clock = OwO.time.Clock()
    running = True


    star_surf = OwO.image.load(join('..', 'images', 'star.png')).convert_alpha()
    for i in range(20): 
        Star(all_sprites, star_surf)
    player = Player(all_sprites)



    ## Meteor
    meteor_surf = OwO.image.load(join('..', 'images', 'meteor.png')).convert_alpha()

    ## Lazer
    lazer_surf = OwO.image.load(join('..', 'images', 'laser.png')).convert_alpha()

    # Custom events -> Meteor event
    meteor_event = OwO.event.custom_type()
    OwO.time.set_timer(meteor_event, 500)

    while running:
        dt = clock.tick(120) / 1000
        # Event loop
        for event in OwO.event.get():
            if event.type == OwO.QUIT:
                running = False
            if event.type == meteor_event:
                x, y = randint(0, W), randint(-200, -100)
                Meteor(meteor_surf, (x, y), all_sprites)

        # Draw the game

        all_sprites.update(dt)

        display.fill('darkgray')

        all_sprites.draw(display)

        OwO.display.flip()
    OwO.quit()
if __name__ == '__main__':
    main()
