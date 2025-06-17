import pygame
import sys
from inventory import items
import uielements as ui_
from typing import List
from objects import Product
from random import randint
from employees import get_candidates


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

cBg = 0

GAIN = pygame.USEREVENT + 1
EXPENSE = pygame.USEREVENT + 2
FINE = pygame.USEREVENT + 3

EDITOR = False
CNAME_TOGGLE = False
CAN_SELECT = False
PNAME_TOGGLE = False
INSUFFICIENT_EMPLOYEES = True
STAFF_MANAGING = False
UPGRADE_OFFICE = False
DEVELOP_BRANCHES = False
HIRING_ERROR = False
FRAUD_DETECTED = False

player_name = ""
income = 0
staff =  []
staff_limit = 1
candidates = get_candidates()

buffer = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

pBuffer = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

office_params = {500000: 5,
                1200000: 10,
                2880000: 24}

curr_price = 500000

products = []

staff_ind = 0
tab_ind = 0
currBtns = []
info = {}

rent = 30000
expenses = 0

tabnames = ["monitors", "mice", "mousepads", "keyboards", "webcameras"]

pygame.time.set_timer(GAIN, 10000)
pygame.time.set_timer(EXPENSE, 30000)
pygame.time.set_timer(FINE, randint(1000, 2000))

startBg = pygame.image.load("sources/Bgs/startbg.png")
blurBg = pygame.image.load("sources/Bgs/blurred.png")
mainScenesBg = [pygame.image.load("sources/Bgs/startoffice.png"),
                pygame.image.load("sources/Bgs/gamescene.png"),
                pygame.image.load("sources/Bgs/mediumoffice.png")]
editorBg = pygame.image.load("sources/Bgs/editorbg.png")

#Miniatures
miniUpg1 = [pygame.image.load("sources/Miniatures/gamescene1.png"),
            pygame.image.load("sources/Miniatures/mediumoffice1.png"),
            pygame.image.load("sources/Miniatures/sold.png"),]


resumeIcon = pygame.image.load("sources/Sprites/resume.png")
monitorDummy = pygame.image.load("sources/Sprites/monitordummy.png")
mouseDummy = pygame.image.load("sources/Sprites/mousedummy.png")
wcamDummy = pygame.image.load("sources/Sprites/webcameradummy.png")
mousepadDummy = pygame.image.load("sources/Sprites/mousepaddummy.png")
keyboardDummy = pygame.image.load("sources/Sprites/keyboarddummy.png")

dummies = [monitorDummy, mouseDummy, mousepadDummy, keyboardDummy, wcamDummy]

colours = [
    (192, 182, 166), #main menu bg
    (227, 206, 150), #beige
    (139, 141, 135) #locker gray
]

initfont = pygame.font.SysFont('Courier New', 80)
mainfont = pygame.font.SysFont('Courier New', 35, bold=True)
mainfont2 = pygame.font.SysFont('Courier New', 30)
smallmainfont = pygame.font.SysFont('Courier New', 20)
tinyfont = pygame.font.SysFont('Courier New', 18)

budget: float = 1_000_000_000.0
number_of_employees: int = len(staff) + 1


# Set the frame rate
clock = pygame.time.Clock()



# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
        ui_.backBtn.is_clicked(event=event)

        if event.type == pygame.USEREVENT and event.button == ui_.backBtn and GAME_SCENE >= 1:
            if STAFF_MANAGING:
                STAFF_MANAGING = False
                HIRING_ERROR = False
            elif UPGRADE_OFFICE:
                UPGRADE_OFFICE = False
            elif DEVELOP_BRANCHES:
                DEVELOP_BRANCHES = False
            else:
                GAME_SCENE -= 1
        
        
        if GAME_SCENE == 0:
            ui_.playBtn.is_clicked(event=event)
            ui_.quitBtn.is_clicked(event=event)

            if event.type == pygame.USEREVENT and event.button == ui_.quitBtn:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.USEREVENT and event.button == ui_.playBtn:
                GAME_SCENE = 1
        
        if GAME_SCENE == 1:
            ui_.nameInput.is_clicked(event=event)

            if event.type == pygame.USEREVENT and event.button == ui_.nameInput:
                player_name = ui_.nameInput.nameVar
                GAME_SCENE = 2

        if GAME_SCENE == 2:
            ui_.companyNameInput.is_clicked(event=event)

            if CNAME_TOGGLE and (not(STAFF_MANAGING)): 
                ui_.editorBtn.is_clicked(event=event)
                ui_.hireBtn.is_clicked(event=event)
                ui_.upgradeBtn.is_clicked(event=event)
                ui_.branchesBtn.is_clicked(event=event)
                ui_.taxfraudBtn.is_clicked(event=event)

            if STAFF_MANAGING:
                ui_.lLeftBtn.is_clicked(event=event)
                ui_.lRightBtn.is_clicked(event=event)

                if candidates[staff_ind]["Статус"]:
                    ui_.fireBtn.is_clicked(event=event)
                
                else:
                    ui_.unfireBtn.is_clicked(event=event)
                
            elif UPGRADE_OFFICE and cBg < 2:
                ui_.procUpgBtn.is_clicked(event=event)


            if event.type == pygame.USEREVENT and event.button == ui_.companyNameInput and not CNAME_TOGGLE:
                CNAME_TOGGLE = True

            if event.type == pygame.USEREVENT and event.button == ui_.editorBtn and not STAFF_MANAGING:
                GAME_SCENE = 3
                INSUFFICIENT_EMPLOYEES = False if number_of_employees >= 3 else True
        
            if event.type == pygame.USEREVENT and event.button == ui_.hireBtn:
                STAFF_MANAGING = True
            
            if event.type == pygame.USEREVENT and event.button == ui_.branchesBtn:
                DEVELOP_BRANCHES = True
            
            if event.type == pygame.USEREVENT and event.button == ui_.upgradeBtn:
                UPGRADE_OFFICE = True
            
            if event.type == pygame.USEREVENT and event.button == ui_.lLeftBtn and staff_ind >= 1:
                staff_ind -= 1
                HIRING_ERROR = False
            
            if event.type == pygame.USEREVENT and event.button == ui_.lRightBtn and staff_ind < len(candidates) - 1:
                staff_ind += 1
                HIRING_ERROR = False
            
            if event.type == pygame.USEREVENT and event.button == ui_.procUpgBtn:
                if budget >= curr_price:
                    budget -= curr_price
                    cBg = cBg + 1
                    staff_limit = office_params[curr_price]
                    curr_price = int(curr_price*2.4)

            if event.type == pygame.USEREVENT and event.button == ui_.taxfraudBtn:
                FRAUD_DETECTED = True
                pass


            if event.type == FINE and FRAUD_DETECTED:
                fine_ = randint(80000, budget-1000) if budget > 81000 else budget
                budget -= fine_
                t = randint(0, 1)
                FRAUD_DETECTED = True if t else False
                
            if event.type == GAIN and products != []:
                budget += profit(products)
            
            if event.type == EXPENSE:
                budget -= (expenses + rent)
            
            if event.type == pygame.USEREVENT and event.button == ui_.fireBtn:
                HIRING_ERROR = False
                expenses -= candidates[staff_ind]["Требуемая З/П"]
                candidates[staff_ind]["Статус"] = False
                staff.remove(candidates[staff_ind])
                
                if len(candidates) >= 2:
                    if staff_ind >= len(candidates) - 1: 
                        staff_ind -= 1
                        candidates.remove(candidates[staff_ind+1])

                    else:
                        candidates.remove(candidates[staff_ind])
                
                number_of_employees -= 1
                
            
            if event.type == pygame.USEREVENT and event.button == ui_.unfireBtn:
                if number_of_employees + 1 > staff_limit:
                    HIRING_ERROR = True
                else:
                    expenses += candidates[staff_ind]["Требуемая З/П"]
                    candidates[staff_ind]["Статус"] = True
                    staff.append(candidates[staff_ind])
                    number_of_employees += 1
            
        
        if GAME_SCENE == 3:
            ui_.swipeLeftBtn.is_clicked(event=event)
            ui_.swipeRightBtn.is_clicked(event=event)
            ui_.createBtn.is_clicked(event=event)

            if event.type == pygame.USEREVENT and event.button == ui_.swipeLeftBtn and tab_ind >= 1 and GAME_SCENE == 3:
                tab_ind -= 1
                currBtns = unfold(items[tabnames[tab_ind]], dummies[tab_ind], 0)
                btns = ui_.form_buttons(currBtns)

                CAN_SELECT = False
                info = {}
            
            if event.type == pygame.USEREVENT and event.button == ui_.swipeRightBtn and tab_ind <= 3 and GAME_SCENE == 3:
                tab_ind += 1
                currBtns = unfold(items[tabnames[tab_ind]], dummies[tab_ind], 0)
                btns = ui_.form_buttons(currBtns)

                CAN_SELECT = False
                info = {}
            
            if event.type == pygame.USEREVENT and event.button == ui_.createBtn and EDITOR == False:
                EDITOR = True
                currBtns = unfold(items["monitors"], monitorDummy, 0)
                btns = ui_.form_buttons(currBtns)

            if EDITOR == True:
                for i in btns: i.is_clicked(event=event)
                ui_.selectBtn.is_clicked(event=event)
                ui_.finishBtn.is_clicked(event=event)
                ui_.productNameInput.is_clicked(event=event)
                
                if event.type == pygame.USEREVENT:

                    for i in range(len(btns)):
                        if event.button == btns[i]:
                            info = items[tabnames[tab_ind]][i].info() #TODO: Change print to real actions
                            CAN_SELECT = True
                        
                    if event.button == ui_.selectBtn and CAN_SELECT:
                        buffer[tab_ind] = info["income"]
                        pBuffer[tab_ind] = info["price"]
                    
                    if event.button == ui_.finishBtn and all([i!=0 for i in buffer.values()]) != 0:
                        PNAME_TOGGLE = True
                        
                    if PNAME_TOGGLE:

                        if event.button == ui_.productNameInput:
                            prLabel = ui_.productNameInput.nameVar
                            if prLabel is not None:
                                products.append(Product(prLabel, 
                                                        sum([i for i in buffer.values()]),
                                                        sum([i for i in pBuffer.values()]),
                                                        randint(10, 120)))
                                EDITOR = False
                                PNAME_TOGGLE = False
                                GAME_SCENE = 2

            


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
        

        if not(CNAME_TOGGLE):
            tint = pygame.Surface((1080, 720))
            tint.set_alpha(200)
            tint.fill((0, 0, 0))
            screen.blit(tint, (0, 0))

            ui_.companyNameInput.draw(screen)
        
        if CNAME_TOGGLE:
            
            screen.blit(mainScenesBg[cBg], (0, 0))

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

            office = mainfont.render(f"Основной офис", True, (255, 244, 244))
            officeRect = office.get_rect(center=(365, 25))
            screen.blit(office, officeRect)

            cEmp = smallmainfont.render(f"Штат сотрудников: {number_of_employees}", True, (255, 244, 244))
            cEmpRect = cEmp.get_rect(topleft=(screen_width-340, 90))
            screen.blit(cEmp, cEmpRect)

            eDisp = smallmainfont.render(f"Расходы в месяц: {expenses + rent}", True, (255, 244, 244))
            eDispRect = eDisp.get_rect(topleft=(screen_width-340, 130))
            screen.blit(eDisp, eDispRect)

            emLimit = smallmainfont.render(f"Макс. сотрудников: {staff_limit}", True, (255, 244, 244))
            emLimitRect = emLimit.get_rect(topleft=(screen_width-340, 170))
            screen.blit(emLimit, emLimitRect)

            ui_.editorBtn.draw(screen)
            ui_.branchesBtn.draw(screen)
            ui_.hireBtn.draw(screen)
            ui_.upgradeBtn.draw(screen)
            ui_.taxfraudBtn.draw(screen)

            if STAFF_MANAGING or DEVELOP_BRANCHES or UPGRADE_OFFICE:
                
                tint = pygame.Surface((1080, 720))
                tint.set_alpha(204)
                tint.fill((0, 0, 0))
                screen.blit(tint, (0, 0))

                stafftab = pygame.Surface((720, 476))
                stafftab.fill((150, 176, 177))
                screen.blit(stafftab, (180, 119))

                if STAFF_MANAGING:

                    cnd_info = mainfont2.render(f"Штат сотрудников: {number_of_employees}", True, (255, 244, 244))
                    cnd_rect = cnd_info.get_rect(topleft=(250, 409))
                    screen.blit(cnd_info, cnd_rect)

                    ui_.lLeftBtn.draw(screen)
                    ui_.lRightBtn.draw(screen)

                    screen.blit(resumeIcon, (250, 139))

                    if len(candidates) > 0:
                        c = 0

                        for key_, val_ in candidates[staff_ind].items():
                            txt = f"{key_}: {val_}" if key_ != "Статус" else f"{key_}: {'Нанят' if val_ else 'Не нанят'}"
                            cnd_info = smallmainfont.render(txt, True, (255, 244, 244))
                            cnd_rect = cnd_info.get_rect(topleft=(500, 139+(25*c)))
                            screen.blit(cnd_info, cnd_rect)
                            c += 1
                        
                        if candidates[staff_ind]["Статус"]:
                            ui_.fireBtn.draw(screen)
                        
                        else:
                            ui_.unfireBtn.draw(screen)
                        
                        if HIRING_ERROR:
                            cnd_info = mainfont2.render(f"Перебор", True, (255, 244, 244))
                            cnd_rect = cnd_info.get_rect(topleft=(250, 449))
                            screen.blit(cnd_info, cnd_rect)

                    
                elif UPGRADE_OFFICE:

                    if cBg <= 1:
                        price = mainfont2.render(f"Цена: {curr_price}", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 450))
                        screen.blit(price, price_rect)

                        price = smallmainfont.render(f"Вместимость: {office_params[curr_price]} сотрудников", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 420))
                        screen.blit(price, price_rect)
                    
                    else:
                        price = mainfont2.render(f"Достигнут макс. уровень", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 450))
                        screen.blit(price, price_rect)

                        price = smallmainfont.render(f"Финал DEMO", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 420))
                        screen.blit(price, price_rect)

                    screen.blit(miniUpg1[cBg], (389, 100))

                    ui_.procUpgBtn.draw(screen)
                    pass

                elif DEVELOP_BRANCHES:

                    pass


        
        ui_.backBtn.draw(screen)
    
    if GAME_SCENE == 3:

        screen.blit(editorBg, (0, 0))

        if INSUFFICIENT_EMPLOYEES:
            tint = pygame.Surface((1080, 720))
            tint.set_alpha(204)
            tint.fill((0, 0, 0))
            screen.blit(tint, (0, 0))

            log1 = smallmainfont.render("Штат сотрудников должен быть от 3-х человек", True, (255, 244, 244))
            log1_rect = log1.get_rect(center=(540, 360))
            screen.blit(log1, log1_rect)
        
        else:
            
            for r, p in [[(350, 720), (730, 0)], [(730, 100), (0, 620)]]:
                tint = pygame.Surface(r)
                tint.set_alpha(184 + 50*(p[1]!=0))
                tint.fill((0, 0, 0))
                screen.blit(tint, p)
            
            ui_.createBtn.draw(screen)

            if EDITOR == True:

                ui_.swipeLeftBtn.draw(screen)
                ui_.swipeRightBtn.draw(screen)
                ui_.selectBtn.draw(screen)
                ui_.finishBtn.draw(screen)
                
                tab = pygame.Surface((270, 30))
                tab.fill(ui_.colours[3])
                screen.blit(tab, (770, 30))

                temp = ""

                match tab_ind:
                    case 0:
                        temp = "Монитор"
                        unfold(items["monitors"], monitorDummy, 1)
                        pass
                    case 1:
                        temp = "Мышь"
                        unfold(items["mice"], mouseDummy, 1)
                        pass
                    case 2:
                        temp = "Коврик"
                        unfold(items["mousepads"], mousepadDummy, 1)
                        pass
                    case 3:
                        temp = "Клавиатура"
                        unfold(items["keyboards"], keyboardDummy, 1)
                        pass
                    case 4:
                        temp = "Веб-камера"
                        unfold(items["webcameras"], wcamDummy, 1)
                        pass
                
                for i in btns: i.draw(screen)
                
                tab_text = smallmainfont.render(temp, True, (255, 244, 244))
                tab_rect = tab_text.get_rect(center=(905, 45))
                screen.blit(tab_text, tab_rect)

                info_label = smallmainfont.render("Хар-ки:", True, (255, 244, 244))
                info_label_rect = info_label.get_rect(topleft=(750, 560))
                screen.blit(info_label, info_label_rect)
                
                if info != []:
                    c = 0

                    for key_, val_ in info.items():
                        itmp = tinyfont.render(f"{key_}: {val_}", True, (255, 244, 244))
                        itmpr = itmp.get_rect(topleft=(750, 600+(18*c)))
                        screen.blit(itmp, itmpr)
                        c += 1

                if PNAME_TOGGLE:
                    
                    ui_.productNameInput.draw(screen)
        ui_.backBtn.draw(screen)
    

    
    def unfold(item, sprite, mode):
        initX = 760
        initY = 60

        toggle = False
        shiftX = 170
        shiftY = 150

        tRects = []

        if item != []:
            if mode: screen.blit(sprite, (initX, initY)) 
            temp_ = smallmainfont.render(item[0].info()["model"], True, (255, 244, 244))
            tempR = temp_.get_rect(topleft=(initX-10, initY+120))
            tRects.append(tempR)

            if mode:
                screen.blit(temp_, tempR)
            
            for i in item[1:]:
                if not toggle:
                    initX += shiftX
                    if mode: screen.blit(sprite, (initX, initY))
                    toggle = True
                else:
                    initX -= shiftX
                    initY += shiftY
                    if mode: screen.blit(sprite, (initX, initY))
                    toggle = False
                    
                temp_ = smallmainfont.render(i.info()["model"], True, (255, 244, 244))
                tempR = temp_.get_rect(topleft=(initX-10, initY+120))
                if mode: screen.blit(temp_, tempR)

                tRects.append(tempR)
            if not mode:
                return tRects
    
    def profit(products: List[Product]) -> int: #Change in budget

        decline = 0
            
        for el in products:
            tmp = el.info()

            decline += randint(tmp["total income"] - randint(100, 1000),
                                tmp["total income"] + randint(100, 1000)) * tmp["amount"]
                
        
            decline -= randint(tmp["total price"] - randint(100, 400),
                                tmp["total price"] + randint(1000, 1200)) * tmp["amount"]
                
        return decline


    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)


