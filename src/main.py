import pygame as pg
import os
import ctypes
from sys import exit

def display_bg(name, screen):
    img = pg.image.load(f'img/bg_{name}.png') # Loads img
    x, y = screen.get_size() # Retrieves screen size
    pg.transform.scale(img, (x, y), screen) # Resizes img to screen size and blits it

def display_spr(name, screen, pos):
    img = pg.image.load(f'img/spr_{name}.png') # Loads img
    x, y = screen.get_size() # Retrieves screen size
    w, h = img.get_size() # Retrieves img dimensions
    # Determines ratio of 1920x1080 to current resolution
    if x == 1920:
       ratio = 1
    elif x == 1280:
        ratio = 2/3
    # Uses ratio to resize img appropriately for current resolution
    img = pg.transform.scale(img, (w*ratio, h*ratio))
    screen.blit(img, (pos[0]*ratio, pos[1]*ratio))

def display_txt(surf, screen, pos):
    x, y = screen.get_size()
    w, h = surf.get_size()
    if x == 1920:
       ratio = 1
    elif x == 1280:
        ratio = 2/3
    surf = pg.transform.scale(surf, (w*ratio, h*ratio))
    screen.blit(surf, (pos[0]*ratio, pos[1]*ratio))

def set_res(settings):
    res = settings.get('Resolution')
    res = list(map(int, res.split('x'))) # turns string into a list of ints
    screen = pg.display.set_mode(res)
    return screen

def start_menu(screen, clock):

    X, Y = 1920, 1080

    font = pg.font.SysFont('Cambria', 50)

    display_bg('start', screen)
    display_spr('ground', screen, (0, Y-138))

    txt_surf = font.render("Stef's test game", True, 'Black')

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        display_bg('start', screen)
        display_spr('ground', screen, (0, Y-138))
        display_txt(txt_surf, screen, (X*.5, Y*.1))
        pg.display.update()
        clock.tick(120)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1' # centers window when not in fullscreen
    pg.init()
    pg.font.init()
    ctypes.windll.user32.SetProcessDPIAware() # keeps Windows GUI scale settings from messing with resolution
    clock = pg.time.Clock()
    pg.display.set_caption("Stef's Practice Game")

    # Opens settings.csv and creates dictionary for settings
    settings = {}
    with open('settings.csv') as file:
        for line in file:
            key, value = line.split(': ')
            settings[key] = value

    screen = set_res(settings)    
    
    start_menu(screen, clock)

if __name__ == '__main__':
    main()