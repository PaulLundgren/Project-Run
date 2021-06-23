"""Side-scrolling game. Run away from your project leader and push your commits to repo."""

import pygame
import sys
from pygame.locals import *
from Background import *
from Currency import *
from Player import *
from Platform import *
import gameIntro
import gameFunctions
import gamePause




# initialize pygame modules
pygame.init()

# Assign FPS value
FPS = 60
FramePerSec = pygame.time.Clock()

# create a blank screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# set the window caption for our game
pygame.display.set_caption("Project Run")

# group creation
sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
platforms = pygame.sprite.Group()
# Sprite creation
player = Player()
platform = Platform()

# add sprites to respective groups
sprites.add(player)
sprites.add(platform)
platforms.add(platform)

# create currency
for i in range(5):
    coin = Currency(i * 45)
    sprites.add(coin)
    coins.add(coin)

# create our background
background = Background()

def game_quit():
    pygame.quit()
    sys.exit()


def game_loop():
    global pause
    while True:

        # go through the events
        for event in pygame.event.get():
            if event.type == QUIT:  # constant QUIT comes from pygames.local import statement
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # jumping mechanic
                    player.jump()
                if event.key == pygame.K_ESCAPE:
                    gamePause.game_pause(screen, screen_width, screen_height, FramePerSec, FPS)

        # draw the background to the screen (NOTE: background is not included in sprite since the background is NOT a sprite)
        background.update()
        background.draw(screen)

        # update positions of sprites + draw them onto the screen
        for sprite in sprites:
            sprite.update()
            sprite.draw(screen)

        # collision b/w coin sprite + player (3rd parameter is FALSE so we don't 'kill' the sprite)
        coins_list = pygame.sprite.spritecollide(player, coins, False)

        # collision b/w platform sprite + player
        hits_list = pygame.sprite.spritecollide(player, platforms, False)
        player.hit(hits_list) # check to see if the player collides with a platform sprite (if so, then stop the player from falling due to acceleration)

        # removes the coins from the screen on the next iteration (so when a player collides with a coin, we don't draw it until it wraps to the other side of the screen)
        for coin in coins_list:
            coin.isTouched = True


        # update the display
        pygame.display.update()
        FramePerSec.tick(FPS)


# Game Loop
def main():
    gameIntro.game_intro(screen, screen_width, screen_height, FramePerSec, FPS)
    game_loop()


if __name__ == "__main__":
    main()
