import pygame as pg
from os import system
from entity.snake import Snake
from entity.apple import Apple

system("clear")
system("python --version")
print("Pygame version:", pg.__version__)

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("My Game")

snake = Snake(screen)
apple = Apple(screen)

running = True

while running:
    screen.fill((55, 70, 80))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    snake.render()
    apple.render()

    pg.display.flip()
    pg.display.update()
