from settings import *

class Game():
    class Player(pg.sprite.Sprite):
        def __init__(self, frames, groups):
            super().__init__(groups)
            self.frames = frames
            self.frame_idx = 0
            self.image = self.frames[self.frame_idx]
            self.rect = self.image.get_frect(center = (W / 2, H / 2))
            self.dir = pg.math.Vector2()
            self.speed = 300

        def update(self, dt):
            keys = pg.key.get_pressed()
            self.dir.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
            self.dir.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
            self.dir = self.dir.normalize() if self.dir else self.dir
            self.rect.center += self.dir * self.speed * dt

    
    # Setup
    pg.init()
    display = pg.display.set_mode((W, H))
    pg.display.set_caption('Vampire Survivor Clone')
    clock = pg.time.Clock()
    running = True

    # Imports
    player_up_frames = [pg.image.load(join('..', 'images', 'player', 'up', f'{i}.png')).convert_alpha() for i in range(4)]
    player_right_frames = [pg.image.load(join('..', 'images', 'player', 'right', f'{i}.png')).convert_alpha() for i in range(4)]
    player_down_frames = [pg.image.load(join('..', 'images', 'player', 'down', f'{i}.png')).convert_alpha() for i in range(4)]
    player_left_frames = [pg.image.load(join('..', 'images', 'player', 'left', f'{i}.png')).convert_alpha() for i in range(4)]

    # Sprites
    all_sprites = pg.sprite.Group()
    player = Player(player_down_frames, all_sprites)

    while running:
        dt = clock.tick() / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        # Update
        all_sprites.update(dt)

        # Draw the game
        display.fill('gray')
        all_sprites.draw(display)

        pg.display.flip()
    pg.quit()