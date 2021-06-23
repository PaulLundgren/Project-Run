import pygame
from pygame.locals import *


vector = pygame.math.Vector2
ACCELERATION = 0.7 # represents gravity
FRICTION = -0.12 # represents friction

class Player(pygame.sprite.Sprite):
    """Represents the Player Sprite in our game."""

    def __init__(self):
        super().__init__()

        # variables for the player sprite
        self.image = pygame.image.load("Images/player.png")
        self.image = pygame.transform.scale(self.image, (85, 85)) # scale the image
        self.surface = pygame.Surface((30, 85)) # set the image's surface      
        self.rect = self.surface.get_rect(center = (260, 430)) # set where the player spawns + it's coordinates relative to the screen

        # vectors for the Player (will represent the movement physics of the Player object)
        self.position = vector((260, 430))
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)
        self.HP = 3
           
    
    def update(self):
        """Updates the current position of the Player."""

        # set the acceleration to be 0
        self.acceleration = vector(0,0.2)
        
        # mechanics for movement
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # boundaries for our screen so the player does not go off the screen
        if self.position.y <= 50:
            self.position.y = 50

        self.rect.midbottom = self.position # update the lower boundary of the player's rectangle; neccesary for collision with platforms

        
    

    def hit(self, hits_list):
        """Detects if the player is in collision with a platform sprite."""

        # only detect collision when the player is falliing
        if self.velocity.y > 0:
            
            # collision detected
            if hits_list:

                if self.position.y < hits_list[0].rect.bottom: # player's y-position must be less than that of the bottom of the platform (visually, this means the player must be above the bottom of the platform)
                    self.position.y = hits_list[0].rect.top + 1 # the vertical position of the player is on top of the platform's top rectangle coordinate
                    self.velocity.y = 0 # player stops falling

        # detect collision while jumping
        elif self.velocity.y <= 0:

            # collision detected
            if hits_list:
                self.velocity.y = 0 # player will stop moving up when there is a collision above


    def jump(self, hits_list):
        """A simple jumping mechanic for the player."""

        if hits_list and self.velocity.y == 0:
            self.velocity.y = -7


    def draw(self, surface):
        """Draws the player to the screen."""
        surface.blit(self.image, (self.rect))