import pygame
from imgsinit import *
import uielements as ui_
from employees import get_candidates
from displayeditor import unfold
from inventory import items
import cfg

pygame.init()

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

grid_shift_y_inf = 18
grid_shift_y_comp = 28

#GAME_SCENE = 0

def func(GAME_SCENE,
         INVALID_NAME,
         EDITOR,
         CNAME_TOGGLE,
         PNAME_TOGGLE,
         INSUFFICIENT_EMPLOYEES,
         STAFF_MANAGING,
         UPGRADE_OFFICE,
         DEVELOP_BRANCHES,
         HIRING_ERROR,
         WATCH_PRODUCTS):
    
    if GAME_SCENE == -1:
        
        screen.fill((169, 195, 196))
        tint = pygame.Surface((1080, 720))
        tint.set_alpha(200)
        tint.fill((0, 0, 0))
        screen.blit(tint, (0, 0))
        
        ui_.backBtn.draw(screen)

        t1_font = mainfont2.render("Вы - банкрот:(", True, (255, 255, 255))
        t1_rect = t1_font.get_rect(center=(screen_width//2, 370))
        screen.blit(t1_font, t1_rect)



    if GAME_SCENE == 0:
        # Background, title and buttons
        screen.fill((192, 182, 166))
        screen.blit(startBg, (-100, 0))

        title_font = initfont.render("AiO Tycoon", True, (255, 255, 255))
        title_rect = title_font.get_rect(center=(screen_width//2, 50))
        screen.blit(title_font, title_rect)

        title_font = mainfont2.render("Громкость", True, (255, 255, 255))
        title_rect = title_font.get_rect(center=(125, 600))
        screen.blit(title_font, title_rect)

        ui_.playBtn.draw(screen)
        ui_.quitBtn.draw(screen)
        ui_.volume_slider.draw(screen)
    
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

        if INVALID_NAME:
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
            
            screen.blit(mainScenesBg[cfg.cBg], (0, 0))

            tint = pygame.Surface((350, 720))
            tint.set_alpha(204)
            tint.fill((0, 0, 0))
            screen.blit(tint, (730, 0))

            cName = smallmainfont.render(f"Название: {ui_.companyNameInput.nameVar}", True, (255, 244, 244))
            cNameRect = cName.get_rect(topleft=(screen_width-340, 10))
            screen.blit(cName, cNameRect)

            cBudget = smallmainfont.render(f"Бюджет: {cfg.budget}", True, (255, 244, 244))
            cBudgetRect = cBudget.get_rect(topleft=(screen_width-340, 50))
            screen.blit(cBudget, cBudgetRect)

            office = mainfont2.render(f"Основной офис", True, (255, 244, 244))
            officeRect = office.get_rect(center=(365, 40))
            screen.blit(office, officeRect)

            cEmp = smallmainfont.render(f"Штат сотрудников: {cfg.number_of_employees}", True, (255, 244, 244))
            cEmpRect = cEmp.get_rect(topleft=(screen_width-340, 90))
            screen.blit(cEmp, cEmpRect)

            eDisp = smallmainfont.render(f"Расходы в месяц: {cfg.expenses + cfg.rent}", True, (255, 244, 244))
            eDispRect = eDisp.get_rect(topleft=(screen_width-340, 130))
            screen.blit(eDisp, eDispRect)

            emLimit = smallmainfont.render(f"Макс. сотрудников: {cfg.staff_limit}", True, (255, 244, 244))
            emLimitRect = emLimit.get_rect(topleft=(screen_width-340, 170))
            screen.blit(emLimit, emLimitRect)

            brNum = smallmainfont.render(f"Филиалов: {cfg.branches} (доход +{int((cfg.adjustment-1)*100)}%)", True, (255, 244, 244))
            brNumRect = brNum.get_rect(topleft=(screen_width-340, 210))
            screen.blit(brNum, brNumRect)

            ui_.editorBtn.draw(screen)
            ui_.branchesBtn.draw(screen)
            ui_.hireBtn.draw(screen)
            ui_.upgradeBtn.draw(screen)
            ui_.taxfraudBtn.draw(screen)
            ui_.depositBtn.draw(screen)
            ui_.watchBtn.draw(screen)

            if STAFF_MANAGING or DEVELOP_BRANCHES or UPGRADE_OFFICE or WATCH_PRODUCTS:
                
                tint = pygame.Surface((1080, 720))
                tint.set_alpha(204)
                tint.fill((0, 0, 0))
                screen.blit(tint, (0, 0))

                stafftab = pygame.Surface((720, 476))
                stafftab.fill((150, 176, 177))
                screen.blit(stafftab, (180, 119))

                if STAFF_MANAGING:

                    cnd_info = mainfont2.render(f"Штат сотрудников: {cfg.number_of_employees}", True, (255, 244, 244))
                    cnd_rect = cnd_info.get_rect(topleft=(250, 409))
                    screen.blit(cnd_info, cnd_rect)

                    ui_.lLeftBtn.draw(screen)
                    ui_.lRightBtn.draw(screen)

                    screen.blit(resumeIcon, (250, 139))

                    if len(cfg.candidates) > 0:
                        c = 0

                        for key_, val_ in cfg.candidates[cfg.staff_ind].items():
                            txt = f"{key_}: {val_}" if key_ != "Статус" else f"{key_}: {'Нанят' if val_ else 'Не нанят'}"
                            cnd_info = smallmainfont.render(txt, True, (255, 244, 244))
                            cnd_rect = cnd_info.get_rect(topleft=(500, 139+(25*c)))
                            screen.blit(cnd_info, cnd_rect)
                            c += 1
                        
                        if cfg.candidates[cfg.staff_ind]["Статус"]:
                            ui_.fireBtn.draw(screen)
                        
                        else:
                            ui_.unfireBtn.draw(screen)
                        
                        if HIRING_ERROR:
                            cnd_info = mainfont2.render(f"Офисы переполнены", True, (255, 244, 244))
                            cnd_rect = cnd_info.get_rect(topleft=(250, 449))
                            screen.blit(cnd_info, cnd_rect)

                    
                elif UPGRADE_OFFICE:

                    if cfg.cBg <= 1:
                        price = mainfont2.render(f"Цена: {cfg.curr_price}", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 450))
                        screen.blit(price, price_rect)

                        price = smallmainfont.render(f"Вместимость: {cfg.office_params[cfg.curr_price]} сотрудников", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 420))
                        screen.blit(price, price_rect)

                        if cfg.staff_limit != cfg.number_of_employees:
                            tt = f"Наймите ещё сотрудников ({cfg.staff_limit-cfg.number_of_employees}), чтобы прокачать офис" 
                        else: 
                            tt = ""

                        price = smallmainfont.render(tt, True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 550))
                        screen.blit(price, price_rect)
                    
                    else:
                        price = mainfont2.render(f"Достигнут макс. уровень", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 450))
                        screen.blit(price, price_rect)

                        price = smallmainfont.render(f"Финал DEMO", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 420))
                        screen.blit(price, price_rect)

                    screen.blit(miniUpg1[cfg.cBg], (389, 100))

                    ui_.procUpgBtn.draw(screen)
                    pass

                elif DEVELOP_BRANCHES:

                    if cfg.cBg == 2:
                        price = mainfont2.render(f"Цена: 90000000", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 450))
                        screen.blit(price, price_rect)

                        price = smallmainfont.render(f"+75% к доходу", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 420))
                        screen.blit(price, price_rect)

                        price = smallmainfont.render(f"Построено филиалов: {cfg.branches}/6", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 550))
                        screen.blit(price, price_rect)

                        screen.blit(branch, (389, 100))
                        ui_.procUpgBtn.draw(screen)

                    else:
                        log1 = smallmainfont.render("У вас должен быть лучший офис,", True, (255, 244, 244))
                        log1_rect = log1.get_rect(center=(540, 360))
                        screen.blit(log1, log1_rect)
                        log1 = smallmainfont.render("прежде чем филиал будет построен", True, (255, 244, 244))
                        log1_rect = log1.get_rect(center=(540, 390))
                        screen.blit(log1, log1_rect)
                
                elif WATCH_PRODUCTS:
                    ui_.lLeftBtn.draw(screen)
                    ui_.lRightBtn.draw(screen)

                    if len(cfg.products) != 0:
                        screen.blit(computerDummy, (324, 100))
                        price = smallmainfont.render(f"{cfg.products[cfg.prod_ind].info()['name']}", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 550))
                        screen.blit(price, price_rect)
                    
                    else:
                        price = smallmainfont.render(f"Пусто", True, (255, 244, 244))
                        price_rect = price.get_rect(center=(540, 550))
                        screen.blit(price, price_rect)


        
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
                screen.blit(computerDummy, (140,100))

                temp = ""

                match cfg.tab_ind:
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
                
                for i in ui_.form_buttons(cfg.currBtns): i.draw(screen)
                
                tab_text = smallmainfont.render(temp, True, (255, 244, 244))
                tab_rect = tab_text.get_rect(center=(905, 45))
                screen.blit(tab_text, tab_rect)

                info_label = smallmainfont.render("Хар-ки:", True, (255, 244, 244))
                info_label_rect = info_label.get_rect(topleft=(750, 560))
                screen.blit(info_label, info_label_rect)
                
                if cfg.info != []:
                    c = 0

                    for key_, val_ in cfg.info.items():
                        itmp = tinyfont.render(f"{key_}: {val_}", True, (255, 244, 244))
                        itmpr = itmp.get_rect(topleft=(750, 600+(grid_shift_y_inf*c)))
                        screen.blit(itmp, itmpr)
                        c += 1
                    
                for key_, val_ in cfg.curr_product.items():
                    itmp = smallmainfont.render(f"{cfg.namm[key_]}: {val_}", True, (255, 244, 244))
                    itmpr = itmp.get_rect(topleft=(20, 400+(grid_shift_y_comp*key_)))
                    screen.blit(itmp, itmpr)

                if PNAME_TOGGLE:
                    ui_.productNameInput.draw(screen)


        ui_.backBtn.draw(screen)
    

