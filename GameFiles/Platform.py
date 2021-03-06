import pygame
import random

class Platform(pygame.sprite.Sprite):
    """Represents randomly generated surfaces that the Player sprite can jump onto and move across."""
    def __init__(self, tile_data):
        super().__init__()
        self.image = tile_data[0]
        self.rect = tile_data[1]
        self.speed = 3
        self.invisible = False # will be used to ignore platforms
    

    def update(self):
        """Changes the postition of the platform relative to the screen."""
        self.rect.x -= self.speed

    def draw(self, screen):
        """Draws the platform onto the screen."""
        if not self.invisible:
            screen.blit(self.image, self.rect)

    
    def relocate(self, x, y):
        """Relocate the platform based off x and y arguments."""
        self.rect.x = x
        self.rect.y = y

    
    def inc_speed(self):
        """Increase the speed at which the object moves."""
        self.speed += 1


    def slowdown(self):
        """Slow the object down when the player comes into collision with an obstacle"""
        self.speed = 3