import pygame


class Enemy(pygame.sprite.Sprite):
    """Class one enemy"""
    def __init__(self, screen):
        """Init start position"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Output enemy on screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move enemy"""
        self.y += 0.1
        self.rect.y = self.y