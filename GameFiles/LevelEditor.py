import pygame

import os





pygame.init()



clock = pygame.time.Clock()

FPS = 60



screen_width = 640

screen_height = 480

boundary = 250

screen = pygame.display.set_mode((screen_width, screen_height + boundary))



# some colors

BLUE = (0, 0, 240)

GREEN = (140, 200, 100)

WHITE = (255, 255, 255)



# image variables

ROWS = 10

COLS_MAX = 150

TILE_SIZE = screen_height // ROWS



scroll_left = False

scroll_right = False

scroll = 0

scroll_speed = 1



# image loading

background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'background_image.jpg')).convert_alpha()



def draw_background():

    screen.fill(BLUE)



    width = background.get_width()



    for i in range(100):

     screen.blit(background, ((i * width) - scroll, 0))



def draw_grid():



    for i in range(COLS_MAX + 1):

        pygame.draw.line(screen, WHITE, (i*TILE_SIZE - scroll, 0), (i*TILE_SIZE - scroll, screen_height))

        



    for i in range(ROWS + 1):

        pygame.draw.line(screen, WHITE, (0, i*TILE_SIZE), (screen_width, i*TILE_SIZE))





pygame.display.set_caption("Level Editor")



while True:

    

    clock.tick(FPS)





    # draw background image

    draw_background()

    draw_grid()





    # scroll map

    if scroll_left == True and scroll > 0:

        scroll -= 10 * scroll_speed



    if scroll_right == True:

        scroll += 10 * scroll_speed



    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

        

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                scroll_left = True

            if event.key == pygame.K_RIGHT:

                scroll_right = True

            if event.key == pygame.K_LSHIFT:

                scroll_speed = 5



        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:

                scroll_left = False

            if event.key == pygame.K_RIGHT:

                scroll_right = False

            if event.key == pygame.K_LSHIFT:

                scroll_speed = 1





        



    



    pygame.display.update()


