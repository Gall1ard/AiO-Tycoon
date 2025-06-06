import pygame
import sys
from inventory import items
import uielements as ui_

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

tab_ind = 0

startBg = pygame.image.load("sources/Bgs/startbg.png")
blurBg = pygame.image.load("sources/Bgs/blurred.png")
mainSceneBg = pygame.image.load("sources/Bgs/gamescene.png")
editorBg = pygame.image.load("sources/Bgs/editorbg.png")

monitorDummy = pygame.image.load("sources/Sprites/monitordummy.png")
mouseDummy = pygame.image.load("sources/Sprites/mousedummy.png")
wcamDummy = pygame.image.load("sources/Sprites/webcameradummy.png")
mousepadDummy = pygame.image.load("sources/Sprites/mousepaddummy.png")
keyboardDummy = pygame.image.load("sources/Sprites/keyboarddummy.png")

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



# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        ui_.playBtn.is_clicked(event=event)
        ui_.quitBtn.is_clicked(event=event)
        ui_.backBtn.is_clicked(event=event)
        ui_.nameInput.is_clicked(event=event)
        ui_.companyNameInput.is_clicked(event=event)
        ui_.editorBtn.is_clicked(event=event)
        ui_.swipeLeftBtn.is_clicked(event=event)
        ui_.swipeRightBtn.is_clicked(event=event)

        if event.type == pygame.USEREVENT and event.button == ui_.quitBtn:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.USEREVENT and event.button == ui_.playBtn:
            GAME_SCENE = 1
        
        if event.type == pygame.USEREVENT and event.button == ui_.backBtn:
            GAME_SCENE -= 1

        if event.type == pygame.USEREVENT and event.button == ui_.nameInput:
            player_name = ui_.nameInput.nameVar
            GAME_SCENE = 2
        
        if event.type == pygame.USEREVENT and event.button == ui_.nameInput:
            CNAME_TOGGLE = True

        if event.type == pygame.USEREVENT and event.button == ui_.editorBtn:
            GAME_SCENE = 3
            pass
            
        if event.type == pygame.USEREVENT and event.button == ui_.swipeLeftBtn and tab_ind >= 1:
            tab_ind -= 1
        
        if event.type == pygame.USEREVENT and event.button == ui_.swipeRightBtn and tab_ind <= 3:
            tab_ind += 1


    #Scene management

    if GAME_SCENE == 0:
        # Background, title and buttons
        screen.fill((192, 182, 166))
        screen.blit(startBg, (-100, 0))

        title_font = initfont.render("AiO Tycoon", True, (255, 255, 255))
        title_rect = title_font.get_rect(center=(screen_width//2, 50))
        screen.blit(title_font, title_rect)

        ui_.playBtn.draw(screen)
        ui_.quitBtn.draw(screen)
    
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

        ui_.nameInput.draw(screen)
        ui_.backBtn.draw(screen)

    if GAME_SCENE == 2:
        screen.fill((169, 195, 196))
        screen.blit(mainSceneBg, (0, 0))
        

        if not(CNAME_TOGGLE):
            tint = pygame.Surface((1080, 720))
            tint.set_alpha(200)
            tint.fill((0, 0, 0))
            screen.blit(tint, (0, 0))

            ui_.companyNameInput.draw(screen)
        
        if CNAME_TOGGLE:

            tint = pygame.Surface((350, 720))
            tint.set_alpha(204)
            tint.fill((0, 0, 0))
            screen.blit(tint, (730, 0))

            cName = smallmainfont.render(f"Фижма: {ui_.companyNameInput.nameVar}", True, (255, 244, 244))
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

            ui_.editorBtn.draw(screen)
        
        ui_.backBtn.draw(screen)
    
    if GAME_SCENE == 3:

        screen.fill((169, 195, 196))
        screen.blit(editorBg, (0, 0))

        tint = pygame.Surface((350, 720))
        tint.set_alpha(184)
        tint.fill((0, 0, 0))
        screen.blit(tint, (730, 0))

        ui_.swipeLeftBtn.draw(screen)
        ui_.swipeRightBtn.draw(screen)
        ui_.backBtn.draw(screen)

        tab = pygame.Surface((270, 30))
        tab.fill(ui_.colours[3])
        screen.blit(tab, (770, 30))


        temp = ""

        match tab_ind:
            case 0:
                temp = "Монитор"
                unfold(items["monitors"], monitorDummy)
                pass
            case 1:
                temp = "Мышь"
                unfold(items["mice"], mouseDummy)
                pass
            case 2:
                temp = "Коврик"
                unfold(items["mousepads"], mousepadDummy)
                pass
            case 3:
                temp = "Клавиатура"
                unfold(items["keyboards"], keyboardDummy)
                pass
            case 4:
                temp = "Веб-камера"
                unfold(items["webcameras"], wcamDummy)
                pass
        
        tab_text = smallmainfont.render(temp, True, (255, 244, 244))
        tab_rect = tab_text.get_rect(center=(905, 45))
        screen.blit(tab_text, tab_rect)

    
    def unfold(item, sprite):
        initX = 760
        initY = 60

        toggle = False
        shiftX = 170
        shiftY = 150

        if item != []:
            screen.blit(sprite, (initX, initY)) 
            temp_ = smallmainfont.render(item[0].info()["model"], True, (255, 244, 244))
            tempR = temp_.get_rect(topleft=(initX-10, initY+120))
            screen.blit(temp_, tempR)
        
            for i in item[1:]:
                if not toggle:
                    initX += shiftX
                    screen.blit(sprite, (initX, initY))
                    toggle = True
                else:
                    initX -= shiftX
                    initY += shiftY
                    screen.blit(sprite, (initX, initY))
                    toggle = False
                
                temp_ = smallmainfont.render(i.info()["model"], True, (255, 244, 244))
                tempR = temp_.get_rect(topleft=(initX-10, initY+120))
                screen.blit(temp_, tempR)


    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)


