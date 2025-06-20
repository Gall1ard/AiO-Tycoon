import pygame
pygame.init()

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
branch = pygame.image.load("sources/Miniatures/branch1.png")

resumeIcon = pygame.image.load("sources/Sprites/resume.png")

monitorDummy = pygame.image.load("sources/Sprites/monitordummy.png")
mouseDummy = pygame.image.load("sources/Sprites/mousedummy.png")
wcamDummy = pygame.image.load("sources/Sprites/webcameradummy.png")
mousepadDummy = pygame.image.load("sources/Sprites/mousepaddummy.png")
keyboardDummy = pygame.image.load("sources/Sprites/keyboarddummy.png")
computerDummy = pygame.image.load("sources/Sprites/aiodummy.png")

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