import pygame as OwO
from os.path import join
from random import randint

W, H = (
        1280,
        720
) # Window width and height

class Player(OwO.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = OwO.image.load(join('..', 'images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (W / 2, H / 2))

def main():
    # General setup
    OwO.init()
    display = OwO.display.set_mode((W, H))
    OwO.display.set_caption('Space Shooter')
    clock = OwO.time.Clock()
    running = True

    all_sprites = OwO.sprite.Group()

    # Imports
    ## Player
    # player_surf = OwO.image.load(join('..', 'images', 'player.png')).convert_alpha()
    # player_rect = player_surf.get_frect(bottomleft = (10, H - 10))
    player = Player(all_sprites)
    player_dir = OwO.math.Vector2()
    player_speed = 300

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


        # Input
        OwO.key.set_repeat()

        keys = OwO.key.get_pressed()
        player_dir.x = int(keys[OwO.K_RIGHT]) - int(keys[OwO.K_LEFT])
        player_dir.y = int(keys[OwO.K_DOWN]) - int(keys[OwO.K_UP])
        player_dir = player_dir.normalize() if player_dir else player_dir
        # player_rect.center += player_dir * player_speed * dt

        # recent_keys = OwO.key.get_just_pressed()
        # if recent_keys[OwO.K_SPACE]:
        #     print('Fire lazer')
            

        # Draw the game

        all_sprites.update()

        display.fill('darkgray')
        for pos in star_positions:
            display.blit(star_surf, pos)

        display.blit(meteor_surf, meteor_rect)

        display.blit(lazer_surf, lazer_rect)
        ## Player movement
        # player_rect.center += player_dir * player_speed * dt
        # if player_rect.top <= 0:
        #     player_dir.y *= -1
        # if player_rect.bottom >= H:
        #     player_dir.y *= -1
        # if player_rect.left <= 0:
        #     player_dir.x *= -1
        # if player_rect.right >= W:
        #     player_dir.x *= -1
        all_sprites.draw(display)

        OwO.display.flip()
    OwO.quit()

if __name__ == "__main__":
    main()