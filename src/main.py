import pygame as pg
import os
import ctypes
from sys import exit

def find_ratio(x):
    """
    Finds ratio of 5120x2880 to the active resolution. Used in scaling backgrounds, sprites, and fonts. 
    """
    ratio = x/5120
    return ratio

def display_bg(name, screen):
    img = pg.image.load(f'img/bg_{name}.png').convert_alpha() # Loads img
    x, y = screen.get_size() # Retrieves screen size
    pg.transform.scale(img, (x, y), screen) # Resizes img to screen size and blits it

def display_spr(name, screen, pos):
    img = pg.image.load(f'img/spr_{name}.png') # Loads img
    x, y = screen.get_size() # Retrieves screen size
    w, h = img.get_size() # Retrieves img dimensions
    ratio = find_ratio(x)
    # Uses ratio to resize img appropriately for current resolution
    img = pg.transform.scale(img, (w*ratio, h*ratio))
    screen.blit(img, (pos[0]*ratio, pos[1]*ratio))

def display_txt(surf, screen, pos):
    x, y = screen.get_size()
    w, h = surf.get_size()
    ratio = find_ratio(x)
    surf = pg.transform.scale(surf, (w*ratio, h*ratio))
    screen.blit(surf, (pos[0]*ratio, pos[1]*ratio))

def set_res(settings):
    res = settings.get('Resolution')
    res = list(map(int, res.split('x'))) # turns string into a list of ints
    fullscreen = settings.get('Fullscreen')
    print(f'fullscreen = {fullscreen}')
    if fullscreen == "0":
        screen = pg.display.set_mode(res)
    else: 
        screen = pg.display.set_mode(res, pg.FULLSCREEN)
    return screen

def start_menu(screen, settings):

    X, Y = 5120, 2880
    clock = pg.time.Clock()

    protag_x = X*.1

    font = pg.font.SysFont('Comic Sans', 100)
    header = font.render("Stef's test game", True, 'Black')

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        display_bg('start', screen)
        display_spr('ground', screen, (0, Y-320))
        display_spr('protag', screen, (protag_x, Y-860))
        display_txt(header, screen, (X*.5-(header.get_size()[0]*.5), Y*.02))
        pg.display.update()
        clock.tick(200)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1' # centers window when not in fullscreen
    pg.init()
    pg.font.init()
    ctypes.windll.user32.SetProcessDPIAware() # keeps Windows GUI scale settings from messing with resolution
    pg.display.set_caption("Stef's Practice Game")

    # Opens settings.csv and creates dictionary for settings
    settings = {}
    with open('settings.csv') as file:
        for line in file:
            key, value = line.split(': ')
            settings[key] = value

    screen = set_res(settings)
    
    start_menu(screen, settings)

if __name__ == '__main__':
    main()