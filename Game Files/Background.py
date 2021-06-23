import pygame

class Background():
    """The background for our game."""

    def __init__(self):
        self.image = pygame.image.load("Images/background_image.jpg").convert() # store image
        self.rect = self.image.get_rect() # store a rectangle TODO: Resize the image to match the window size

        # 1st set of coordinates
        self.x1 = 0
        self.y1 = 0

        # 2nd set of coordinates, with the y-coordinate matching the height of our image
        self.x2 = self.rect.width
        self.y2 = 0

        # the speed of the scrolling image
        self.speed = 3 

    def update(self):
        """Update the position of the image relative to the window."""

        # move both images at the same time to create the illusion of a scrolling image
        self.x1 -= self.speed
        self.x2 -= self.speed

        # reset the postitions of the images to wrap to the other side of the window
        if self.x1 <= - self.rect.width:
            self.x1 = self.rect.width
        
        if self.x2 <= - self.rect.width:
            self.x2 = self.rect.width
    

    def draw(self, surface):
        """Draw the background onto the screen with its respective coordinates."""
        surface.blit(self.image, (self.x1, self.y1))
        surface.blit(self.image, (self.x2, self.y2))