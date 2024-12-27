import pygame as pg
import os
import ctypes
from sys import exit

def display_bg(name, screen):
    surf = pg.image.load(f'img/bg_{name}.png') # Loads and stores called image
    x, y = screen.get_size() # Retrieves screen size
    pg.transform.scale(surf, (x, y), screen) # Resizes img to screen size and blits it

def start_menu(screen, clock):

    display_bg('start', screen)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        pg.display.update()
        clock.tick(120)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1' # centers window when not in fullscreen
    pg.init()
    pg.font.init()
    ctypes.windll.user32.SetProcessDPIAware() # keeps Windows GUI scale settings from messing with resolution
    clock = pg.time.Clock()
    pg.display.set_caption("Stef's Practice Game")
    screen = pg.display.set_mode((1280, 720))
    
    start_menu(screen, clock)


if __name__ == '__main__':
    main()