import pygame

class Currency(pygame.sprite.Sprite):
    """The currency of our game. The user can collect these objects to purchase items."""
    
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.surface = pygame.Surface((45, 45))
        self.image = pygame.transform.scale(self.image, (45, 45))

        self.positions = (410, 350, 425, 200, 350) # predetermined locations for the coins to relocate to
        self.rect = self.surface.get_rect(center = (600 - pos, self.positions[0]))
        self.pos_index = 0 # index to use for our predetermined drawing locations for the coins
        self.isTouched = False # boolean that determines if the player sprite collides with a coin sprite
        
    def update(self):
        """Updates the current position of the Player."""
        
        self.rect.move_ip(-4, 0) # for each iteration, move left 4 units

        # wraps the coin to the other side of the screen
        if (self.rect.left < -30):
            self.isTouched = False # allows for the coin to be drawn to the screen
            self.rect.right = 640
            self.rect.center = (640, self.positions[self.pos_index])

            # increment through our predetermined locations for the coins to relocate to
            if self.pos_index == 4:
                self.pos_index = 0
            else:
                self.pos_index += 1

    def draw(self, surface):
        """Draws the coin to the screen."""

        # if the player has not collided with the coin, then draw the coin onto the screen
        if not self.isTouched:
            surface.blit(self.image, self.rect)