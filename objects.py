import pygame
import sys
from enum import Enum
#Object classes

class Buttons:
    def __init__(self, rect, color, hover_color, text, txtcol, txthov, font, alpha=0) -> None:
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.txtcol = txtcol
        self.txthov = txthov
        self.font = font
        self.alpha = alpha

    def draw(self, screen) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):

            current_color = self.hover_color
            current_txt_color = self.txthov
        
        else: 
            current_color = self.color
            current_txt_color = self.txtcol

        #pygame.draw.rect(screen, current_color, self.rect)
        btn = pygame.Surface((self.rect[2], self.rect[3]))
        btn.set_alpha(self.alpha)
        btn.fill(current_color)
        screen.blit(btn, (self.rect[0], self.rect[1]))

        if self.text:
            text_surf = self.font.render(self.text, True, current_txt_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)

    def is_clicked(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


COLOR_ACTIVE = (250, 250, 250)
COLOR_INACTIVE = (200, 200, 200)

class InputBox:

    def __init__(self, rect, font, text):
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, (250, 250, 250))
        self.active = False
        self.font = font
        self.nameVar = ""

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = not self.active if self.rect.collidepoint(event.pos) else False
            self.text = ""
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if 3 <= len(self.text) <= 20:
                        self.nameVar = self.text
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
                    else:
                        print("КАКОЙ ЖЕ ТЫ ДЕГЕНЕРАТ, СКАЗАНО ЖЕ, ЧТО ОТ 3-Х ДО 20-И")
                        
                    self.text = ''
                
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                
                else:
                    if (self.txt_surface.get_width()+30 < self.rect.w):
                        self.text += event.unicode
                    else:
                        pass #TODO: print out ENOUGH ТЫ ЗАЕБАЛ НИК ДЛИННЫМ СТАВИТЬ
                
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        pygame.draw.rect(screen, (230, 230, 230), self.rect, 1)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+(self.rect.h//4)))


class JobTitle:
    
    def __init__(self, minimum_wage, title):
        self.minimum_wage: int = minimum_wage
        self.title: str = title


class Employee(JobTitle):

    def __init__(self, minimum_wage, title, sex, name, age):
        super().__init__(minimum_wage, title)
        self.sex: str = sex
        self.name: str = name
        self.age: int = age
        self.salary: int = self.salary_calc()
    
    def salary_calc(self) -> int:

        if self.sex == "F": 
            self.salary = self.minimum_wage
        
        else:
            self.salary = int(self.minimum_wage * (1 + abs(100 - self.age)))


class Quality(Enum):
    WORST = 1
    BAD = 2
    MID = 3
    GOOD = 4
    BEST = 5

class Devices:

    def __init__(self, model, quality, income):
        self.model: str = model
        self.quality: Quality = quality
        self.income: int = income
    
    def count_influence(self) -> float:
        return self.income / (self.income * (6 - self.quality))

class Monitor(Devices):

    def __init__(self, model, quality, income, resolution, ratio):
        super().__init__(model, quality, income)
        self.resolution: str = resolution
        self.ratio: str = ratio

class Mouse(Devices):

    def __init__(self, model, quality, income, dpi):
        super().__init__(model, quality, income)
        self.dpi: int = dpi

class MousePad(Devices): #Extinction danger

    def __init__(self, model, quality, income, softness):
        super().__init__(model, quality, income)
        self.softness: str = softness

class WebCamera(Devices):
    
    def __init__(self, model, quality, income, resolution, hasMic):
        super().__init__(model, quality, income)
        self.resolution: str = resolution
        self.hasMic: bool = hasMic

class Keyboard(Devices):

    def __init__(self, model, quality, income, size):
        super().__init__(model, quality, income)
        self.size: str = size



    
    


