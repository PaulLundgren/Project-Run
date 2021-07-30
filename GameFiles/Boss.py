import pygame
import os
class Boss(pygame.sprite.Sprite):
    """Represents a type of obstacle that the player must avoid. Slows the player down when collision occurs."""

    def __init__(self, screen_height):
        super().__init__()
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'bug.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (350, 350))
        self.surface = pygame.Surface((275, screen_height)) # set the image's surface
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect(center=(-150, 325))
        self.speed = 4


    def update(self):
        """Updates the current position of the bug."""

        self.rect.x += self.speed


    def draw(self, screen):
        """Draws the bug to the screen."""
        screen.blit(self.image, self.rect)


    def slowdown(self):
        pass








