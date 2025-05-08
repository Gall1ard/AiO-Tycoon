import pygame
import sys
from objects import Buttons, InputBox

# Initialize PyGame
pygame.init()

# Set up the game window
screen_width = 1080
screen_height = 720
gameicon = pygame.image.load("sources/icon.png")
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_icon(gameicon)
pygame.display.set_caption("AiO-Tycoon")

GAME_SCENE = 0

player_name = ""

startBg = pygame.image.load("sources/Bgs/startbg.png")
blurBg = pygame.image.load("sources/Bgs/blurred.png")

colours = [
    (192, 182, 166), #main menu bg
    (227, 206, 150), #beige
    (139, 141, 135) #locker gray
]

initfont = pygame.font.SysFont('Courier New', 80)
mainfont = pygame.font.SysFont('Courier New', 35, bold=True)
smallmainfont = pygame.font.SysFont('Courier New', 20)


# Set the frame rate
clock = pygame.time.Clock()

playBtn = Buttons(rect=(59, 260, 124, 50),
                  color=colours[2],
                  hover_color=colours[2],
                  text="Play",
                  txtcol=(200, 200, 200),
                  txthov=(230, 230, 230),
                  font=mainfont,
                  alpha=0)

quitBtn = Buttons(rect=(59, 365, 124, 50),
                  color=colours[2],
                  hover_color=colours[2],
                  text="Quit",
                  txtcol=(200, 200, 200),
                  txthov=(230, 230, 230),
                  font=mainfont,
                  alpha=0)

backBtn = Buttons(rect=(20, 20, 100, 40),
                  color=colours[2],
                  hover_color=colours[2],
                  text="Back",
                  txtcol=(255, 255, 255),
                  txthov=(230, 230, 230),
                  font=mainfont,
                  alpha=0)

nameInput = InputBox(
    rect=(340, 260, 400, 50),
    font=smallmainfont,
    text="имя (от 3-х до 20-и символов)"
)


# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        playBtn.is_clicked(event=event)
        quitBtn.is_clicked(event=event)
        backBtn.is_clicked(event=event)
        nameInput.is_clicked(event=event)

        if event.type == pygame.USEREVENT and event.button == quitBtn:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.USEREVENT and event.button == playBtn:
            GAME_SCENE = 1
        
        if event.type == pygame.USEREVENT and event.button == backBtn:
            GAME_SCENE = 0


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

        screen.blit(blurBg, (-100, 0))

        tint = pygame.Surface((1080, 720))
        tint.set_alpha(64)
        tint.fill((0, 0, 0))
        screen.blit(tint, (0, 0))

        title_font = initfont.render("AiO Tycoon", True, (255, 255, 255))
        title_rect = title_font.get_rect(center=(screen_width//2, 50))
        screen.blit(title_font, title_rect)

        t1_font = mainfont.render("Введите псевдоним", True, (255, 255, 255))
        t1_rect = t1_font.get_rect(center=(screen_width//2, 170))
        screen.blit(t1_font, t1_rect)

        nameInput.draw(screen)
        backBtn.draw(screen)

        

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
