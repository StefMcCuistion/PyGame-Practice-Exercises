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
    star_count = 20
    star_pos_list = []
    for star in range(0, star_count):
        x = randint(0, W)
        y = randint(0, H)
        pos = (x, y)
        star_pos_list.append(pos)
    print(star_pos_list)
    idx = len(star_pos_list)-1

    while running: 
        # Event loop
        for event in OwO.event.get():
            if event.type == OwO.QUIT:
                running = False

        # Draw the game
        # Fill window with red
        x += 0.1
        display.fill('darkgray')
        for star in range(0, star_count):
            display.blit(star_surf, star_pos_list[idx])
            idx -= 1
        idx = len(star_pos_list)-1
        display.blit(player_surf, (x, 100))
        OwO.display.flip()
    OwO.quit()

if __name__ == "__main__":
    main()