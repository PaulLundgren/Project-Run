import pygame
import sys
from GameFiles.gameFunctions import *
from GameFiles.LevelEditor import *
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
intro = True
level = False
level_value = 0
global shopscreen
global shopwidth
global shopheight
global shopFPS
global shopSPF
global shopPlayer

def unpause():
    global intro
    intro = False
def exitmenu():
    global level
    level = False

def gamehelp():
    shopscreen.fill(white)

def leveleditting():
    gameedit()

def gamehelp(screen, screen_width, screen_height, FramePerSec, FPS):
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
    screen.fill(white)
    start_x = 150
    start_y = 350
    start_w = 100
    start_h = 50
    global intro
    global level
    while intro:
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        TitleSurf, TitleRect = text_objects("Controls:", largeText)
        TitleRect.center = ((screen_width/2), (screen_height/8))
        screen.blit(TitleSurf, TitleRect)
        TitleSurf, TitleRect = text_objects("ESC: Pause Menu and Shop Menu in game", largeText)
        TitleRect.center = ((screen_width/2), (screen_height/8 + 50))
        screen.blit(TitleSurf, TitleRect)
        TitleSurf, TitleRect = text_objects("A and D: for left and right movement respectivly", largeText)
        TitleRect.center = ((screen_width/2), ((screen_height/8 + 100)))
        screen.blit(TitleSurf, TitleRect)
        TitleSurf, TitleRect = text_objects("S: To go down faster", largeText)
        TitleRect.center = ((screen_width/2), ((screen_height/8 + 150)))
        screen.blit(TitleSurf, TitleRect)
        TitleSurf, TitleRect = text_objects("SPACE: To jump", largeText)
        TitleRect.center = ((screen_width/2), ((screen_height/8 + 200)))
        screen.blit(TitleSurf, TitleRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
            button(screen, "Back", start_x - 80, start_y, start_w, start_h, green, bright_green, unpause)
            pygame.display.update()
        FramePerSec.tick(FPS)
    intro = True
    return
