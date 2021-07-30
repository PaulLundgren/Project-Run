import pygame
import sys
from GameFiles.gameFunctions import *
from GameFiles.ProjectRun import *
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
intro = True
def unpause():
    global intro
    intro = False

def game_quit():
    pygame.quit()
    sys.exit()

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
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
        button(screen, "Start", start_x, start_y, start_w, start_h, green, bright_green, unpause)
        button(screen, "Quit", exit_x, exit_y, exit_w, exit_h, red, bright_red, game_quit)
        pygame.display.update()
        FramePerSec.tick(FPS)
    return
