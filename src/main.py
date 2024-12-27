import pygame as pg
import os
import ctypes
from sys import exit

def display_bg(name, screen):
    img = pg.image.load(f'img/bg_{name}.png') # Loads img
    x, y = screen.get_size() # Retrieves screen size
    pg.transform.scale(img, (x, y), screen) # Resizes img to screen size and blits it

def set_res(settings):
    res = settings.get('Resolution')
    res = list(map(int, res.split('x')))
    screen = pg.display.set_mode(res)
    return screen

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

    # Opens settings and creates dictionary
    settings = {}
    with open('settings.csv') as file:
        for line in file:
            key, value = line.split(': ')
            settings[key] = value

    screen = set_res(settings)    
    
    start_menu(screen, clock)

if __name__ == '__main__':
    main()