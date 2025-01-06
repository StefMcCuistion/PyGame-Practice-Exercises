import pygame as pg

def main():
    # General setup
    pg.init()
    W, H = (
            1280,
            720
    ) # Window width and height
    display = pg.display.set_mode((W, H))
    pg.display.set_caption('Space Shooter')
    running = True

    x = 100
    player_surf = pg.image.load('../images/player.png')

    while running: 
        # Event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Draw the game
        # Fill window with red
        x += 1
        display.fill('darkgray')
        display.blit(player_surf, (x, 100))
        pg.display.flip()
    pg.quit()

if __name__ == "__main__":
    main()