import pygame
from sprites import *
import random



       # keys = pygame.key.get_pressed()
       # if pygame.mouse.get_pressed()[0]:  # left, mid, right (0,1,2)
        #    pygame.draw.rect(screen, YELLOW, (bullet_x, bullet_y, bullet_size, bullet_size))
         #   print("lmb pressed")


    # (620,80), (50,50), (50, 400,), (666,410,)

if detect_collision_bullet(bullet_x, bullet_y, enemy_x, enemy_y):
    score += 1
    new_pos = random.randint(1, 4)
    if new_pos == 1:
        enemy_x = 620
        enemy_y = 80
    elif new_pos == 2:
        enemy_x = 50
        enemy_y = 50
    elif new_pos == 3:
        enemy_x = 50
        enemy_y = 400
    elif new_pos == 4:
        enemy_x = 666
        enemy_y = 410

# if detect_collision(player_x, player_y, enemy_x, enemy_y):
    # game_over = True
   # break





