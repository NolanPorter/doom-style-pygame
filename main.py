import pygame as pg
import sys
from settings import RESOLUTION, FPS
from map import Map

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self) -> None:
        self.map = Map(self)

    def update(self) -> None:
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self) -> None:
        self.screen.fill('black')
        self.map.draw()

    def check_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self) -> None:
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()