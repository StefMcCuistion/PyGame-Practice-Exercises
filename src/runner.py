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
    font = pg.font.Font('runner/font/pixeltype.ttf', 50)

    bg_surf = pg.image.load('runner/graphics/sky.png').convert()
    ground_surf = pg.image.load('runner/graphics/ground.png').convert()
    txt_surf = font.render("Stef's Game", False, 'Black').convert()

    snail_surf = pg.image.load('runner/graphics/snail/snail1.png').convert_alpha()
    snail_x = 600

    player_surf = pg.image.load('runner/graphics/player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        screen.blit(bg_surf)
        screen.blit(ground_surf, (0, 300))
        screen.blit(txt_surf, (300, 50))
        screen.blit(snail_surf, (snail_x, 264))
        player_rect.left += 4
        screen.blit(player_surf, player_rect)
        snail_x -= 4
        if snail_x < -72:
            snail_x = screen.get_width()
        pg.transform.scale(screen, (W, H), window)
        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()