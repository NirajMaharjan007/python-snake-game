import pygame as pg
import numpy as np


class Snake:
    x = np.array([])
    y = np.array([])
    __size = 30
    __direction = 'r'
    __speed = 0.85

    def __init__(self, screen):
        self.screen = screen

    def __move(self):
        if self.__direction == 'l':
            self.x -= self.__speed

        if self.__direction == 'r':
            self.x += self.__speed

        if self.__direction == 'u':
            self.y -= self.__speed

        if self.__direction == 'd':
            self.y += self.__speed

    def __update(self):
        if self.x > (800):
            self.x = 0

        elif self.x < 0:
            self.x = 800

        elif self.y > 600:
            self.y = 0

        elif self.y < 0:
            self.y = 600

        key = pg.key.get_pressed()

        if key[pg.K_DOWN]:
            if self.__direction != 'u':
                self.__direction = 'd'

        if key[pg.K_UP]:
            if self.__direction != 'd':
                self.__direction = 'u'

        if key[pg.K_LEFT]:
            if self.__direction != 'r':
                self.__direction = 'l'

        if key[pg.K_RIGHT]:
            if self.__direction != 'l':
                self.__direction = 'r'

    def render(self):
        self.__update()
        self.__move()
        pg.draw.rect(self.screen, (150, 200, 0), pg.Rect(
            round(self.x, 2), round(self.y, 2), self.__size, self.__size))
        print(round(self.x, 2), round(self.y, 2))
