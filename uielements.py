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
    (169, 195, 196), #lightblue-ish
    (182, 212, 214) 
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

editorBtn = Buttons(rect=(740, 250, 332, 40),
                    color=colours[3],
                    hover_color=colours[4],
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

createBtn = Buttons(rect=(20, 630, 130, 30), #TODO: redo 
                       color=colours[3],
                       hover_color=colours[2],
                       text="Создать +",
                       txtcol=(255, 255, 255),
                       txthov=(230, 230, 230),
                       font=smallmainfont,
                       alpha=255)

selectBtn = Buttons(rect=(900, 555, 130, 30), #TODO: redo 
                       color=colours[3],
                       hover_color=colours[2],
                       text="Выбрать",
                       txtcol=(255, 255, 255),
                       txthov=(230, 230, 230),
                       font=smallmainfont,
                       alpha=255)

finishBtn = Buttons(rect=(20, 680, 130, 30), #TODO: redo 
                       color=colours[3],
                       hover_color=colours[2],
                       text="Завершить",
                       txtcol=(255, 255, 255),
                       txthov=(230, 230, 230),
                       font=smallmainfont,
                       alpha=255)

branchesBtn = Buttons(rect=(740, 300, 332, 40),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Филиалы",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

hireBtn = Buttons(rect=(740, 350, 332, 40),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Нанять",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

upgradeBtn = Buttons(rect=(740, 400, 332, 40),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Улучшить офис",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

taxfraudBtn = Buttons(rect=(740, 450, 332, 40),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Уклонение от налогов",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

depositBtn = Buttons(rect=(740, 500, 332, 40),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Депнуть имущество",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

watchBtn = Buttons(rect=(740, 550, 332, 40),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Посмотреть продукцию",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

lLeftBtn = Buttons(rect=(180, 119, 50, 476),
                    color=colours[3],
                    hover_color=colours[4],
                    text="<<",
                    txtcol=(255, 255, 255),
                    txthov=(255, 255, 255),
                    font=smallmainfont,
                    alpha=255)

lRightBtn = Buttons(rect=(900, 119, 50, 476),
                    color=colours[3],
                    hover_color=colours[4],
                    text=">>",
                    txtcol=(255, 255, 255),
                    txthov=(255, 255, 255),
                    font=smallmainfont,
                    alpha=255)

fireBtn = Buttons(rect=(250, 380, 198, 20),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Уволить",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

unfireBtn = Buttons(rect=(250, 380, 198, 20),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Нанять",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)

procUpgBtn = Buttons(rect=(451, 480, 198, 40),
                    color=colours[3],
                    hover_color=colours[4],
                    text="Купить",
                    txtcol=(255, 255, 255),
                    txthov=(230, 230, 230),
                    font=smallmainfont,
                    alpha=255)


nameInput = InputBox(
    rect=(340, 260, 400, 50),
    font=smallmainfont,
    text="Имя (от 3-х до 10-и букв)"
)

companyNameInput = InputBox(
    rect=(340, 260, 400, 50),
    font=smallmainfont,
    text="Название фирмы (3-10 букв)"
)

productNameInput = InputBox(
    rect=(180, 645, 520, 50),
    font=smallmainfont,
    text="Название девайса (Нажать Enter после ввода)"
)

def form_buttons(rects = []) -> list:
    return [Buttons(rect=rct_) for rct_ in rects]

