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
pause = True

def unpause():
    global pause
    pause = False


def game_pause(screen, screen_width, screen_height, FramePerSec, FPS):
    # screen.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TitleSurf, TitleRect = gameFunctions.text_objects("Paused", largeText)
    TitleRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TitleSurf, TitleRect)
    start_x = 150
    start_y = 350
    start_w = 100
    start_h = 50
    exit_x = 350
    exit_y = 350
    exit_w = 100
    exit_h = 50
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
        gameFunctions.button(screen, "Continue", start_x, start_y, start_w, start_h, green, bright_green, ProjectRun.game_loop)
        gameFunctions.button(screen, "Quit", exit_x, exit_y, exit_w, exit_h, red, bright_red, ProjectRun.game_quit)
        pygame.display.update()
        FramePerSec.tick(FPS)