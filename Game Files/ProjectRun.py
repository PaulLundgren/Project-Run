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
sprites.add(player)
sprites.add(floor)

# add floor to list of platform
platforms.add(floor)

# custom game over event
GAMEOVER = USEREVENT + 1
game_over = pygame.event.Event(GAMEOVER)

# create currency
for i in range(5):
    coin = Currency(i * 45)
    sprites.add(coin)
    coins.add(coin)

# create our background
background = Background()

# generate platforms
def plat_gen():
    """Generate the platforms for the player to utilize."""

    # dictates the number of platforms we can have at most (in this case, it would be 3, since the floor is considered a platform)
    while len(platforms) < 4:
        platform = Platform()
       

        while check_platforms(platform, platforms):
            platform = Platform()
            
        # add platforms to groups
        platforms.add(platform)
        sprites.add(platform)

def check_platforms(platform, platforms):
    """Generates the spawning locations of the platforms."""

    # if a platform is spawned colliding with another platform, this method returns true and will result in another instance of a platform
    if pygame.sprite.spritecollideany(platform, platforms):
        return True
    
    else:
        # check the current platforms and make sure that their is a decent space between them, returning true will result in another instance of a platform
        for p in platforms:

            if p == platform:
                continue
            elif (abs(platform.rect.top - p.rect.bottom) < 110) and (abs(platform.rect.bottom - p.rect.top) < 110):
                return True

        # valid spacing + no collision detected, so no need to create another platform     
        return False

def check_obstacles(obstacles_hit):
    """Determine the number of obstacles that the player sprite has currently collided with."""
    
    for obstacle in obstacles_hit:

        if obstacle.hasTouched:
            player.HP -= 1
            obstacle.kill() # remove the sprite

def bug_gen():
    """Generate the bug obstacles for the game."""
    
    while len(bugs) < 1:
        bug = Bug()

        bugs.add(bug)
        sprites.add(bug)
        obstacles.add(bug)

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

        # draw the background to the screen (NOTE: background is not included in sprite since the background is NOT a sprite)
        background.update()
        background.draw(screen)

       # generate platforms
        plat_gen()

        # generate bugs
        bug_gen() 

        # update positions of sprites + draw them onto the screen
        for sprite in sprites:
            sprite.update()
            sprite.draw(screen)

        # collision b/w coin sprite + player (3rd parameter is FALSE so we don't 'kill' the sprite)
        coins_hit = pygame.sprite.spritecollide(player, coins, False)

        # collision b/w platform sprite + player
        platforms_hit = pygame.sprite.spritecollide(player, platforms, False)
        player.hit(platforms_hit) # check to see if the player collides with a platform sprite (if so, then stop the player from falling due to acceleration)

        # collision b/w obstacle sprite + player
        obstacles_hit = pygame.sprite.spritecollide(player, obstacles, False)

        # check how many obstacles that the player has collided with
        check_obstacles(obstacles_hit)

        # removes the coins from the screen on the next iteration (so when a player collides with a coin, we don't draw it until it wraps to the other side of the screen)
        for coin in coins_hit:
            coin.hasTouched = True

        # check the collisions b/w player + obstacles
        for obstacle in obstacles_hit:
            obstacle.hasTouched = True

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
