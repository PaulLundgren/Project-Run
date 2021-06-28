import pygame

class Bug(pygame.sprite.Sprite):
    """Represents a type of obstacle that the player must avoid. Slows the player down when collision occurs."""
    
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("bug.png")
        self.surface = pygame.Surface((20, 40))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.surface.get_rect(center = (300, 300))
        self.width = screen_width
        self.height = screen_height
        self.speed = 3
        self.touched = False
        self.invisible = True
        
        
    def update(self):
        """Updates the current position of the bug."""
        
        self.rect.x -= self.speed


    def draw(self, screen):
        """Draws the bug to the screen."""
        if not self.touched and not self.invisible:
            screen.blit(self.image, self.rect)

    def collision(bugs_hit, player):
        """A method that decreases HP when collision occurs b/w player and bug sprite."""

        for bug in bugs_hit:

            if not bug.touched and not bug.invisible:
                pygame.mixer.Sound.play(pygame.mixer.Sound("damage.wav")) # play sound effect for hitting a bug
                pygame.mixer.music.stop()
                bug.touched = True
                player.HP -= 1 # decrease HP of the player

    def relocate(self, x, y):
        """Relocates bug sprite based on x and y arguments."""
        self.rect.x = x
        self.rect.y = y

    def inc_speed(self):
        """Increase the speed at which the object moves."""
        self.speed += 1

    
    def slowdown(self):
        """Slow the object down when the player comes into collision with an obstacle"""
        self.speed = 3