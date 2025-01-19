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
                Lazer(lazer_surf, self.rect.midtop, (all_sprites, lazer_sprites))
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

    def collision():
        global running

        collision_sprites = OwO.sprite.spritecollide(player, meteor_sprites, False)
        if collision_sprites: 
            running = False
            print('collision')
        for lazer in lazer_sprites:
            collided_sprites = OwO.sprite.spritecollide(lazer, meteor_sprites, True)
            if collided_sprites:
                lazer.kill()


    # General setup
    W, H = (
            1280,
            720
    )       # Window width and height
    OwO.init()
    display = OwO.display.set_mode((W, H))
    OwO.display.set_caption('Space Shooter')
    clock = OwO.time.Clock()
    global running
    running = True

    # Imports
    star_surf = OwO.image.load(join('..', 'images', 'star.png')).convert_alpha()
    meteor_surf = OwO.image.load(join('..', 'images', 'meteor.png')).convert_alpha()
    lazer_surf = OwO.image.load(join('..', 'images', 'lazer.png')).convert_alpha()
    font = OwO.font.Font(join('..', 'images', 'Oxanium-Bold.ttf'), 20)
    txt_surf = font.render('text', True, (240, 240, 240))

    # Sprites
    all_sprites = OwO.sprite.Group()
    meteor_sprites = OwO.sprite.Group()
    lazer_sprites = OwO.sprite.Group()
    for i in range(20): 
        Star(all_sprites, star_surf)
    player = Player(all_sprites)

    # Custom events -> Meteor event
    meteor_event = OwO.event.custom_type()
    OwO.time.set_timer(meteor_event, 500)

    while running:
        dt = clock.tick() / 1000
        # Event loop
        for event in OwO.event.get():
            if event.type == OwO.QUIT:
                running = False
            if event.type == meteor_event:
                x, y = randint(0, W), randint(-200, -100)
                Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))
            if event.type == OwO.KEYDOWN:
                if event.key == OwO.K_ESCAPE:
                    running = False

        # Update
        all_sprites.update(dt)
        collision()

        # Draw the game
        display.fill('#3a2e3f')
        all_sprites.draw(display)
        display.blit(txt_surf, (0, 0))
        OwO.display.flip()
    OwO.quit()

if __name__ == '__main__':
    main()
