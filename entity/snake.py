import pygame as pg


class Snake:
    __size = 30
    __direction = 'r'
    __speed = 2
    __snake_position = [100, 50]
    __snake_body = [[150, 50],
                    [90, 50],
                    [80, 50],
                    [70, 50]
                    ]
    # __length = 5

    def __init__(self, screen):
        self.screen = screen

    def __move(self):
        if self.__direction == 'l':
            self.__snake_position[0] -= self.__speed

        if self.__direction == 'r':
            self.__snake_position[0] += self.__speed

        if self.__direction == 'u':
            self.__snake_position[1] -= self.__speed

        if self.__direction == 'd':
            self.__snake_position[1] += self.__speed

        self.__snake_body.insert(0, list(self.__snake_position))

    def __update(self):
        if self.__snake_position[0] > 800:
            self.__snake_position[0] = 0

        elif self.__snake_position[0] < 0:
            self.__snake_position[0] = 800

        elif self.__snake_position[1] > 600:
            self.__snake_position[1] = 0

        elif self.__snake_position[1] < 0:
            self.__snake_position[1] = 600

        key = pg.key.get_pressed()

        if key[pg.K_DOWN] and self.__direction != 'u':
            self.__direction = 'd'

        if key[pg.K_UP] and self.__direction != 'd':
            self.__direction = 'u'

        if key[pg.K_LEFT] and self.__direction != 'r':
            self.__direction = 'l'

        if key[pg.K_RIGHT] and self.__direction != 'l':
            self.__direction = 'r'

    def render(self):
        green_color = (170, 200, 115)
        green_color_two = (205, 235, 145)

        self.__move()
        self.__update()

        for pos in self.__snake_body:
            pg.draw.rect(self.screen, green_color_two,
                         pg.Rect(pos[0], pos[1], self.__size, self.__size))

        pg.draw.rect(self.screen, green_color, pg.Rect(
            self.__snake_position[0], self.__snake_position[1], self.__size, self.__size))
