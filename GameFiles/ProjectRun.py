"""Side-scrolling game. Run away from your project leader and push your commits to repo."""

import pygame
import sys
import time
import random
from pygame.locals import *
from GameFiles.Background import *
from GameFiles.Currency import *
from GameFiles.Player import *
from GameFiles.Platform import *
from GameFiles.Floor import *
from GameFiles.Bug import *
from GameFiles.End import *
from GameFiles.gameIntro import *
from GameFiles.gameFunctions import *
from GameFiles.gamePause import *
from GameFiles.Generator import *
from GameFiles.gameShop import *






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

# background music for the game
# pygame.mixer.Sound.play(pygame.mixer.Sound("music2.wav")) # play sound effect for hitting a coin
#pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Images', 'music2.wav')))

# group creation
sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
platforms = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
bugs = pygame.sprite.Group()
end_spawn = pygame.sprite.Group()

# Sprite creation
player = Player(screen_width, screen_height)
floor = Floor(screen_width, screen_height)
end = End(screen_width, screen_height)

# add Non-Generated sprites to respective groups (FIXME: rework this to include player as well)
sprites.add(floor)
platforms.add(floor)

# custom game over event; this occurs when the player's HP is 0
GAMEOVER = USEREVENT + 1
game_over = pygame.event.Event(GAMEOVER)

# custom event that increases the speed of the images
SPEED = USEREVENT + 2

# custom event that respawns sprites
REDRAW = USEREVENT + 3

# custom event that happens when the player reaches the end
WIN = USEREVENT + 4
player_wins = pygame.event.Event(WIN)

# custom event that 'slows down' the player (happens when there is a collision b/w the player sprite and an obstacle)
SLOWDOWN = USEREVENT + 5
slowdown = pygame.event.Event(SLOWDOWN)

# create our background
background = Background(screen_width, screen_height)


# generate items outside game loop()
coin_gen(coins, sprites, screen_width, screen_height)
plat_gen(platforms, sprites, screen_width, screen_height)
bug_gen(bugs, obstacles, sprites, screen_width, screen_height)


def game_quit():
    pygame.quit()
    sys.exit()


def game_loop():

    global pause
    counter = 0 # keep track of the time in game (in milliseconds)
    isEnd = False
    FramePerSec = pygame.time.Clock()
    pygame.time.set_timer(SPEED, 20000) # every 20 seconds, increase the speed of the game
    pygame.time.set_timer(REDRAW, 8000) # every 8 seconds, redraw objects on the other side of the screen


    offset = FramePerSec.get_time()
    start_time = pygame.time.get_ticks()

    while True:
        counter += FramePerSec.get_time() - offset
        # print(counter)
        for event in pygame.event.get():
            if event.type == QUIT:  # constant QUIT comes from pygames.local import statement
                game_quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump(platforms_hit)

                if event.key == pygame.K_ESCAPE:
                    game_pause(screen, screen_width, screen_height, FramePerSec, FPS)
                if event.key == pygame.K_p:
                    game_shop(screen, screen_width, screen_height, FramePerSec, FPS, player)


            if event.type == GAMEOVER:
                screen.fill((255,0,0))
                pygame.display.update()
                time.sleep(1)
                game_quit()

            if event.type == SPEED:
                background.inc_speed()

                # increase speed of sprites that are not the floor or the player
                for sprite in sprites:
                    if not isinstance(sprite, Floor) and not isinstance(sprite, Player):
                        sprite.inc_speed()

            if event.type == REDRAW:

                # spawn end after 90 seconds
                if isEnd:
                    x = -1
                    change_coins(coins, x)
                    change_platforms(platforms, x)
                    change_bugs(bugs, x)
                    end_spawn.add(end)
                    sprites.add(end)

                if not isEnd:
                    x = random.randint(0,5)
                    change_coins(coins, x)
                    change_platforms(platforms, x)
                    change_bugs(bugs, x)


            if event.type == SLOWDOWN:
                background.slowdown()
                for sprite in sprites:
                    if not isinstance(sprite, Floor) and not isinstance(sprite, Player):
                        sprite.slowdown()


            if event.type == WIN:
                screen.fill((0,255,0))
                pygame.display.update()
                time.sleep(1)
                game_quit()



        # draw the background to the screen (NOTE: background is not included in sprite since the background is NOT a sprite)
        background.update()
        background.draw(screen)


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
        coins_hit = pygame.sprite.spritecollide(player, coins, False)

        # collision b/w the end sprite + player
        end_hit = pygame.sprite.spritecollide(player, end_spawn, False)


        # remove the coins that the player has come in contact with
        if coins_hit:
            Currency.collision(coins_hit, player)

        # remove bugs that collide with player
        if obstacles_hit:
            Bug.collision(obstacles_hit, player)
            pygame.event.post(slowdown)


        # when the player's HP goes to 0, post game over event
        if player.HP == 0:
            pygame.event.post(game_over)

        # after 90 seconds, spawn the end condition for the level
        if counter > 90000 and not isEnd:
            isEnd = True

        # player wins when they collide with the end sprite
        if end_hit:
            pygame.event.post(player_wins)

        show_score(screen, "Coins : " + str(player.Coins))
        show_ui(screen, "Health : " + str(player.HP), 540, 20)
        
        time_since_enter = pygame.time.get_ticks() - start_time
        seconds = (time_since_enter/1000)%60
        seconds = int(seconds)
        show_ui(screen, "Game Time: " + ("%d" % (seconds)), 490, 75)

        # update the display
        pygame.display.update()
        FramePerSec.tick(FPS)


# Game Loop
def main():
    pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Images', 'music2.wav')))
    game_intro(screen, screen_width, screen_height, FramePerSec, FPS)
    game_loop()


if __name__ == "__main__":
    main()