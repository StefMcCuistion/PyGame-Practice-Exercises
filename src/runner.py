import pygame as pg
from sys import exit

def main():
    pg.init()
    screen = pg.Surface((800, 400))
    W, H = (
            1600, 
            800,
    )
    window = pg.display.set_mode((W, H))
    pg.display.set_caption('Runner')
    clock = pg.time.Clock()

    bg = pg.image.load('runner/graphics/sky.png')
    ground = pg.image.load('runner/graphics/ground.png')

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        screen.blit(bg)
        screen.blit(ground, (0, 300))
        pg.transform.scale(screen, (W, H), window)
        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()