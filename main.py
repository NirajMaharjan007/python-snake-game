import pygame as pg
from os import system
from logic import Logic

system("clear")
system("python --version")
print("Pygame version:", pg.__version__)

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("My Game")

running = True

logic = Logic(screen)

while running:
    screen.fill((55, 70, 80))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    logic.render()
    pg.display.flip()
    pg.display.update()
