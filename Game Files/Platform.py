import pygame

class Platform(pygame.sprite.Sprite):
    """Represents a solid surface that the Player sprite cannot fall through."""
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((640, 30))
        self.rect = self.surface.get_rect(center = (640 / 2, 470))
    
    # TODO: change these next two functions to represent images of platforms the user can jump on, etc.
    def update(self):
        pass

    def draw(self, screen):
        pass