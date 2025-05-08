import pygame
import sys

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

mainfont = pygame.font.SysFont('Courier New', 35, bold=True)
initfont = pygame.font.SysFont('Courier New', 80)


class Buttons:
    def __init__(self, rect, color, hover_color, text, txtcol, txthov) -> None:
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.txtcol = txtcol
        self.txthov = txthov
        self.font = mainfont

    def draw(self, screen) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):

            current_color = self.hover_color
            current_txt_color = self.txthov
        
        else: 
            current_color = self.color
            current_txt_color = self.txtcol

        pygame.draw.rect(screen, current_color, self.rect)

        if self.text:
            text_surf = self.font.render(self.text, True, current_txt_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)

    def is_clicked(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
    



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
