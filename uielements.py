#UI elements translocation for better management
import pygame
import sys
from objects import Buttons, InputBox

pygame.init()

initfont = pygame.font.SysFont('Courier New', 80)
mainfont = pygame.font.SysFont('Courier New', 35, bold=True)
mainfont2 = pygame.font.SysFont('Courier New', 30)
smallmainfont = pygame.font.SysFont('Courier New', 20)

colours = [
    (192, 182, 166), #main menu bg
    (227, 206, 150), #beige
    (139, 141, 135), #locker gray
    (169, 195, 196) #lightblue-ish
]

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

swipeLeftBtn = Buttons(rect=(740, 30, 30, 30), #TODO: redo 
                       color=colours[3],
                       hover_color=colours[2],
                       text="<",
                       txtcol=(255, 255, 255),
                       txthov=(230, 230, 230),
                       font=smallmainfont,
                       alpha=255)

swipeRightBtn = Buttons(rect=(1040, 30, 30, 30), #TODO: redo 
                       color=colours[3],
                       hover_color=colours[2],
                       text=">",
                       txtcol=(255, 255, 255),
                       txthov=(230, 230, 230),
                       font=smallmainfont,
                       alpha=255)

createBtn = Buttons(rect=(20, 360, 130, 30), #TODO: redo 
                       color=colours[3],
                       hover_color=colours[2],
                       text="Create +",
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

def form_buttons(rects = []) -> list:
    return [Buttons(rect=rct_) for rct_ in rects]

