import pygame

class Ship:
    """ A claa to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/SpaceShip3.png')
        self.rect = self.image.get_rect()

        # Star each new ship at the botton center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship and its current location"""

        self.screen.blit(self.image, self.rect)