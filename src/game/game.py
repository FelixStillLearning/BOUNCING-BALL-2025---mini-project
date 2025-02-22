import pygame

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bouncing Ball Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.ball = None
        self.paddle = None
        self.bounce_sound = None

    def initialize(self):
        from .ball import Ball
        from .paddle import Paddle
        self.ball = Ball(self.width // 2, self.height // 2, 10, 5, 5)  # Adjusted values for radius, velocity_x, and velocity_y
        self.paddle = Paddle(self.width // 2 - 50, self.height - 30)
        self.bounce_sound = pygame.mixer.Sound("assets/sounds/bounce.wav")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Update paddle position based on mouse movement
        mouse_x, _ = pygame.mouse.get_pos()
        self.paddle.x = mouse_x - self.paddle.width // 2

    def update(self):
        self.ball.move()
        if self.ball.bounce(self.paddle):
            self.bounce_sound.play()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.ball.draw(self.screen)
        self.paddle.draw(self.screen)
        pygame.display.flip()

    def game_over(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(text, (self.width // 2 - 150, self.height // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(2000)

        font = pygame.font.Font(None, 36)
        text = font.render("Press R to Retry or Q to Quit", True, (255, 255, 255))
        self.screen.blit(text, (self.width // 2 - 200, self.height // 2 + 50))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.initialize()
                        waiting = False
                    if event.key == pygame.K_q:
                        self.running = False
                        waiting = False

    def run(self):
        pygame.init()
        pygame.mixer.init()
        self.initialize()
        pygame.mouse.set_visible(False)  # Hide the mouse cursor
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            if self.ball.y > self.height:  # Example condition for game over
                self.game_over()
            self.clock.tick(60)  # Ensure the game runs at 60 frames per second
        pygame.mouse.set_visible(True)  # Show the mouse cursor again
        pygame.quit()