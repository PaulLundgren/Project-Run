import pygame
import os
class Currency(pygame.sprite.Sprite):
    """The currency of our game. The user can collect these objects to purchase items."""
    
    def __init__(self, tile_data):
        super().__init__()
        self.image = tile_data[0]
        self.rect = tile_data[1]
        self.speed = 3
        self.touched = False
        self.invisible = False
        
    def update(self):
        """Updates the current position of the currency."""
        self.rect.x -= self.speed

            

    def draw(self, surface):
        """Draws the coin to the screen."""

        # if the coin has not collided w/ player + is a coin from a set to be drawn, then draw the coin to the screen
        if not self.touched:
            surface.blit(self.image, self.rect)

    
    def collision(coins_hit, player):
        """A method that removes coin sprites when collision occurs b/w player and coin sprite."""
        for coin in coins_hit:
            if not coin.touched:
                pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Images', 'coin.wav')))
                # pygame.mixer.Sound.play(pygame.mixer.Sound("coin.wav")) # play sound effect for hitting a coin
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