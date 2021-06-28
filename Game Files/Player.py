import pygame
from pygame.locals import *


vector = pygame.math.Vector2
ACCELERATION = 0.7 # represents gravity
FRICTION = -0.12 # represents friction

class Player(pygame.sprite.Sprite):
    """Represents the Player Sprite in our game."""

    def __init__(self, screen_width, screen_height):
        super().__init__()

        # variables for the player sprite
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (85, 85)) # scale the image
        self.width = screen_width
        self.height = screen_height
        self.surface = pygame.Surface((30, 85)) # set the image's surface      
        self.rect = self.surface.get_rect(center = (260, 430)) # set where the player spawns + it's coordinates relative to the screen
        self.flip_LEFT = False
        self.flip_RIGHT = True
        

        # vectors for the Player (will represent the movement physics of the Player object)
        self.position = vector((260, 430))
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)
        # Player attributes, i.e money, HP, Lives
        self.HP = 3
        self.Lives = 3
        self.Coins = 0
           
    
    def update(self):
        """Updates the current position of the Player."""

        # set the acceleration to be 0
        self.acceleration = vector(0,0.22)

        # this will store left and right movement
        keys = pygame.key.get_pressed()

        if keys[K_a]:
            
            self.acceleration.x = -ACCELERATION

            # changes direction of the image
            if not self.flip_LEFT:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip_LEFT = True
                self.flip_RIGHT = False
        
        if keys[K_d]:
            
            self.acceleration.x = ACCELERATION

            # changes direction of the image
            if not self.flip_RIGHT:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip_LEFT = False
                self.flip_RIGHT = True
        
        # change position, velocity, and acceleration vectors due to user input
        self.acceleration.x += self.velocity.x * FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # boundaries for our screen so the player does not go off the screen
        if self.position.x >= self.width - 40:
            self.position.x = self.width - 40
        
        if self.position.x <= 0:
            self.position.x = 0

        if self.position.y <= 50:
            self.position.y = 50

        self.rect.midbottom = self.position # update the lower boundary of the player's rectangle; neccesary for collision with platforms

        
    def hit(self, hits_list):
        """Detects if the player is in collision with a platform sprite."""

        # collision detected
        if hits_list:
            
            # if the platform is invisible, then ignore it (this means that the platform is not intended to be drawn)
            if not hits_list[0].invisible:
            
                # player is standing or falling
                if self.velocity.y >= 0:
                
                    # repositions the player sprite onto the top of the platform
                    if self.position.y < hits_list[0].rect.bottom:
                        self.position.y = hits_list[0].rect.top + 1
                        self.velocity.y = 0

            
                # player is jumping, there should be no ability to get onto a platform during this period
                if self.velocity.y < 0:
                
                    # collision causes player to move back slightly, and jump stops
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