from ast import Param
import pygame
from GameFiles.Bug import *
from GameFiles.Platform import *
from GameFiles.Currency import *

"""Functions listed here are intended to generate non-player sprites."""

def coin_gen(coins, sprites, screen_width, screen_height):
    """Generate the coin obstacles for the game."""

    # generate 20 coins
    for i in range(20):
        coin = Currency(screen_width, screen_height)

        # add coin to lists
        sprites.add(coin)
        coins.add(coin)


def plat_gen(platforms, sprites, screen_width, screen_height):
    """Generate the platform obstacles for the game."""

    # generate 4 platforms
    for i in range(4):
        platform = Platform(screen_width, screen_height)

        # add platforms to lists
        platforms.add(platform)
        sprites.add(platform)


def bug_gen(bugs, obstacles, sprites, screen_width, screen_height):
    """Generate the bug obstacles for the game."""

    # generate 6 bugs
    for i in range(6):
        bug = Bug(screen_width, screen_height)

        # add bugs to lists
        bugs.add(bug)
        obstacles.add(bug)
        sprites.add(bug)

def change_coins(coins, index):
    """Change the locations of the coins."""
    x = 0
    y = 0
    count = 0

    # special set that occurs when the end condition is met.
    if index == -1:
        for coin in coins:
            coin.relocate(0,0)
            coin.invisible = True
            coin.touched = False

    # 1st set
    if index == 0:

        for coin in coins:
            if count < 6:
                coin.relocate(coin.width + 45*x, coin.height - 120)
                count += 1
                coin.invisible = False
                
            elif 6 <= count < 9:
                y += 1
                coin.relocate(coin.width + 45*x, (coin.height - 120) - 30*y)
                count += 1
                coin.invisible = False
            elif 9 <= count < 12:
                y -= 1
                coin.relocate(coin.width + 45*x, (coin.height - 150) - 30*y)
                count += 1
                coin.invisible = False
            elif count < 18:
                coin.relocate(coin.width + 45*x, coin.height - 120)
                count += 1
                coin.invisible = False
            else:
                coin.relocate(0,0)
                coin.invisible = True

            x += 1
            coin.touched = False
            
    
    # 2nd set
    if index == 1:

        for coin in coins:
            if count < 4:
                coin.relocate((coin.width + 460) + 35*x, (coin.height - 280) + 30*count)
                count += 1
                coin.invisible = False
            else:
                count = 0
                x += 1
                coin.relocate(0,0)
                coin.invisible = True
            
            coin.touched = False

    
    if index == 2:

        for coin in coins:
            if count < 2:
                if y < 6:
                    coin.relocate((coin.height + 370) + 35*x, (coin.height - 190) + 30*count)

                elif y < 12:
                    coin.relocate((coin.height + 600) + 35*x, (coin.height - 190) + 30*count)

                count += 1
                y += 1
                coin.invisible = False
            else:
                count = 0
                x += 1
                
                coin.invisible = True

            coin.touched = False

    if index == 3:

        for coin in coins:

            if count < 8:
                coin.relocate(700 + 35*x, 350)
                coin.invisible = False
            elif count < 10:
                coin.relocate(700 + 35*x, 350)
                coin.invisible = True
            elif count < 18:
                coin.relocate(700 + 35*x, 275)    
                coin.invisible = False
            else:
                coin.relocate(0, 0)
                coin.invisible = True      
            
            count += 1
            x += 1
            coin.touched = False

    if index == 4:

        for coin in coins:
            if count < 5:
                coin.relocate(700 + 35*x, 420)
                coin.invisible = False
                count += 1
            elif count < 9:
                coin.relocate(0,0)
                coin.invisible = True
                count += 1
            elif count == 9:
                coin.relocate(0, 0)
                count = 0
                coin.invisible = True
            
            x += 1
            coin.touched = False

    if index == 5:

        for coin in coins:
            if count < 3:
                coin.relocate(670 + 35*x, 275 + 30*count)
                count += 1
                coin.invisible = False
            else:
                count = 0
                x += 1
                coin.relocate(0,0)
                coin.invisible = True
            
            coin.touched = False
            
            


