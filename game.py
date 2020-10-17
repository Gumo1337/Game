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

    def new(self):      # new game
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
        pg.display.flip()
        # myFont = pg.font.SysFont(FONT_NAME, 35)
        # text = "Score:" + str(score)
        # self.label = myFont.render(text, 1, YELLOW)
        # self.screen.blit(self.label, (540, 440))

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

