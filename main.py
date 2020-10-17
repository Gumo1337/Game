from game import *
# if pygame.mouse.get_pressed()[0]:  # left, mid, right (0,1,2)

if __name__ == "__main__":
    g = Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_game_over_screen()
    pg.quit()
