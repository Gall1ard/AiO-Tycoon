import pygame
from imgsinit import smallmainfont

pygame.init()

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

grid_shift_x = 10
grid_shift_y = 120

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
                tempR = temp_.get_rect(topleft=(initX-grid_shift_x, initY+grid_shift_y))
                if mode: screen.blit(temp_, tempR)

                tRects.append(tempR)
            if not mode:
                return tRects