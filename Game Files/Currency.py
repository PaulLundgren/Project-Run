import pygame

class Currency(pygame.sprite.Sprite):
    """The currency of our game. The user can collect these objects to purchase items."""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.surface = pygame.Surface((45, 45))
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.surface.get_rect(center = (1000 + x, y))
        
    def update(self):
        """Updates the current position of the Player."""
        
        self.rect.x -= 3 # for each iteration, move left 4 units

        # wraps the coin to the other side of the screen
        if (self.rect.left < -30):
            self.kill() # remove the coin when it goes off the screen

            

    def draw(self, surface):
        """Draws the coin to the screen."""

        if self.rect.left < 650:
            surface.blit(self.image, self.rect)

    
    def collision(coins_hit):
        """A method that removes coin sprites when collision occurs b/w player and coin sprite."""

        for coin in coins_hit:
                coin.kill() # remove the sprite if a collision is detected
