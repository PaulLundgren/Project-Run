import pygame

# TODO: IN PROGRESS
class End(pygame.sprite.Sprite):
    """Represents the destination object with which the player can collide with. If the player collides with this sprite, then the level ends with the player 'winning'. """

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.surface = pygame.Surface((35, screen_height)) # random horizontal size for our surface
        self.rect = self.surface.get_rect(center = (screen_width - 15, screen_height / 2))
        self.surface.fill((0,255,0))
        self.speed = 3
        self.invisible = False # will be used to ignore platforms

    
    def update(self):
        """Changes the postition of the End sprite relative to the screen."""
        pass

    def draw(self, screen):
        """Draws the End sprite onto the screen."""
        if not self.invisible:
            screen.blit(self.surface, self.rect)

    def inc_speed(self):
        """Increase the speed at which the object moves."""
        self.speed += 1


    def slowdown(self):
        """Slow the object down when the player comes into collision with an obstacle."""
        self.speed = 3
