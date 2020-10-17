import pygame
from sprites import *
import random
def enemy_move(player_x, player_y, enemy_x, enemy_y):
    p_x = player_x
    p_y = player_y
    e_x = enemy_x
    e_y = enemy_y
    if e_x > p_x:
        e_x -= 10
    elif e_x < p_x:
        e_x += 10
    if e_y > p_y:
        e_y -= 10
    elif e_y < p_y:
        e_y += 10
    return (e_x,e_y)


def detect_collision(player_x, player_y, enemy_x, enemy_y):
    p_x = player_x
    p_y = player_y
    e_x = enemy_x
    e_y = enemy_y

    if((p_x < e_x + enemy_size) and
        (p_x + player_size > e_x) and
        (p_y < e_y + enemy_size) and
        (p_y + player_size > e_y)):
        print("Collision")
        return True


def detect_collision_bullet(player_x, player_y, enemy_x, enemy_y):
    p_x = player_x
    p_y = player_y
    e_x = enemy_x
    e_y = enemy_y

    if p_x < e_x + enemy_size and p_x + bullet_size > e_x and p_y < e_y + enemy_size and p_y + bullet_size > e_y:
        print("Collision")
        return True


# mouse_pos = pygame.mouse.get_pos()
# mouse_x = mouse_pos[0]
# mouse_y = mouse_pos[1]

       # keys = pygame.key.get_pressed()
       # if pygame.mouse.get_pressed()[0]:  # left, mid, right (0,1,2)
        #    pygame.draw.rect(screen, YELLOW, (bullet_x, bullet_y, bullet_size, bullet_size))
         #   print("lmb pressed")

    # Vector2 do smooth movement


if e_x > p_x:
    e_x -= 1
elif e_x < p_x:
    e_x += 1
if e_y > p_y:
    e_y -= 1
elif e_y < p_y:
    e_y += 1

if m_x < b_x:
    b_x -= 6
elif m_x > b_x:
    b_x += 6
if m_y < b_y:
    b_y -= 6
elif m_y > b_y:
    b_y += 6


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