def change_platforms(platforms, index):
    """Change the locations of the platforms."""

    # used to change positions of certain platforms
    x = 0
    y = 0
    count = 0

    # special set that occurs when the end condition is met.
    if index == -1:
        for platform in platforms:

            if isinstance(platform, Platform):
                platform.relocate(0,0)
                platform.invisible = True
                

    if index == 0:

        for platform in platforms:

            if isinstance(platform, Platform):

                if y % 2 == 0:
                    platform.relocate(platform.width+ 250*x, platform.height - 80)
                    platform.invisible = False
                else:
                    platform.invisible = True
                x += 1
                y += 1
                platform.invisible = False
    
    if index == 1:

        for platform in platforms:

            if isinstance(platform, Platform):

                if count < 1:
                    platform.relocate(platform.width + 60, platform.height - 80)
                    x += 1
                    y += 1
                    platform.invisible = False

    if index == 2:

        for platform in platforms:

            if isinstance(platform, Platform):
                platform.relocate(0,0)
                platform.invisible = True

    if index == 3:

        for platform in platforms:

            if isinstance(platform, Platform):
                if count < 2:
                    platform.relocate(700 + 350*x, 400 - 75*y)
                    platform.invisible = False                   
                else:
                    platform.relocate(0, 0)
                    platform.invisible = True

                x += 1
                y += 1
                count += 1

    if index == 4:

        for platform in platforms:

            if isinstance(platform, Platform):
                platform.relocate(0,0)
                platform.invisible = True
    

    if index == 5:

        for platform in platforms:

            if isinstance(platform, Platform):
                platform.relocate(0,0)
                platform.invisible = True




def change_bugs(bugs, index):
    """Change the locations of the bugs."""

    # used to change positions of certain bugs
    x = 0
    y = 0
    count = 0

    # special set that occurs when the end condition is met.
    if index == -1:
        for bug in bugs:
            bug.relocate(0,0)
            bug.invisible = True
            bug.touched = False


    if index == 0:

        for bug in bugs:

            if count < 1:
                bug.relocate(bug.width + 345 + 250*x, (bug.height - 145) - 250*y)
                bug.invisible = False
                count += 1
            elif count < 2:
                bug.relocate(bug.width + 395, bug.height - 80)
                bug.invisible = False
                count += 1
            else:
                bug.relocate(0,0)
                bug.invisible = True
            
            bug.touched = False
            x += 1
            y += 1
            

    

    if index == 1:

        for bug in bugs:
            if count < 1:
                bug.relocate(bug.width + 50*x, bug.height - 70)
                count += 1
                bug.invisible = False
            elif count < 2:
                bug.relocate(bug.width + 385, bug.height - 130)
                count += 1
                bug.invisible = False
            elif count < 5:
                bug.relocate((bug.width + 510) + 50*x, bug.height - 50)
                bug.invisible = False
                count += 1
            else:
                bug.relocate(0,0)
                bug.invisible = True

            bug.touched = False
            x += 1
            y += 1

    if index == 2:

        for bug in bugs:

            if count < 3:
                bug.relocate(1000 + 45*x, 420)
                bug.invisible = False
                count += 1
            else:
                bug.relocate(1200 + 45*x, 420)
                bug.invisible = False
            
            x += 1
            bug.touched = False

    if index == 3:

        for bug in bugs:

            if count < 1:
                bug.relocate(720, 430)
                bug.invisible = False

            elif count < 2:
                bug.relocate(1000, 330)
                bug.invisible = False

            elif count < 3:

                bug.relocate(1345, 275)
                bug.invisible = False
            
            else:
                bug.relocate(0,0)
                bug.invisible = True
            
            count += 1
            bug.touched = False


    if index == 4:

        for bug in bugs:

            if count < 3:

                bug.relocate(915 + 40*x, 420)
                bug.invisible = False
                count += 1
                x += 1
            else:
                bug.relocate(1150 + 40*x, 420)
                bug.invisible = False
                x += 1

            bug.touched = False


    if index == 5:

        for bug in bugs:

            if count < 2:
                bug.relocate(700, 420 - 45*y)
                count += 1
                y += 1
                bug.invisible = False
            elif count < 4:
                bug.relocate(700, 240 - 45*x)
                count += 1
                y = 0
                x += 1
                bug.invisible = False
            else:
                bug.relocate(855, 330 - 45*y)
                y += 1
                bug.invisible = False

            bug.touched = False

