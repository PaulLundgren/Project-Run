import pygame

class Bug(pygame.sprite.Sprite):
    """Represents a type of obstacle that the player must avoid. Slows the player down when collision occurs."""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/bug.png")
        self.surface = pygame.Surface((40, 40))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.surface.get_rect(center = (600, 440))
        self.hasTouched = False
        
        
    def update(self):
        """Updates the current position of the bug."""
        
        self.rect.x -= 3 # for each iteration, move left 4 units
    
        # wraps the Bug to the other side of the window when it goes out of bounds, visually
        if (self.rect.left < -30):
            self.rect.right = 640
            self.rect.center = (640, 440)


    def draw(self, screen):
        """Draws the bug to the screen."""
        screen.blit(self.image, self.rect)