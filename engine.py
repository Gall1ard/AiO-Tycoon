import pygame
import sys
from objects import Buttons, InputBox
from inventory import items

# Initialize PyGame
pygame.init()

# Set up the game window
screen_width = 1080
screen_height = 720
gameicon = pygame.image.load("sources/icon.png")
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_icon(gameicon)
pygame.display.set_caption("AiO-Tycoon")

GAME_SCENE = 2 #Start scene is 0. If it's not then it's for testing purposes
'''
0 - Main menu screen
1 - Login/Register screen (pops up if the player wasn't logged in)
2 - Main game scene
3 - Device constructor scene
'''

#EDITOR_TOGGLE = False
CNAME_TOGGLE = False

player_name = ""

startBg = pygame.image.load("sources/Bgs/startbg.png")
blurBg = pygame.image.load("sources/Bgs/blurred.png")
mainSceneBg = pygame.image.load("sources/Bgs/gamescene.png")
editorBg = pygame.image.load("sources/Bgs/editorbg.png")

colours = [
    (192, 182, 166), #main menu bg
    (227, 206, 150), #beige
    (139, 141, 135) #locker gray
]

initfont = pygame.font.SysFont('Courier New', 80)
mainfont = pygame.font.SysFont('Courier New', 35, bold=True)
mainfont2 = pygame.font.SysFont('Courier New', 30)
smallmainfont = pygame.font.SysFont('Courier New', 20)

budget: float = 1_000_000.0
number_of_employees: int = 3


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

editorBtn = Buttons(rect=(740, 150, 120, 40),
                    color=colours[0],
                    hover_color=colours[0],
                    text="Создать +",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

nameInput = InputBox(
    rect=(340, 260, 400, 50),
    font=smallmainfont,
    text="Имя (от 3-х до 20-и символов)"
)

companyNameInput = InputBox(
    rect=(340, 260, 400, 50),
    font=smallmainfont,
    text="Название фирмы"
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
        companyNameInput.is_clicked(event=event)
        editorBtn.is_clicked(event=event)

        if event.type == pygame.USEREVENT and event.button == quitBtn:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.USEREVENT and event.button == playBtn:
            GAME_SCENE = 1
        
        if event.type == pygame.USEREVENT and event.button == backBtn:
            GAME_SCENE = 0

        if event.type == pygame.USEREVENT and event.button == nameInput:
            player_name = nameInput.nameVar
            GAME_SCENE = 2
        
        if event.type == pygame.USEREVENT and event.button == nameInput:
            CNAME_TOGGLE = True

        if event.type == pygame.USEREVENT and event.button == editorBtn:
            GAME_SCENE = 3
            pass


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

        t2_font = mainfont2.render("Неверный псевдоним", True, (255, 244, 244))
        t2_rect = t2_font.get_rect(center=(screen_width//2, 600))
        screen.blit(t2_font, t2_rect)

        nameInput.draw(screen)
        backBtn.draw(screen)

    if GAME_SCENE == 2:
        screen.fill((169, 195, 196))
        screen.blit(mainSceneBg, (0, 0))

        if not(CNAME_TOGGLE):
            tint = pygame.Surface((1080, 720))
            tint.set_alpha(200)
            tint.fill((0, 0, 0))
            screen.blit(tint, (0, 0))

            companyNameInput.draw(screen)
        
        if CNAME_TOGGLE:

            tint = pygame.Surface((350, 720))
            tint.set_alpha(204)
            tint.fill((0, 0, 0))
            screen.blit(tint, (730, 0))

            cName = smallmainfont.render(f"Фижма: {companyNameInput.nameVar}", True, (255, 244, 244))
            cNameRect = cName.get_rect(topleft=(screen_width-340, 10))
            screen.blit(cName, cNameRect)

            cBudget = smallmainfont.render(f"Бюджет: {budget}", True, (255, 244, 244))
            cBudgetRect = cBudget.get_rect(topleft=(screen_width-340, 50))
            screen.blit(cBudget, cBudgetRect)

            office = mainfont.render(f"Ваш офис", True, (255, 244, 244))
            officeRect = office.get_rect(center=(365, 25))
            screen.blit(office, officeRect)

            cEmp = smallmainfont.render(f"Штат сотрудников: {number_of_employees}", True, (255, 244, 244))
            cEmpRect = cEmp.get_rect(topleft=(screen_width-340, 90))
            screen.blit(cEmp, cEmpRect)

            editorBtn.draw(screen)
    
    if GAME_SCENE == 3:

        screen.fill((169, 195, 196))
        screen.blit(editorBg, (0, 0))

        tint = pygame.Surface((1080, 720))
        tint.set_alpha(100)
        tint.fill((0, 0, 0))
        screen.blit(tint, (0, 0))




    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
