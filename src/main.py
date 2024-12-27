import pygame
import os
import ctypes
from sys import exit

def start_menu(screen, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(120)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1' # centers window when not in fullscreen
    pygame.init()
    pygame.font.init()
    ctypes.windll.user32.SetProcessDPIAware() # keeps windows GUI scale settings from messing with resolution
    clock = pygame.time.Clock()
    pygame.display.set_caption("Stef's Practice Game")
    screen = pygame.display.set_mode((1280, 720))
    
    start_menu(screen, clock)


if __name__ == '__main__':
    main()