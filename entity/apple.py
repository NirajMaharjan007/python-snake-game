import pygame as pg
from random import randint


class Apple:
    __size = 10

    def __init__(self, screen):
        self.screen = screen
        self.apple_x = randint(1, 750)
        self.apple_y = randint(1, 550)

    def render(self):
        color = (235, 69, 95)
        pg.draw.circle(self.screen, color, (self.apple_x,
                       self.apple_y), self.__size)

    def collision(self, x, y):
        snake = pg.Rect(x, y, 30, 30)
        apple = pg.Rect(self.apple_x, self.apple_y, 15, 15)

        global collide
        collide = pg.Rect.colliderect(snake, apple)

        if collide:
            self.apple_x = randint(1, 600)
            self.apple_y = randint(1, 500)

    def get_collision(self):
        return collide
