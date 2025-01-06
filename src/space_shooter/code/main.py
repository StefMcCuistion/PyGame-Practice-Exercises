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

    x = 100
    path = join('..', 'images', 'player.png')
    player_surf = OwO.image.load(path).convert_alpha()

    star_surf = OwO.image.load(join('..', 'images', 'star.png')).convert_alpha()
    star_positions = [(randint(0, W), randint(0, H)) for i in range(20)]

    while running: 
        # Event loop
        for event in OwO.event.get():
            if event.type == OwO.QUIT:
                running = False

        # Draw the game
        # Fill window with red
        x += 0.1
        display.fill('darkgray')
        for pos in star_positions:
            display.blit(star_surf, pos)
        display.blit(player_surf, (x, 100))
        OwO.display.flip()
    OwO.quit()

if __name__ == "__main__":
    main()