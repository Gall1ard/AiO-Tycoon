import pygame
import sys
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
        btn.fill((0, 0, 0))
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
                        nameVar = self.text
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