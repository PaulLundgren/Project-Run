import pygame
import os
import sys
from GameFiles.gameFunctions import *
#from GameFiles.ProjectRun import *
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
yellow = (255,255,0)
dark_yellow = (200,200,0)
darker_yellow = (150,150,0)
pause = True

def unpause():
    global pause
    pause = False

def game_quit():
    pygame.quit()
    sys.exit()
def gamenothing():
    return

def game_shop(screen, screen_width, screen_height, FramePerSec, FPS, player):
    #def item_one():
    global pause
    pause = True
    # screen.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    text = largeText.render("Store", True, yellow, black)
    textRect = text.get_rect()
    # TitleSurf, TitleRect = text_objects("Store", largeText)
    textRect.center = ((screen_width/2),(screen_height/8))
    screen.blit(text, textRect)

    start_x = 125
    start_y = 350
    start_w = 100
    start_h = 50
    exit_x = 375
    exit_y = 350
    exit_w = 100
    exit_h = 50
    item1_x = 100
    item1_y = 100
    item_w = 200
    item_h = 50
    item2_x = 100
    item2_y = 160
    item3_x = 100
    item3_y = 220
    w = 100
    h = 50
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
            button(screen, "Continue", start_x, start_y, start_w, start_h, green, bright_green, unpause)
            button(screen, "Quit", exit_x, exit_y, exit_w, exit_h, red, bright_red, game_quit)
            button(screen, "Shop", exit_x -125, exit_y, w, h, yellow, yellow, gamenothing)
            if(booleanButton(screen, "Buy a Heart = 50", item1_x, item1_y, item_w, item_h, yellow, dark_yellow)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    downButton(screen, "Buy a Heart = 50", item1_x, item1_y, item_w, item_h, darker_yellow)
                    if(player.Coins >= 50):
                        player.HP = player.HP + 1
                        player.Coins = player.Coins - 50
            if(booleanButton(screen, "increase speed = 1", item2_x, item2_y, item_w, item_h, yellow, dark_yellow)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    downButton(screen, "increase speed = 1", item2_x, item2_y, item_w, item_h, darker_yellow)
                    if(player.Coins >= 1):
                        player.permanent_increase_speed()
                        player.Coins = player.Coins - 1
            if(booleanButton(screen, "increase jump = 1", item3_x, item3_y, item_w, item_h, yellow, dark_yellow)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    downButton(screen, "increase jump = 1", item3_x, item3_y, item_w, item_h, darker_yellow)
                    if(player.Coins >= 1):
                        player.permanent_increase_jump()
                        player.Coins = player.Coins - 1
        
        # updates coin ui while in store
        show_ui(screen, "Health : " + str(player.HP), 540, 20)
        show_ui(screen, "Coins : " + str(player.Coins), 100, 15)

        pygame.display.update()
        FramePerSec.tick(FPS)
    return