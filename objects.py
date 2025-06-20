import pygame
import sys
from enum import Enum
#Object classes

pygame.init()

class Buttons:
    def __init__(self, 
                 rect,
                 color=(0,0,0),
                 hover_color=(0,0,0),
                 text="",
                 txtcol=(0,0,0),
                 txthov=(0,0,0),
                 font=pygame.font.SysFont('Arial',0), 
                 alpha=0) -> None:
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
        self.buffer = text

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            bfr = self.text
            if self.rect.collidepoint(event.pos):
                self.active = not self.active 
                if self.text == self.buffer: self.text = ""
            else:
                self.active = False
                self.text = bfr

            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            self.txt_surface = self.font.render(self.text, True, self.color)

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if 3 <= len(self.text) <= 10:
                        self.nameVar = self.text
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
                    else:
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT + 4, button=self))
                        #print("СКАЗАНО ЖЕ, ЧТО ОТ 3-Х ДО 10-И")
                    
                    self.active = False
                    self.text = self.buffer
                
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


class Slider:
    def __init__(self, slider_x, slider_y, width, height, knob_rad, colour1, colour2):
        self.slider_x = slider_x
        self.slider_y = slider_y
        self.width = width
        self.height = height
        self.volume = 0.25
        self.knob_rad = knob_rad
        self.knob_x = slider_x + int(self.volume * self.width)
        self.col1 = colour1
        self.col2 = colour2
    
    def drag(self,):
        mouse_x = pygame.mouse.get_pos()[0]
        self.knob_x = max(self.slider_x, min(mouse_x, self.slider_x + self.width))
        self.volume = (self.knob_x - self.slider_x) / self.width
        return self.volume
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.col1, (self.slider_x, self.slider_y - self.height // 2, self.width, self.height))
        pygame.draw.circle(screen, self.col2, (self.knob_x, self.slider_y), self.knob_rad)

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

    def __init__(self, model, quality, income, price):
        self.model: str = model
        self.quality: Quality = quality
        self.income: int = income
        self.price: int = price
    
    def count_influence(self) -> float:
        return self.income / (self.income * (6 - self.quality))

class Monitor(Devices):

    def __init__(self, model, quality, income, price, resolution, ratio):
        super().__init__(model, quality, income, price)
        self.resolution: str = resolution
        self.ratio: str = ratio
    
    def info(self):
        return {
            'model': self.model,
            'quality': self.quality.name,
            'income': self.income,
            'price': self.price,
            'resolution': self.resolution,
            'ratio': self.ratio
        }

class Mouse(Devices):

    def __init__(self, model, quality, income, price, dpi):
        super().__init__(model, quality, income, price)
        self.dpi: int = dpi
    
    def info(self):
        return {
            'model': self.model,
            'quality': self.quality.name,
            'income': self.income,
            'price': self.price,
            'dpi': self.dpi
        }

class MousePad(Devices): #Extinction danger

    def __init__(self, model, quality, income, price, softness):
        super().__init__(model, quality, income, price)
        self.softness: str = softness

    def info(self):
        return {
            'model': self.model,
            'quality': self.quality.name,
            'income': self.income,
            'price': self.price,
            'softness': self.softness
        }

class WebCamera(Devices):
    
    def __init__(self, model, quality, income, price, resolution, hasMic):
        super().__init__(model, quality, income, price)
        self.resolution: str = resolution
        self.hasMic: bool = hasMic
    
    def info(self):
        return {
            'model': self.model,
            'quality': self.quality.name,
            'income': self.income,
            'price': self.price,
            'resolution': self.resolution,
            'hasMic': self.hasMic
        }

class Keyboard(Devices):

    def __init__(self, model, quality, income, price, size):
        super().__init__(model, quality, income, price)
        self.size: str = size
    
    def info(self):
        return {
            'model': self.model,
            'quality': self.quality.name,
            'income': self.income,
            'price': self.price,
            'size': self.size
        }


class Product:

    def __init__(self, name: str, total_income: int, total_price: int, amount: int):
        self.name = name
        self.total_income = total_income
        self.total_price = total_price
        self.amount = amount
    
    def info(self):
        return {
            "name": self.name,
            "total income": self.total_income,
            "total price": self.total_price,
            "amount": self.amount
        }
    

class Employee:

    def __init__(self, name: str, age: int, rating: float, experience: int, salary: int):
        self.name = name
        self.age = age
        self.rating = rating
        self.experience = experience
        self.is_hired = False
        self.salary = salary
    
    def info(self):
        return {
            "Имя": self.name,
            "Возраст": self.age,
            "Рейтинг": self.rating,
            "Стаж (лет)": self.experience,
            "Статус": self.is_hired,
            "Требуемая З/П": self.salary
        }