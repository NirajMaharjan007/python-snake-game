from entity.snake import Snake
from entity.apple import Apple


class Logic:

    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake(self.screen)
        self.apple = Apple(self.screen)

    def render(self):
        self.snake.render()
        # self.apple.render()
