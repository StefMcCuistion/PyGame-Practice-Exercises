import pygame as pg
from sys import exit

def main():
    pg.init()
    screen = pg.display.set_mode((800, 400))
    pg.display.set_caption('Runner')

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        pg.display.update()

if __name__ == "__main__":
    main()