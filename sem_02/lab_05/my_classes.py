import pygame as pg
from random import *
from math import *

class Rocket(pg.sprite.Sprite):
    def __init__(self, x, y, speed, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self, *args):
        if self.rect.y > -250:
            self.rect.y -= self.speed
        else:
            self.rect.y = args[0]

class Star(pg.sprite.Sprite):
    def __init__(self, x, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = randint(2, 5)

    def update(self, *args):
        if self.rect.x < args[0]:
            self.rect.x += self.speed
        else:
            self.rect.x = 0

class Saturn(pg.sprite.Sprite):
    def __init__(self, x, y, t, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.t = t

    def update(self, *args):
        self.rect.x = args[0] + 25 * cos(self.t)
        self.rect.y = args[1] + 25 * sin(self.t)
        self.t += 0.05
