import pygame
from Currency import *
from Platform import *
from Bug import *


"""Functions listed here are intended to generate non-player sprites."""
def coin_gen(coins, sprites):
    """Generate the coin obstacles for the game."""

    # generate 20 coins
    for i in range(20):
        coin = Currency()

        # add coin to lists
        sprites.add(coin)
        coins.add(coin)


def plat_gen(platforms, sprites):
    """Generate the platform obstacles for the game."""

    # generate 4 platforms
    for i in range(4):
        platform = Platform()

        # add platforms to lists
        platforms.add(platform)
        sprites.add(platform)


def bug_gen(bugs, obstacles, sprites):
    """Generate the bug obstacles for the game."""

    # generate 2 bugs
    for i in range(2):
        bug = Bug()

        # add bugs to lists
        bugs.add(bug)
        obstacles.add(bug)
        sprites.add(bug)

def change_coins(coins, index):
    """Change the locations of the coins."""
    x = 0
    y = 0
    count = 0

    # 1st set
    if index == 0:

        for coin in coins:
            if count < 6:
                coin.relocate(600 + 45*x, 360)
                count += 1
                
            elif 6 <= count < 9:
                y += 1
                coin.relocate(600 + 45*x, 360 - 30*y)
                count += 1
            elif 9 <= count < 12:
                y -= 1
                coin.relocate(600 + 45*x, 330 - 30*y)
                count += 1
            else:
                coin.relocate(600 + 45*x, 360)

            x += 1
            coin.touched = False
            coin.invisible = False
    
    # 2nd set
    if index == 1:

        for coin in coins:
            if count < 4:
                coin.relocate(900, 400 - 20*x)
                count += 1
            elif 4 <= count < 8:
                coin.relocate(945, 400 - 20*x)
                count += 1
            else:
                coin.relocate(950 + 45*x, 400)
            
            coin.touched = False
            coin.invisible = False
            x += 1


def change_platforms(platforms, index):
    """Change the locations of the platforms."""

    # used to change positions of certain platforms
    x = 0
    y = 0

    if index == 0:

        for platform in platforms:

            if isinstance(platform, Platform):

                if y % 2 == 0:
                    platform.relocate(600 + 250*x, 400)
                    platform.invisible = False
                else:
                    platform.invisible = True
                x += 1
                y += 1
                platform.invisible = False
    
    if index == 1:

        for platform in platforms:

            if isinstance(platform, Platform):
                platform.relocate(700, 400 - 100*y)
                x += 1
                y += 1
                platform.invisible = False


def change_bugs(bugs, index):
    """Change the locations of the bugs."""

    # used to change positions of certain bugs
    x = 0
    y = 0

    if index == 0:

        for bug in bugs:

            if y % 2 == 0:
                bug.relocate(975 + 250*x, 335 - 250*y)
                bug.invisible = False
            else:
                bug.invisible = True
            
            x += 1
            y += 1
            bug.touched = False

    

    if index == 1:

        for bug in bugs:
            bug.relocate(700 + 50*x, 430)
            bug.touched = False
            bug.invisible = False
            x += 1
            y += 1