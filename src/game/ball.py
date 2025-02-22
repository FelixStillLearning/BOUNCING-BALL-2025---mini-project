import pygame

class Ball:
    def __init__(self, x, y, radius, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def bounce(self, paddle):
        bounced = False
        # Check for collision with the paddle
        if (self.y + self.radius >= paddle.y and
            paddle.x <= self.x <= paddle.x + paddle.width):
            self.velocity_y = -self.velocity_y
            bounced = True

        # Check for collision with the screen edges
        if self.x - self.radius <= 0 or self.x + self.radius >= 800:  # Assuming screen width is 800
            self.velocity_x = -self.velocity_x
            bounced = True
        if self.y - self.radius <= 0:
            self.velocity_y = -self.velocity_y
            bounced = True

        return bounced

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)