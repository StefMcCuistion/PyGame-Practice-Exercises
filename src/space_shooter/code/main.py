import pygame as OwO
from os.path import join
from random import randint

def main():
    # General setup
    OwO.init()
    W, H = (
            1280,
            720
    ) # Window width and height
    display = OwO.display.set_mode((W, H))
    OwO.display.set_caption('Space Shooter')
    running = True

    # Imports
    ## Player
    path = join('..', 'images', 'player.png')
    player_surf = OwO.image.load(path).convert_alpha()
    player_rect = player_surf.get_frect(bottomleft = (10, H - 10))
    player_dir = 1

    ## Meteor
    meteor_surf = OwO.image.load(join('..', 'images', 'meteor.png')).convert_alpha()
    meteor_rect = meteor_surf.get_frect(center = (W / 2, H / 2))

    ## Lazer
    lazer_surf = OwO.image.load(join('..', 'images', 'laser.png')).convert_alpha()
    lazer_rect = lazer_surf.get_frect(bottomleft = (W - 20, H - 20))

    ## Stars
    star_surf = OwO.image.load(join('..', 'images', 'star.png')).convert_alpha()
    star_positions = [(randint(0, W), randint(0, H)) for i in range(20)]

    while running: 
        # Event loop
        for event in OwO.event.get():
            if event.type == OwO.QUIT:
                running = False

        # Draw the game
        display.fill('darkgray')
        for pos in star_positions:
            display.blit(star_surf, pos)

        display.blit(lazer_surf, lazer_rect)

        if player_rect.right == W or player_rect.left == 0:
            player_dir = -player_dir
        player_rect.left += .5*player_dir
        display.blit(player_surf, player_rect)

        display.blit(meteor_surf, meteor_rect)

        OwO.display.flip()
    OwO.quit()

if __name__ == "__main__":
    main()