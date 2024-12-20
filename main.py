__author__ = "Ido Senn and the Roip team"

import sys

from settings import *
import sys


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption(WINDOW_CAPTION)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=BG_COLOR)
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()