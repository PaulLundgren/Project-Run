import pygame

class Currency(pygame.sprite.Sprite):
    """The currency of our game. The user can collect these objects to purchase items."""
    
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.surface = pygame.Surface((45, 45))
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.surface.get_rect(center = (600, 0))
        self.sound = pygame.mixer.Sound("coin.wav")
        self.width = screen_width
        self.height = screen_height
        self.speed = 3
        self.touched = False
        self.invisible = True
        
    def update(self):
        """Updates the current position of the currency."""
        
        self.rect.x -= self.speed

            

    def draw(self, surface):
        """Draws the coin to the screen."""

        # if the coin has not collided w/ player + is a coin from a set to be drawn, then draw the coin to the screen
        if not self.touched and not self.invisible:
            surface.blit(self.image, self.rect)

    
    def collision(coins_hit, player):
        """A method that removes coin sprites when collision occurs b/w player and coin sprite."""
        for coin in coins_hit:
            if not coin.touched and not coin.invisible:
                pygame.mixer.Sound.play(pygame.mixer.Sound("coin.wav")) # play sound effect for hitting a coin
                pygame.mixer.music.stop()
                coin.touched = True
                player.Coins += 1 # Increase Coin total on hit

    def relocate(self, x, y):
        """Relocate the coin based off x and y arguments."""
        self.rect.x = x
        self.rect.y = y
    

    def inc_speed(self):
        """Increase the speed at which the object moves."""
        self.speed += 1

    
    def slowdown(self):
        """Slow the object down when the player comes into collision with an obstacle"""
        self.speed = 3