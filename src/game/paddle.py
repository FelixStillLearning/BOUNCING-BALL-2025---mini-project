import pygame

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 10
        self.velocity = 10

    def move_left(self):
        self.x -= self.velocity
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.velocity
        if self.x + self.width > 800:  # Assuming the screen width is 800
            self.x = 800 - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))