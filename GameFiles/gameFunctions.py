import pygame
import os

green = (0, 225, 0)
black = (0, 0, 0)
def text_objects(text, font):  # function to simplify creating text to the screen, taking in as (Font,Size)
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(screen, message, x, y, w, h, default_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # if the mouse is over the button
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            # play sound effect for hitting a button
            # os.path.join(os.path.dirname(__file__), 'Images', 'click.wav')
            #pygame.mixer.Sound.play(pygame.mixer.Sound("click.wav"))
            pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Images', 'click.wav')))
            pygame.mixer.music.stop()
            action()
    else:
        pygame.draw.rect(screen, default_color, (x, y, w, h))
    button_text = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(message, button_text)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def booleanButton (screen, message, x, y, w, h, default_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # x-cord + rect.width > mouse pos x > x-cord and y-cord + rect.height > mouse pos y > y-cord
    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # if the mouse is over the button
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, default_color, (x, y, w, h))
    button_text = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(message, button_text)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def downButton (screen, message, x, y, w, h, default_color):
    pygame.draw.rect(screen, default_color, (x, y, w, h))
    pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Images', 'click.wav')))
    pygame.mixer.music.stop()
    button_text = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(message, button_text)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

# def show_coins(screen, message, x, y):
    # score_text = pygame.font.Font("freesansbold.ttf", 40)
    # text = score_text.render(message, True, green, blue)
    # textSurf, textRect = text_objects(text, score_text)
    # screen.blit(textSurf, textRect)


def show_ui(screen, message, x, y, font_size = None):
    font_size = font_size if font_size != None else 25
    score_text = pygame.font.Font("freesansbold.ttf", font_size)
    text = score_text.render(message, True, green, black)
    textRect = text.get_rect()
    textRect.center = (x,y)
    screen.blit(text, textRect)


