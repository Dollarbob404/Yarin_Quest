__author__ = "Ido Senn and the Roip team"
# Used this tutorial by TechWithTim as a base https://www.youtube.com/watch?v=6gLeplbqtqg

from settings import *
import sys
import pygame as pg
import random
import math
import os
from os import listdir
from os.path import isfile, join


pg.init()
WINDOW = pg.display.set_mode(RES)


def get_background(name):
    image = pg.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WINDOW_WIDTH // width + 1):
        for j in range(WINDOW_HEIGHT // height + 1):
            pos = i * width, j * height
            tiles.append(pos)

    return tiles, image


class App:
    def __init__(self):
        pg.display.set_caption(WINDOW_CAPTION)
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(FPS)

    def draw(self):
        WINDOW.fill(color=BG_COLOR)
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
