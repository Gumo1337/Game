import pygame
import sys
import random
# from pygame.math import Vector2

pygame.init()


GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
player_x = 360
player_y = 240
player_size = 50
enemy_x = 600
enemy_y = 240
enemy_size = 50
score = 0
bullet_size = 10
bullet_x = player_x + 60
bullet_y = player_y + 60
mouse_x = 0
mouse_y = 0

myFont = pygame.font.SysFont("monospace", 35)


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
        (p_x + bullet_size > e_x) and
        (p_y < e_y + enemy_size) and
        (p_y + bullet_size > e_y)):
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


screen = pygame.display.set_mode((720, 480))

game_over = False
clock = pygame.time.Clock()


def a_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        return True
    return False


while not game_over:

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    for event in pygame.event.get():
        x = player_x
        y = player_y
        # print(event)

        if event.type == pygame.QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[0]:  # left, mid, right (0,1,2)
            pygame.draw.rect(screen, YELLOW, (bullet_x, bullet_y, bullet_size, bullet_size))
            print("lmb pressed")

    # Vector2 do smooth movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= 10
            elif event.key == pygame.K_d:
                x += 10
            elif event.key == pygame.K_w:
                y -= 10
            elif event.key == pygame.K_s:
                y += 10
            player_x = x
            player_y = y

    p_x = player_x
    p_y = player_y
    e_x = enemy_x
    e_y = enemy_y
    b_x = bullet_x
    b_y = bullet_y
    m_x = mouse_x
    m_y = mouse_y

    if e_x > p_x:
        e_x -= 1
    elif e_x < p_x:
        e_x += 1
    if e_y > p_y:
        e_y -= 1
    elif e_y < p_y:
        e_y += 1

    if m_x < b_x:
        b_x -= 5
    elif m_x > b_x:
        b_x += 5
    if m_y < b_y:
        b_y -= 5
    elif m_y > b_y:
        b_y += 5

    bullet_x = b_x
    bullet_y = b_y
    enemy_x = e_x
    enemy_y = e_y

    # (620,80), (50,50), (50, 400,), (666,410,)

    if detect_collision(bullet_x, bullet_y, enemy_x, enemy_y):
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

    if detect_collision(player_x, player_y, enemy_x, enemy_y):
        game_over = True
        break

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.draw.rect(screen, YELLOW, (bullet_x, bullet_y, bullet_size, bullet_size))

    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (540, 440))

    clock.tick(60)
    pygame.display.update()
