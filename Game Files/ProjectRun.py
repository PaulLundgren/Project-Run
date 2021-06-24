"""Side-scrolling game. Run away from your project leader and push your commits to repo."""

import pygame
import sys
import time
from pygame.locals import *
from Background import *
from Currency import *
from Player import *
from Platform import *
from Floor import *
from Bug import *
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
obstacles = pygame.sprite.Group()
bugs = pygame.sprite.Group()

# Sprite creation
player = Player()
floor = Floor()

# add sprites to respective groups
sprites.add(floor)

# add floor to list of platform
platforms.add(floor)

# custom game over event
GAMEOVER = USEREVENT + 1
game_over = pygame.event.Event(GAMEOVER)

# custom event that increases the speed of the images
SPEED = USEREVENT + 2
pygame.time.set_timer(SPEED, 30000) # every 30 seconds, increase the speed of the game



# create our background
background = Background()


def plat_gen(platforms, sprites, index):
    """Generate the platforms for the player to utilize."""

    # platforms empty; make platforms
    if len(platforms) < 4:


        if index == 0:

            for i in range(2):
                platform = Platform(700 + 200 * i, 400 - 100 * i)
                platforms.add(platform)
                sprites.add(platform)
        
        elif index == 1:

            for i in range(1):
                platform = Platform(700, 400 - 100 * i)
                platforms.add(platform)
                sprites.add(platform)
        


def bug_gen():
    """Generate the bug obstacles for the game."""
    
    while len(bugs) < 1:
        bug = Bug()

        bugs.add(bug)
        sprites.add(bug)
        obstacles.add(bug)


def coin_gen(coins, sprites, index):
    """Generate the coin obstacles for the game."""

    # check to make sure the list is empty before we generate new coins
    if not coins:

        

        if index == 0:

            # create first set of coins
            for i in range(10):
                if i < 5:
                    coin = Currency(i * 45, 400 - 25 * i)                    
                else:
                    coin = Currency (i * 45, 400)
                
                # add coins to groups
                sprites.add(coin)
                coins.add(coin)
        
        elif index == 1:
            for i in range(20):             
                if i < 10:
                    coin = Currency(i * 45, 400)
                else:
                    coin = Currency(i * 45, 300)           
            # add coins to groups
                sprites.add(coin)
                coins.add(coin)
            
            
    
def game_quit():
    pygame.quit()
    sys.exit()


def game_loop():
    global pause
    while True:

        # go through the events
        for event in pygame.event.get():
            if event.type == QUIT:  # constant QUIT comes from pygames.local import statement
                game_quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # jumping mechanic
                    player.jump(platforms_hit)

                if event.key == pygame.K_ESCAPE:
                    gamePause.game_pause(screen, screen_width, screen_height, FramePerSec, FPS)
            
            

            # game over event; this occurs when the player's HP is 0
            if event.type == GAMEOVER:
                screen.fill((255,0,0))
                pygame.display.update()
                for sprite in sprites:
                    sprite.kill()
                    time.sleep(1)
                    game_quit()

           # if event.type == SPEED:
                #TODO: increase the speed of the images here...
        

        # draw the background to the screen (NOTE: background is not included in sprite since the background is NOT a sprite)
        background.update()
        background.draw(screen)

        index = random.randint(0,1)

       # generate platforms
        plat_gen(platforms, sprites, index)

        # generate bugs
        bug_gen()

        # generate coins
        
        coin_gen(coins, sprites, index)

        # update positions of sprites + draw them onto the screen
        for sprite in sprites:
            sprite.update()
            sprite.draw(screen)

        # update the player + draw the player last (this is so the player image appears in front of other objects)
        player.update()
        player.draw(screen)

        # collision b/w coin sprite + player (3rd parameter is FALSE so we don't 'kill' the sprite)
        coins_hit = pygame.sprite.spritecollide(player, coins, False)

        # collision b/w platform sprite + player
        platforms_hit = pygame.sprite.spritecollide(player, platforms, False)
        player.hit(platforms_hit) # check to see if the player collides with a platform sprite (if so, then stop the player from falling due to acceleration)

        # collision b/w obstacle sprite + player
        obstacles_hit = pygame.sprite.spritecollide(player, obstacles, False)

        

        # remove the coins that the player has come in contact with
        Currency.collision(coins_hit)

        # remove bugs that collide with player
        Bug.collision(obstacles_hit, player)

        

        

        # when the player's HP goes to 0, post game over event
        if player.HP == 0:
            pygame.event.post(game_over)


        # update the display
        pygame.display.update()
        FramePerSec.tick(FPS)


# Game Loop
def main():
    gameIntro.game_intro(screen, screen_width, screen_height, FramePerSec, FPS)
    game_loop()


if __name__ == "__main__":
    main()
