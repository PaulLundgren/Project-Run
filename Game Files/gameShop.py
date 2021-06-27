import gameFunctions
import pygame
import ProjectRun
# from pygame.locals import *
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


def game_shop(screen, screen_width, screen_height, FramePerSec, FPS, player):
    #def item_one():

    # screen.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TitleSurf, TitleRect = gameFunctions.text_objects("Store", largeText)
    TitleRect.center = ((screen_width/2),(screen_height/8))
    screen.blit(TitleSurf, TitleRect)
    start_x = 150
    start_y = 350
    start_w = 100
    start_h = 50
    exit_x = 350
    exit_y = 350
    exit_w = 100
    exit_h = 50
    item_x = 100
    item_y = 100
    item_w = 100
    item_h = 50
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
            gameFunctions.button(screen, "Continue", start_x, start_y, start_w, start_h, green, bright_green, ProjectRun.game_loop)
            gameFunctions.button(screen, "Quit", exit_x, exit_y, exit_w, exit_h, red, bright_red, ProjectRun.game_quit)
            if(gameFunctions.booleanButton(screen, "Item", item_x, item_y, item_w, item_h, yellow, dark_yellow)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameFunctions.downButton(screen, "Item", item_x, item_y, item_w, item_h, darker_yellow)
                    print("item one")

        pygame.display.update()
        FramePerSec.tick(FPS)