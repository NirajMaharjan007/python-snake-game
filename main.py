import pygame as pg
from os import system
from logic import Logic

system("clear")
print("Pygame version:", pg.__version__)

pg.init()
pg.font.init()

screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

pg.display.set_caption("My Game")

running = True

logic = Logic(screen)

while running:
    clock.tick(200)

    screen.fill((55, 70, 80))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    logic.render()
    pg.display.flip()
    pg.display.update()
