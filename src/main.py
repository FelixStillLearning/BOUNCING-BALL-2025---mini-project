print("Welcome to the Bouncing Ball Game!")
import pygame
from game.game import Game

def main():
    pygame.init()
    pygame.mixer.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()