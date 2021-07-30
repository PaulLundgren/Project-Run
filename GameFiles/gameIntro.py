import pygame
import sys
from GameFiles.gameFunctions import *
#from GameFiles.ProjectRun import *
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
intro = True
level = False
level_value = 0
def unpause():
    global intro
    intro = False

def game_quit():
    pygame.quit()
    sys.exit()

def level_select():
    global level
    level = True

def level_one():
    global level_value
    global level
    unpause()
    level_value = 1
    level = False

def level_two():
    global level_value
    global level
    unpause()
    level_value = 2
    level = False

def level_three():
    global level_value
    global level
    unpause()
    level_value = 3
    level = False
def exitmenu():
    global level
    level = False

def game_intro(screen, screen_width, screen_height, FramePerSec, FPS):
    screen.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TitleSurf, TitleRect = text_objects("Project Run", largeText)
    TitleRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TitleSurf, TitleRect)
    score_text = pygame.font.Font("freesansbold.ttf", 20)
    text = score_text.render("P Key to Enter Store / Space Key to Jump / Esc Key to Pause", True, yellow, black)
    textRect = text.get_rect()
    textRect.center = (320,300)
    screen.blit(text, textRect)
    start_x = 150
    start_y = 350
    start_w = 100
    start_h = 50
    exit_x = 350
    exit_y = 350
    exit_w = 100
    exit_h = 50
    global intro
    global level
    while intro:
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TitleSurf, TitleRect = text_objects("Project Run", largeText)
        TitleRect.center = ((screen_width/2),(screen_height/2))
        screen.blit(TitleSurf, TitleRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
            button(screen, "Start", start_x, start_y, start_w, start_h, green, bright_green, level_select)
            button(screen, "Quit", exit_x, exit_y, exit_w, exit_h, red, bright_red, game_quit)
            pygame.display.update()
        FramePerSec.tick(FPS)
        while(level):
            screen.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf', 80)
            TitleSurf, TitleRect = text_objects("Level Select", largeText)
            TitleRect.center = ((screen_width/2),(screen_height/4))
            screen.blit(TitleSurf, TitleRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                button(screen, "level 1", 50 + start_x/2, start_y - 100, start_w, start_h, green, bright_green, level_one)
                button(screen, "level 2", 50 + start_x + start_x/2 , start_y - 100, start_w, start_h, green, bright_green, level_two)
                button(screen, "level 3", 50 + start_x * 2 + start_x/2, start_y - 100, start_w, start_h, green, bright_green, level_three)
                button(screen, "Back", exit_x - 80, exit_y, exit_w, exit_h, red, bright_red, exitmenu)
                pygame.display.update()
            FramePerSec.tick(FPS)
    intro = True
    level = False
    return level_value
