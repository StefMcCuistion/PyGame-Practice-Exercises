import pygame
from sys import exit

def start_menu(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption("Stef's Practice Game")
    screen = pygame.display.set_mode((1280, 720))
    
    start_menu(screen)


if __name__ == '__main__':
    main()