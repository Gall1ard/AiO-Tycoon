import pygame
import sys
from inventory import items
import uielements as ui_
from objects import Product
from random import randint
from imgsinit import *
from calcs import profit
from displayeditor import unfold
from canvas_handle import func
import cfg


pygame.init()

screen_width = 1080
screen_height = 720
gameicon = pygame.image.load("sources/icon.png")
screen = pygame.display.set_mode((screen_width, screen_height))

music = pygame.mixer.music.load("sources/audio/bgmusic.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1, 0.0)
dragging = False

pygame.display.set_icon(gameicon)
pygame.display.set_caption("AiO-Tycoon")


GAIN = pygame.USEREVENT + 1
EXPENSE = pygame.USEREVENT + 2
FINE = pygame.USEREVENT + 3

pygame.time.set_timer(GAIN, 10000)
pygame.time.set_timer(FINE, randint(1000, 2000))
pygame.time.set_timer(EXPENSE, 30000)



# Set the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        ui_.backBtn.is_clicked(event=event)

        if event.type == pygame.USEREVENT and event.button == ui_.backBtn and cfg.GAME_SCENE != 0:
            if cfg.GAME_SCENE == -1:
                cfg.BANKRUPCY = True
                cfg.GAME_SCENE = 0
            elif cfg.STAFF_MANAGING:
                cfg.STAFF_MANAGING = False
                cfg.HIRING_ERROR = False
            elif cfg.UPGRADE_OFFICE:
                cfg.UPGRADE_OFFICE = False
            elif cfg.DEVELOP_BRANCHES:
                cfg.DEVELOP_BRANCHES = False
            elif cfg.WATCH_PRODUCTS:
                cfg.WATCH_PRODUCTS = False
            elif cfg.player_name != "":
                if cfg.GAME_SCENE == 3:
                    cfg.GAME_SCENE -= 1
                else:
                    cfg.GAME_SCENE -= 2
            else:
                cfg.GAME_SCENE -= 1
        
        
        if cfg.GAME_SCENE == 0:
            ui_.playBtn.is_clicked(event=event)
            ui_.quitBtn.is_clicked(event=event)
            ui_.muteBtn.is_clicked(event=event)

            if event.type == pygame.USEREVENT and event.button == ui_.quitBtn:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if abs(mouse_x - ui_.volume_slider.knob_x) <= ui_.volume_slider.knob_rad\
                      and abs(mouse_y - ui_.volume_slider.slider_y) <= 20:
                    
                    dragging = True
                
            elif event.type == pygame.MOUSEBUTTONUP:

                dragging = False
                    
            
            if event.type == pygame.USEREVENT and event.button == ui_.playBtn:
                if cfg.BANKRUPCY:
                    pass

                cfg.GAME_SCENE = 1 if cfg.player_name == "" else 2
        
        if cfg.GAME_SCENE == 1:
            ui_.nameInput.is_clicked(event=event)

            if event.type == pygame.USEREVENT and event.button == ui_.nameInput:
                cfg.player_name = ui_.nameInput.nameVar
                cfg.INVALID_NAME = False
                cfg.GAME_SCENE = 2
            
            if event.type == pygame.USEREVENT + 4 and event.button == ui_.nameInput:
                cfg.INVALID_NAME = True

        if cfg.GAME_SCENE == 2:
            ui_.companyNameInput.is_clicked(event=event)

            if cfg.CNAME_TOGGLE and (not(cfg.STAFF_MANAGING or cfg.UPGRADE_OFFICE or\
                                         cfg.DEVELOP_BRANCHES or cfg.WATCH_PRODUCTS)):
                ui_.editorBtn.is_clicked(event=event)
                ui_.hireBtn.is_clicked(event=event)
                ui_.upgradeBtn.is_clicked(event=event)
                ui_.branchesBtn.is_clicked(event=event)
                ui_.taxfraudBtn.is_clicked(event=event)
                ui_.watchBtn.is_clicked(event=event)
                ui_.depositBtn.is_clicked(event=event)

            if cfg.STAFF_MANAGING:
                ui_.lLeftBtn.is_clicked(event=event)
                ui_.lRightBtn.is_clicked(event=event)

                if cfg.candidates[cfg.staff_ind]["Статус"]:
                    ui_.fireBtn.is_clicked(event=event)
                
                else:
                    ui_.unfireBtn.is_clicked(event=event)
                
            elif (cfg.UPGRADE_OFFICE and cfg.cBg < 2) or cfg.DEVELOP_BRANCHES:
                ui_.procUpgBtn.is_clicked(event=event)
            
            elif cfg.WATCH_PRODUCTS:
                ui_.lLeftBtn.is_clicked(event=event)
                ui_.lRightBtn.is_clicked(event=event)
            

            if event.type == pygame.USEREVENT and event.button == ui_.depositBtn:
                cfg.GAME_SCENE = -1

            if event.type == pygame.USEREVENT and event.button == ui_.companyNameInput and not cfg.CNAME_TOGGLE:
                cfg.CNAME_TOGGLE = True

            if event.type == pygame.USEREVENT and event.button == ui_.editorBtn and not cfg.STAFF_MANAGING:
                cfg.GAME_SCENE = 3
                cfg.INSUFFICIENT_EMPLOYEES = False if cfg.number_of_employees >= 3 else True
        
            if event.type == pygame.USEREVENT and event.button == ui_.hireBtn:
                cfg.STAFF_MANAGING = True
            
            if event.type == pygame.USEREVENT and event.button == ui_.branchesBtn:
                cfg.DEVELOP_BRANCHES = True
            
            if event.type == pygame.USEREVENT and event.button == ui_.upgradeBtn:
                cfg.UPGRADE_OFFICE = True
            
            if event.type == pygame.USEREVENT and event.button == ui_.watchBtn:
                cfg.WATCH_PRODUCTS = True
            
            if event.type == pygame.USEREVENT and event.button == ui_.lLeftBtn:
                if cfg.STAFF_MANAGING and (not(cfg.WATCH_PRODUCTS))  and cfg.staff_ind >= 1:
                    cfg.staff_ind -= 1
                    cfg.HIRING_ERROR = False
                elif not(cfg.STAFF_MANAGING) and cfg.WATCH_PRODUCTS and cfg.prod_ind >= 1:
                    cfg.prod_ind -= 1
            
            if event.type == pygame.USEREVENT and event.button == ui_.lRightBtn:
                if cfg.STAFF_MANAGING and (not(cfg.WATCH_PRODUCTS)) and cfg.staff_ind < len(cfg.candidates) - 1:
                    cfg.staff_ind += 1
                    cfg.HIRING_ERROR = False
                elif not(cfg.STAFF_MANAGING) and cfg.WATCH_PRODUCTS and cfg.prod_ind < len(cfg.products)-1:
                    cfg.prod_ind += 1
            
            if event.type == pygame.USEREVENT and event.button == ui_.procUpgBtn:
                if cfg.UPGRADE_OFFICE:
                    if cfg.budget >= cfg.curr_price and cfg.staff_limit == cfg.number_of_employees:
                        cfg.budget -= cfg.curr_price
                        cfg.cBg = cfg.cBg + 1
                        cfg.staff_limit = cfg.office_params[cfg.curr_price]
                        cfg.curr_price = int(cfg.curr_price*2.4)

                elif cfg.DEVELOP_BRANCHES:
                    if cfg.budget > 9000000 and cfg.branches <= 5:
                        cfg.budget -= 9000000
                        cfg.adjustment *= 1.75
                        cfg.branches += 1

            if event.type == pygame.USEREVENT and event.button == ui_.taxfraudBtn:
                cfg.FRAUD_DETECTED = True
                pass


            if event.type == FINE and cfg.FRAUD_DETECTED:
                fine_ = randint(80000, cfg.budget-1000) if cfg.budget > 81000 else cfg.budget
                if cfg.budget - fine_ <= 0:
                    cfg.GAME_SCENE = -1
                else:
                    cfg.budget -= fine_
                    t = randint(0, 1)
                    cfg.FRAUD_DETECTED = True if t else False
                
            if event.type == GAIN and cfg.products != []:
                t = cfg.budget + profit(cfg.products, cfg.adjustment)
                if t <= 0:
                    cfg.GAME_SCENE = -1
                cfg.budget = t if t < 999999999999999 else 999999999999999
            
            if event.type == EXPENSE:
                if cfg.budget - (cfg.expenses + cfg.rent) <= 0:
                    cfg.GAME_SCENE = -1
                else:
                    cfg.budget -= (cfg.expenses + cfg.rent)

            
            if event.type == pygame.USEREVENT and event.button == ui_.fireBtn:
                cfg.HIRING_ERROR = False
                cfg.expenses -= cfg.candidates[cfg.staff_ind]["Требуемая З/П"]
                cfg.candidates[cfg.staff_ind]["Статус"] = False
                cfg.staff.remove(cfg.candidates[cfg.staff_ind])
                
                if len(cfg.candidates) >= 2:
                    if cfg.staff_ind >= len(cfg.candidates) - 1: 
                        cfg.staff_ind -= 1
                        cfg.candidates.remove(cfg.candidates[cfg.staff_ind+1])

                    else:
                        cfg.candidates.remove(cfg.candidates[cfg.staff_ind])
                
                cfg.number_of_employees -= 1
                
            
            if event.type == pygame.USEREVENT and event.button == ui_.unfireBtn:
                if cfg.number_of_employees + 1 > cfg.staff_limit:
                    cfg.HIRING_ERROR = True
                else:
                    cfg.expenses += cfg.candidates[cfg.staff_ind]["Требуемая З/П"]
                    cfg.candidates[cfg.staff_ind]["Статус"] = True
                    cfg.staff.append(cfg.candidates[cfg.staff_ind])
                    cfg.number_of_employees += 1
            
        
        if cfg.GAME_SCENE == 3:
            ui_.swipeLeftBtn.is_clicked(event=event)
            ui_.swipeRightBtn.is_clicked(event=event)
            ui_.createBtn.is_clicked(event=event)

            if event.type == pygame.USEREVENT and event.button == ui_.swipeLeftBtn and cfg.tab_ind >= 1 and cfg.GAME_SCENE == 3:
                cfg.tab_ind -= 1
                cfg.currBtns = unfold(items[cfg.tabnames[cfg.tab_ind]], cfg.dummies[cfg.tab_ind], 0)
                btns = ui_.form_buttons(cfg.currBtns)

                cfg.CAN_SELECT = False
                cfg.info = {}
            
            if event.type == pygame.USEREVENT and event.button == ui_.swipeRightBtn and cfg.tab_ind <= 3 and cfg.GAME_SCENE == 3:
                cfg.tab_ind += 1
                cfg.currBtns = unfold(items[cfg.tabnames[cfg.tab_ind]], cfg.dummies[cfg.tab_ind], 0)
                btns = ui_.form_buttons(cfg.currBtns)

                cfg.CAN_SELECT = False
                cfg.info = {}
            
            if event.type == pygame.USEREVENT and event.button == ui_.createBtn and cfg.EDITOR == False:
                cfg.EDITOR = True
                cfg.currBtns = unfold(items["monitors"], monitorDummy, 0)
                btns = ui_.form_buttons(cfg.currBtns)

            if cfg.EDITOR == True:
                for i in btns: i.is_clicked(event=event)
                ui_.selectBtn.is_clicked(event=event)
                ui_.finishBtn.is_clicked(event=event)
                ui_.productNameInput.is_clicked(event=event)
                
                if event.type == pygame.USEREVENT:

                    for i in range(len(btns)):
                        if event.button == btns[i]:
                            cfg.info = items[cfg.tabnames[cfg.tab_ind]][i].info() #TODO: Change print to real actions
                            cfg.CAN_SELECT = True
                        
                    if event.button == ui_.selectBtn and cfg.CAN_SELECT:
                        cfg.buffer[cfg.tab_ind] = cfg.info["income"]
                        cfg.pBuffer[cfg.tab_ind] = cfg.info["price"]
                        cfg.curr_product[cfg.tab_ind] = cfg.info["model"]
                    
                    if event.button == ui_.finishBtn and all([i!=0 for i in cfg.buffer.values()]) != 0:
                        cfg.PNAME_TOGGLE = True
                        
                    if cfg.PNAME_TOGGLE:

                        if event.button == ui_.productNameInput:
                            prLabel = ui_.productNameInput.nameVar
                            if prLabel is not None:
                                cfg.products.append(Product(prLabel, 
                                                        sum([i for i in cfg.buffer.values()]),
                                                        sum([i for i in cfg.pBuffer.values()]),
                                                        randint(10, 120)))
                                cfg.EDITOR = False
                                cfg.PNAME_TOGGLE = False
                                for key_ in cfg.curr_product.keys(): cfg.curr_product[key_] = "-"
                                cfg.GAME_SCENE = 2

    if dragging: pygame.mixer.music.set_volume(ui_.volume_slider.drag())

    #Scene management
    func(cfg.GAME_SCENE,
         cfg.INVALID_NAME,
         cfg.EDITOR,
         cfg.CNAME_TOGGLE,
         cfg.PNAME_TOGGLE,
         cfg.INSUFFICIENT_EMPLOYEES,
         cfg.STAFF_MANAGING,
         cfg.UPGRADE_OFFICE,
         cfg.DEVELOP_BRANCHES,
         cfg.HIRING_ERROR,
         cfg.WATCH_PRODUCTS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)


