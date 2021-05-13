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
        self.speed = randint(1, 4)

    def update(self, *args):
        if self.rect.x < args[0]:
            self.rect.x += self.speed
        else:
            self.rect.x = 0

class Meteor(pg.sprite.Sprite):
    def __init__(self, x, y, speed, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self, *args):
        if self.rect.x > 0:
            self.rect.x -= self.speed
            self.rect.y += self.speed - 3
        else:
            self.rect.x = args[0]
            self.rect.y = 50
