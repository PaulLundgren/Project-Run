"""A small tutorial w/ comments on initializing a game in Python using Pygame.
   This follows the PyGame tutorial located here: https://www.pygame.org/docs/tut/MoveIt.html"""

import pygame
import sys
from pygame.locals import *


class GameObject:
    """ A class for objects represented in the game"""

    def __init__(self, image, height, width, speed):
        self.image = image  # the object's loaded image
        self.speed = speed  # the "speed" (which is just the distance of relocation per iteration in the event cycle
        self.pos = image.get_rect().move(width, height)  # the position relative to the window

    def move(self):
        self.pos = self.pos.move(0, self.speed)

        # wrap the game object to the other side if it goes beyond the window
        if self.pos.bottom > 480:
            self.pos.top = 0


# initialize pygame modules
pygame.init()

# create a blank screen
screen = pygame.display.set_mode((640, 480))

# calling .convert() manages the pixel formats of the files being loaded
player = pygame.image.load("ball.png").convert()  # load the player image -- creates a 'Surface'
background = pygame.image.load("background_image.jpg").convert()  # load the background image -- creates a 'Surface'


screen.blit(background, (0, 0))  # draw the background screen at (X,Y) = (0,0)  [from the top-left of the window]
game_objects = []  # a list for our game objects

for x in range(10):
    obj = GameObject(player, x * 40, x * 60, x)  # create game objects
    game_objects.append(obj)

# event handling
while 1:

    # go through the events
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):  # constant QUIT + KEYWORD come from pygames.local import statement
            sys.exit()  # will exit the program w/ keyboard input or the close button in the window

    # after events, do things with objects
    for obj in game_objects:
        screen.blit(background, obj.pos, obj.pos)  # remove the images of all objects from the screen

    for obj in game_objects:
        obj.move()  # move the objects to the new location relative to the screen
        screen.blit(obj.image, obj.pos)  # redraw the images onto the screen

    # update the display
    pygame.display.update()
    pygame.time.delay(100)  # make it slower
