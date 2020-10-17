import pygame as pg
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(PLAYER_SIZE)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = PLAYER_START_POS
        self.pos = vec(PLAYER_START_POS)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x -= PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x += PLAYER_ACC
        if keys[pg.K_w]:
            self.acc.y -= PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y += PLAYER_ACC

        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + PLAYER_ACC * self.acc
        self.rect.center = self.pos

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT


class Enemy(Player):
    def __init__(self):
        super(Enemy, self).__init__()
        self.player = Player()
        self.image = pg.Surface(ENEMY_SIZE)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = ENEMY_START_POS
        self.pos = vec(ENEMY_START_POS)

    def update(self):
        self.player.update()
        if self.pos.x > self.player.pos.x:
            self.pos.x -= 1
        elif self.pos.x < self.player.pos.x:
            self.pos.x += 1
        if self.pos.y > self.player.pos.y:
            self.pos.y -= 1
        elif self.pos.y < self.player.pos.y:
            self.pos.y += 1
        self.rect.center = self.pos


class Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(BULLET_SIZE)
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = BULLET_START_POS
        self.pos = vec(BULLET_START_POS)
        self.mouse_pos = pg.mouse.get_pos()

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()
        if self.mouse_pos[0] < self.pos.x:
            self.pos.x -= 6
        elif self.mouse_pos[0] > self.pos.x:
            self.pos.x += 6
        if self.mouse_pos[1] < self.pos.y:
            self.pos.y -= 6
        elif self.mouse_pos[1] > self.pos.y:
            self.pos.y += 6
        self.rect.center = self.pos
