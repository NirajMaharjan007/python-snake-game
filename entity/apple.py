import pygame as pg
from random import randint


class Apple:
    __apple_x = __apple_y = 0
    __size = 12

    def __init__(self, screen):
        self.screen = screen
        self.__apple_y = randint(1, 800)
        self.__apple_x = randint(1, 600)

    def render(self):
        color = (235, 69, 95)
        pg.draw.circle(self.screen, color, (self.__apple_x,
                       self.__apple_y), self.__size)

    @staticmethod
    def get_x(self):
        return self.__apple_x

    @staticmethod
    def get_y(self):
        return self.__apple_y
