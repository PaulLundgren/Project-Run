import pygame

class Floor(pygame.sprite.Sprite):
    """Represents a solid surface that the Player sprite cannot fall through."""
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((640, 10))
        self.rect = self.surface.get_rect(center = (640 / 2, 475))
        self.surface.fill((255,0,0))
        self.invisible = False
    
    
    def update(self):
        pass

    def draw(self, screen):
        """Draw the floor onto the screen."""
        screen.blit(self.surface, self.rect)