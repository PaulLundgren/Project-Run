import pygame
import sys
from GameFiles.gameFunctions import *
from GameFiles.gameShop import *
#from GameFiles.ProjectRun import *
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
yellow = (255,255,0)
dark_yellow = (200,200,0)
darker_yellow = (150,150,0)
pause = True
exitgame = False
global shopscreen
global shopwidth
global shopheight
global shopFPS
global shopSPF
global shopPlayer

def unpause():
    global pause
    pause = False
    global exitgame
    exitgame = False

def game_quit():
    global pause
    pause = False
    global exitgame
    exitgame = True
def callshop():
     if(game_shop(shopscreen, shopwidth, shopheight, shopFPS, shopSPF, shopPlayer)):
         game_quit()


def game_pause(screen, screen_width, screen_height, FramePerSec, FPS, player):
    # screen.fill(white)
    global shopscreen
    shopscreen = screen
    global shopwidth
    shopwidth = screen_width
    global shopheight
    shopheight = screen_height
    global shopFPS
    shopFPS = FramePerSec
    global shopSPF
    shopSPF = FPS
    global shopPlayer
    shopPlayer = player
    global pause
    pause = True
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TitleSurf, TitleRect = text_objects("Paused", largeText)
    TitleRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TitleSurf, TitleRect)
    # 
    score_text = pygame.font.Font("freesansbold.ttf", 26)
    # text = score_text.render("P Key to Enter Store / Space Key to Jump", True, yellow, black)
    #textRect = text.get_rect()
    #textRect.center = (300,300)
    #screen.blit(text, textRect)
    w = 100
    h = 50
    start_x = 150
    start_y = 350
    exit_x = 350
    exit_y = 350
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
        button(screen, "Continue", start_x - 25, start_y, w, h, green, bright_green, unpause)
        button(screen, "Quit", exit_x + 25, exit_y, w, h, red, bright_red, game_quit)
        button(screen, "Shop", exit_x -100, exit_y, w, h, dark_yellow, yellow, callshop)
        pygame.display.update()
        FramePerSec.tick(FPS)
    return pause, exitgame
