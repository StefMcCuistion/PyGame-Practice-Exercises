import pygame as pg
from sys import exit

def main():

    def display_score():
        current_time = int((pg.time.get_ticks() - start_time)/100)
        score_surf = font.render(f'SCORE: {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (400, 50))
        score_backdrop_rect = score_rect.inflate(10, 10)
        pg.draw.rect(screen, '#c0e8ec', score_backdrop_rect, False, 5)
        screen.blit(score_surf, score_rect)

    def display_title():
        title_surf = font.render("STEF'S GAME", False, 'black')
        title_surf = pg.transform.scale_by(title_surf, 2)
        title_rect = title_surf.get_rect(center = (400, 50))
        screen.blit(title_surf, title_rect)

    def display_instructions():
        instructions_surf = font.render("Press SPACE to START GAME or to JUMP", False, (64, 64, 64))
        instructions_rect = instructions_surf.get_rect(center = (400, 370))
        screen.blit(instructions_surf, instructions_rect)

    pg.init()
    screen = pg.display.set_mode((800, 400))
    pg.display.set_caption('Runner')
    clock = pg.time.Clock()
    font = pg.font.Font('runner/font/pixeltype.ttf', 50)

    game_active = False
    start_time = 0

    bg_surf = pg.image.load('runner/graphics/sky.png').convert()
    ground_surf = pg.image.load('runner/graphics/ground.png').convert()

    snail_surf = pg.image.load('runner/graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surf.get_rect(midbottom = (700, 300))

    player_surf = pg.image.load('runner/graphics/player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    player_stand = pg.image.load('runner/graphics/player/player_stand.png').convert_alpha()
    player_stand = pg.transform.scale_by(player_stand, 3)
    player_stand_rect = player_stand.get_rect(center = (400, 200))

    gravity = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if game_active:
                    if event.key == pg.K_SPACE and player_rect.bottom == 300:
                        gravity = -18
                else:
                    game_active = True
                    snail_rect.left = screen.get_width()   
                    start_time = pg.time.get_ticks()   
        if game_active:
            screen.blit(bg_surf)
            screen.blit(ground_surf, (0, 300))
            display_score()

            screen.blit(snail_surf, snail_rect)

            snail_rect.left -= 4
            if snail_rect.right < 0:
                snail_rect.left = screen.get_width()

            gravity += .8
            screen.blit(player_surf, player_rect)
            player_rect.y += gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300

            if player_rect.colliderect(snail_rect):
                game_active = False
        else:
            screen.fill((94, 129, 162))
            screen.blit(player_stand, player_stand_rect)
            display_instructions()
            display_title()


        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()