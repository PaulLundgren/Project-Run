import pygame
import random

class Platform(pygame.sprite.Sprite):
    """Represents randomly generated surfaces that the Player sprite can jump onto and move across."""
    def __init__(self, x, y):
        super().__init__()
        self.surface = pygame.Surface((random.randint(175, 250), 20)) # random horizontal size for our surface
        self.rect = self.surface.get_rect(center = (x, y)) # random spawn locations on the y-axis; always spawn them on the right side of the screen
        self.surface.fill((255,255,0))
    

    def update(self):
        """Changes the postition of the platform relative to the screen."""
        self.rect.x -= 3 # update the platform to move 3 units to the left

        if self.rect.right <= 0:
            self.kill() # delete the Sprite when it goes off the screen

    def draw(self, screen):
        """Draws the platform onto the screen."""
        screen.blit(self.surface, self.rect)