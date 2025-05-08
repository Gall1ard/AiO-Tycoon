import pygame
import sys
#Object classes

class Buttons:
    def __init__(self, rect, color, hover_color, text, txtcol, txthov, font) -> None:
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.txtcol = txtcol
        self.txthov = txthov
        self.font = font

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
