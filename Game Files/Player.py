import pygame
from pygame.locals import *
import Floor


vector = pygame.math.Vector2
ACCELERATION = 0.7 # represents gravity
FRICTION = -0.12 # represents friction

class Player(pygame.sprite.Sprite):
    """Represents the Player Sprite in our game."""

    def __init__(self):
        super().__init__()

        # variables for the player sprite
        self.image = pygame.image.load("player.png")
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

        # this will store left and right movement
        keys = pygame.key.get_pressed()

        if keys[K_a]:
            self.acceleration.x = -ACCELERATION
        
        if keys[K_d]:
            self.acceleration.x = ACCELERATION
        
        # change position, velocity, and acceleration vectors due to user input
        self.acceleration.x += self.velocity.x * FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # boundaries for our screen so the player does not go off the screen
        if self.position.x >= 590:
            self.position.x = 590
        
        if self.position.x <= 0:
            self.position.x = 0

        if self.position.y <= 50:
            self.position.y = 50

        self.rect.midbottom = self.position # update the lower boundary of the player's rectangle; neccesary for collision with platforms

        
    

    def hit(self, hits_list):
        """Detects if the player is in collision with a platform sprite."""

        # collision detected
        if hits_list:
            
            # player is standing or falling
            if self.velocity.y >= 0:
                
                if self.position.y < hits_list[0].rect.bottom:
                    self.position.y = hits_list[0].rect.top + 1
                    self.velocity.y = 0

            
            # player is jumping, there should be no ability to get onto a platform during this period
            if self.velocity.y < 0:

                self.position.x -= 3
                self.velocity.y = 0
                self.acceleration.x = 0





        
        
        


    def jump(self, hits_list):
        """A simple jumping mechanic for the player."""

        if hits_list and self.velocity.y == 0:
            self.velocity.y = -7



    def draw(self, surface):
        """Draws the player to the screen."""
        surface.blit(self.image, (self.rect))