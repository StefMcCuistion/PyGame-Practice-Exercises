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

    while running: 
        # Event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Draw the game
        # Fill window with red
        display.fill('red')
        pg.display.flip()
    pg.quit()

if __name__ == "__main__":
    main()