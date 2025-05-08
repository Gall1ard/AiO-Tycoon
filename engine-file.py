import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up the game window
screen_width = 1280
screen_height = 720
gameicon = pygame.image.load("sources\icon.png")
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_icon(gameicon)
pygame.display.set_caption("AiO-Tycoon")

# Set the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (black in this case)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
