"""Side-scrolling game. Run away from your project leader and push your commits to repo."""



import pygame
import sys
import time
import random
import csv
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
from GameFiles.Level import *


# initialize pygame modules
pygame.init()
# set the window caption for our game
pygame.display.set_caption("Project Run")

# Assign FPS value
FPS = 60
FramePerSec = pygame.time.Clock()

# create a blank screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
ROWS = 10
COLS = 1300
TILE_SIZE = screen_height // ROWS

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# image things


def gamecreation(level):
    images = []
    coin = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'coin.png')).convert_alpha()
    coin = pygame.transform.scale(coin, (TILE_SIZE, TILE_SIZE))
    bug = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'bug.png')).convert_alpha()
    bug = pygame.transform.scale(bug, (TILE_SIZE, TILE_SIZE))
    floor = pygame.Surface((TILE_SIZE, TILE_SIZE))
    floor.fill((255,0,0))
    platform = pygame.Surface((TILE_SIZE, TILE_SIZE))
    platform.fill((255,255,0))
    end = pygame.Surface((TILE_SIZE, TILE_SIZE))
    end.fill((255, 0, 255))

    images.append(coin)
    images.append(bug)
    images.append(floor)
    images.append(platform)
    images.append(end)

    # group creation
    sprites = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    bugs = pygame.sprite.Group()
    end_spawn = pygame.sprite.Group()

    # loading level
    current_level = level


    tiles = []
    for row in range(ROWS):
        row = [-1] * COLS
        tiles.append(row)

    with open(f"level_{current_level}.csv", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        for x, row in enumerate(reader):
            for y, tile in enumerate(row):
                tiles[x][y] = int(tile)

    level = Level()
    level.process(tiles, images, coins, platforms, obstacles, sprites, end_spawn, TILE_SIZE)


    # Sprite creation

    player = Player(screen_width, screen_height)
    floor = Floor(screen_width, screen_height)
    end = End(screen_width, screen_height)

    # add Non-Generated sprites to respective groups (FIXME: rework this to include player as well)
    sprites.add(floor)
    platforms.add(floor)
    gamevalues = [player, coins, platforms, obstacles, end_spawn, sprites]
    return gamevalues

# custom game over event; this occurs when the player's HP is 0
GAMEOVER = USEREVENT + 1
game_over = pygame.event.Event(GAMEOVER)

# custom event that increases the speed of the images
SPEED = USEREVENT + 2
speed_event = pygame.event.Event(SPEED)

# custom event that happens when the player reaches the end
WIN = USEREVENT + 4
player_wins = pygame.event.Event(WIN)

# custom event that 'slows down' the player (happens when there is a collision b/w the player sprite and an obstacle)
SLOWDOWN = USEREVENT + 5
slowdown = pygame.event.Event(SLOWDOWN)

# create our background
background = Background(screen_width, screen_height)


# generate items outside game loop()
# coin_gen(coins, sprites, screen_width, screen_height)
# plat_gen(platforms, sprites, screen_width, screen_height)
# bug_gen(bugs, obstacles, sprites, screen_width, screen_height)


def game_quit():
    pygame.quit()
    sys.exit()


def game_loop(player, coins, platforms, obstacles, end_spawn, sprites, current_level):

    global pause
    counter = 0 # keep track of the time in game (in milliseconds)
    isEnd = False
    FramePerSec = pygame.time.Clock()
    #pygame.time.set_timer(SPEED, 20000) # every 20 seconds, increase the speed of the game
    #pygame.time.set_timer(REDRAW, 8000) # every 8 seconds, redraw objects on the other side of the screen


    offset = FramePerSec.get_time()
    start_time = pygame.time.get_ticks()
    pause_offset = 0
    pause = False
    time_since_pause = 0
    counter += FramePerSec.get_time() - offset
    redraw_offset = 12000
    speed_offset = 20000
    #redraw_counter = FramePerSec.get_time() - offset
    #speed_counter = FramePerSec.get_time() - offset
    while True:
        counter += FramePerSec.get_time() - offset
        #redraw_counter += FramePerSec.get_time() - offset
        #speed_counter += FramePerSec.get_time() - offset
        # counter checks to throw events in respect to game time
        if counter > speed_offset: # after 20 seconds in game, the player will speed up
            pygame.event.post(speed_event)
            speed_offset = speed_offset + 20000
        
        for event in pygame.event.get():
            if event.type == QUIT:  # constant QUIT comes from pygames.local import statement
                game_quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump(platforms_hit)

                if event.key == pygame.K_ESCAPE:
                    pause = True
                   # pause_offset = FramePerSec.get_time()
                    # pygame.time.wait()
                    pause = game_pause(screen, screen_width, screen_height, FramePerSec, FPS)
                if event.key == pygame.K_p:
                    game_shop(screen, screen_width, screen_height, FramePerSec, FPS, player)


            if event.type == GAMEOVER:
                screen.fill((255,0,0))
                pygame.display.update()
                time.sleep(1)
                player.playerDeath()
                pygame.event.clear()
                player.HP = 3
                player.Coins = 0
                if(player.Lives > 1):
                    player.Lives = player.Lives - 1
                    return player, True
                player.Lives = 3
                return player, False

            if event.type == SPEED:
                background.inc_speed()

                # increase speed of sprites that are not the floor or the player
                for sprite in sprites:
                    if not isinstance(sprite, Floor) and not isinstance(sprite, Player):
                        sprite.inc_speed()

                
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

        # draw tiles
       # level.draw(screen)


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
            speed_offset = speed_offset + 20000


        # when the player's HP goes to 0, post game over event
        if player.HP == 0:
            pygame.event.post(game_over)

        # after 90 seconds, spawn the end condition for the level
        if counter > 90000 and not isEnd:
            isEnd = True

        # player wins when they collide with the end sprite
        if end_hit:
            pygame.event.post(player_wins)

        seconds = (counter/1000) % 60 # timer for ui
        seconds = int(seconds)

        show_ui(screen, "Game Time: " + ("%d" % (seconds)), 510, 75)

        # score = (0.5 * player.total_coins) + ( 0.05 * seconds) - ( 0.4 * player.HP)
        score = (1 * player.total_coins) + ( 0.4 * player.HP) + ( 0.05 * seconds)
        score = round(score, 2)
        score = score + 10 * player.Lives
        if score <= 0:
            score = 0
        player.Score = score


        show_ui(screen, "Coins : " + str(player.Coins), 100, 15)
        show_ui(screen, "Health : " + str(player.HP), 540, 20)
        show_ui(screen, "Score : " + str(score), 100, 60)
        
        # update the display
        pygame.display.update()
        FramePerSec.tick(FPS)


# Game Loop
def main():
    running = True
    pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Images', 'music2.wav')))
    while running:
        current_level = game_intro(screen, screen_width, screen_height, FramePerSec, FPS)
        gamevalues = gamecreation(current_level) # player, coins, platforms, obstacles, end_spawn, sprites
        results = game_loop(gamevalues[0], gamevalues[1], gamevalues[2], gamevalues[3], gamevalues[4], gamevalues[5], current_level)
        while results[1]:
            gamevalues = gamecreation(current_level)
            gamevalues[0] = results[0]
            results = game_loop(gamevalues[0], gamevalues[1], gamevalues[2], gamevalues[3], gamevalues[4], gamevalues[5], current_level)
    return



if __name__ == "__main__":
    main()
