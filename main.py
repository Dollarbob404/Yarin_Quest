__author__ = "Ido Senn"

import pygame

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


def flip_sprites(sprites):
    return [pg.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pg.Surface((width, height), pg.SRCALPHA, 32)
            rect = pg.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pg.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip_sprites(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


class Player(pg.sprite.Sprite):
    COLOR = (100, 100, 100)
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 50, 50)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "right"
        self.animation_count = 0
        self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def update(self, fps):
        self.y_vel += min(1, self.fall_count / fps) * GRAVITY
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self, win):
        pg.draw.rect(win, self.COLOR, self.rect)


class App:
    def __init__(self):
        pg.display.set_caption(WINDOW_CAPTION)
        self.clock = pg.time.Clock()
        self.bg_tiles, self.bg_img = get_background(BG_IMAGE)
        self.player = Player(100, 100)

    def handle_move(self):
        keys = pg.key.get_pressed()

        self.player.x_vel = 0
        if keys[pygame.K_LEFT]:
            self.player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            self.player.move_right(PLAYER_VEL)

    def update(self):
        self.clock.tick(FPS)
        self.player.update(FPS)

    def draw(self):
        # Draw bg
        for tile in self.bg_tiles:
            WINDOW.blit(self.bg_img, tile)

        self.player.draw(WINDOW)

        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.handle_move()
            self.update()
            self.draw()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
