import pygame as pg
from random import randint
from sys import exit


def main():

    def obstacle_movement(list):
        if list:
            for rect in list:
                rect.x -= 5
                screen.blit(snail_surf, rect)
            list = [obstacle for obstacle in list if obstacle.x > -100]
                
            return list
        else: 
            return []

    def display_score():
        score = int((pg.time.get_ticks() - start_time)/100)
        score_surf = font.render(f'SCORE: {score}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (400, 50))
        score_backdrop_rect = score_rect.inflate(10, 10)
        pg.draw.rect(screen, '#c0e8ec', score_backdrop_rect, False, 5)
        screen.blit(score_surf, score_rect)
        return score

    def display_title():
        title_surf = font.render("STEF'S GAME", False, 'black')
        title_surf = pg.transform.scale_by(title_surf, 2)
        title_rect = title_surf.get_rect(center = (400, 50))
        screen.blit(title_surf, title_rect)

    pg.init()
    screen = pg.display.set_mode((800, 400))
    pg.display.set_caption('Runner')
    clock = pg.time.Clock()
    font = pg.font.Font('font/pixeltype.ttf', 50)


    game_active = False
    start_time = 0

    # Environment
    bg_surf = pg.image.load('graphics/sky.png').convert()
    ground_surf = pg.image.load('graphics/ground.png').convert()

    # Obstacles
    snail_surf = pg.image.load('graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surf.get_rect(midbottom = (randint(900, 1100), 300))

    obstacle_rect_list = []

    # Player
    player_surf = pg.image.load('graphics/player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    player_stand = pg.image.load('graphics/player/player_stand.png').convert_alpha()
    player_stand = pg.transform.scale_by(player_stand, 3)
    player_stand_rect = player_stand.get_rect(center = (400, 200))
    player_stand_rect.y += 10

    score = 0
    gravity = 0

    obstacle_timer = pg.USEREVENT + 1
    pg.time.set_timer(obstacle_timer, 1400)

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
                    start_time = pg.time.get_ticks()  
            if event.type == obstacle_timer and game_active:
                obstacle_rect_list.append(snail_rect)
        if game_active:
            screen.blit(bg_surf)
            screen.blit(ground_surf, (0, 300))
            score = display_score()
            
            gravity += .8
            screen.blit(player_surf, player_rect)
            player_rect.y += gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300

            #Obstacle movement
            obstacle_rect_list = obstacle_movement(obstacle_rect_list)
            if obstacle_rect_list:
                print(obstacle_rect_list)
            if player_rect.colliderect(snail_rect):
                game_active = False


        else:
            screen.fill((94, 129, 162))
            screen.blit(player_stand, player_stand_rect)
            if score == 0:
                message_surf = font.render('Press SPACE to start!', False, (64, 64, 64))
                message_rect = message_surf.get_rect(center = (400, 370))
                screen.blit(message_surf, message_rect)
            else:
                score_surf = font.render(f"Your score was {score}!", False, (64, 64, 64))            
                score_rect = score_surf.get_rect(center = (400, 370))
                screen.blit(score_surf, score_rect)
            display_title()


        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()