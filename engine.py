import pygame
import sys
from objects import Buttons

# Initialize PyGame
pygame.init()

# Set up the game window
screen_width = 1080
screen_height = 720
gameicon = pygame.image.load("sources\icon.png")
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_icon(gameicon)
pygame.display.set_caption("AiO-Tycoon")

GAME_SCENE = 0

startBg = pygame.image.load("sources\Bgs\startbg.png")

colours = [
    (192, 182, 166),
    (227, 206, 150),
    (139, 141, 135) #locker gray
]

initfont = pygame.font.SysFont('Courier New', 80)


# Set the frame rate
clock = pygame.time.Clock()

playBtn = Buttons(rect=(59, 260, 124, 50),
                  color=colours[2],
                  hover_color=colours[2],
                  text="Play",
                  txtcol=(200, 200, 200),
                  txthov=(230, 230, 230))

quitBtn = Buttons(rect=(59, 365, 124, 50),
                  color=colours[2],
                  hover_color=colours[2],
                  text="Quit",
                  txtcol=(200, 200, 200),
                  txthov=(230, 230, 230))

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        playBtn.is_clicked(event=event)
        quitBtn.is_clicked(event=event)

        if event.type == pygame.USEREVENT and event.button == quitBtn:
            print("!")
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.USEREVENT and event.button == playBtn:
            GAME_SCENE = 1


    #Scene management

    if GAME_SCENE == 0:
        # Background, title and buttons
        screen.fill((192, 182, 166))
        screen.blit(startBg, (-100, 0))

        title_font = initfont.render("AiO Tycoon", True, (255, 255, 255))
        title_rect = title_font.get_rect(center=(screen_width//2, 50))
        screen.blit(title_font, title_rect)

        playBtn.draw(screen)
        quitBtn.draw(screen)
    
    if GAME_SCENE == 1:
        screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
