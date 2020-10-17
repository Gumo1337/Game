import pygame as pg
from settings import *
from sprites import *
import random
import sys

class Game:
    def __init__(self):     # init
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):      # new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.enemy = Enemy()
        self.all_sprites.add(self.enemy)
        self.bullet = Bullet()
        self.all_sprites.add(self.bullet)
        self.run()

    def run(self):      # game loop\
        self.game_over = False
        while not self.game_over:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):       # update game loop
        self.all_sprites.update()
        if self.detect_collision_bullet():
            self.enemy_reset()
        if (self.detect_collision()):
            self.game_over = True
            self.running = False

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if not self.game_over:
                    self.game_over = True
                self.running = False
                # sys.exit()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 35, YELLOW, FONT_POS[0], FONT_POS[1])
        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def detect_collision(self):
        if self.player.pos.x < self.enemy.pos.x + ENEMY_SIZE[0] and\
                self.player.pos.x + PLAYER_SIZE[0] > self.enemy.pos.x and\
                self.player.pos.y < self.enemy.pos.y + ENEMY_SIZE[1] and\
                self.player.pos.y + PLAYER_SIZE[1] > self.enemy.pos.y :
            return True

    def detect_collision_bullet(self):
        if self.bullet.pos.x < self.enemy.pos.x + ENEMY_SIZE[0] and\
                self.bullet.pos.x + BULLET_SIZE[0] > self.enemy.pos.x and\
                self.bullet.pos.y < self.enemy.pos.y + ENEMY_SIZE[1] and\
                self.bullet.pos.y + BULLET_SIZE[1] > self.enemy.pos.y:
            print("Collision")
            return True

    def enemy_reset(self):
        self.score += 1
        new_pos = random.randint(1, 4)
        if new_pos == 1:
            self.enemy.pos = vec(620, 80)
        elif new_pos == 2:
            self.enemy.pos = vec(50, 50)
        elif new_pos == 3:
            self.enemy.pos = vec(50, 400)
        elif new_pos == 4:
            self.enemy.pos = vec(666, 410)

    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_game_over_screen()

pg.quit()

