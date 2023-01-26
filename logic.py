import pygame as pg
from entity.snake import Snake
from entity.apple import Apple


class Logic:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pg.font.SysFont("", 32)

        global snake, apple
        snake = Snake(self.screen)
        apple = Apple(self.screen)

    def render(self):

        apple.render()
        apple.collision(snake.get_x(), snake.get_y())
        snake.render()

        self.text = self.font.render(str(self.score), True, (255, 255, 255))
        self.screen.blit(self.text, (10, 10))

        if apple.get_collision():
            self.score += 10
