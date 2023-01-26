import pygame as pg
from random import randint


class Apple:
    apple_x = apple_y = 0
    __size = 12

    def __init__(self, screen):
        self.screen = screen
        self.apple_x = randint(1, 750)
        self.apple_y = randint(1, 550)

    def render(self):
        color = (235, 69, 95)
        # Apple.set_apple(self)
        pg.draw.circle(self.screen, color, (self.apple_x,
                       self.apple_y), self.__size)

    @staticmethod
    def set_apple(self):
        self.apple_x = randint(1, 750)
        self.apple_y = randint(1, 550)
