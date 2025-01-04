import pygame as pg
from sys import exit

def main():
    pg.init()
    screen = pg.display.set_mode((800, 400))
    pg.display.set_caption('Runner')
    clock = pg.time.Clock()
    font = pg.font.Font('runner/font/pixeltype.ttf', 50)

    bg_surf = pg.image.load('runner/graphics/sky.png').convert()
    ground_surf = pg.image.load('runner/graphics/ground.png').convert()

    txt_surf = font.render("Stef's Game", False, (64, 64, 64)).convert()
    txt_rect = txt_surf.get_rect(midbottom = (400, 70))
    txt_backdrop_rect = txt_rect.inflate(10, 10)

    snail_surf = pg.image.load('runner/graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surf.get_rect(midbottom = (700, 300))

    player_surf = pg.image.load('runner/graphics/player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))

    gravity = -20

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and player_rect.bottom == 300:
                    gravity = -20
        screen.blit(bg_surf)
        screen.blit(ground_surf, (0, 300))
        pg.draw.rect(screen, '#c0e8ec', txt_backdrop_rect, False, 5)
        screen.blit(txt_surf, txt_rect)

        screen.blit(snail_surf, snail_rect)

        snail_rect.left -= 4
        if snail_rect.right < 0:
            snail_rect.left = screen.get_width()

        gravity += 1
        screen.blit(player_surf, player_rect)
        player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_rect.colliderect(snail_rect)

        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()