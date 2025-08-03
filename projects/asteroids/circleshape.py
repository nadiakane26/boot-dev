import pygame

# CircleShape class inherits from pygame's Sprite class to represent game objects as circles (even if they aren't).
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # CircleShape extends the Sprite class to also store a position, velocity, and radius.
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides(self, other):
        # Check if this circle collides with another circle
        return self.position.distance_to(other.position) < (self.radius + other.radius)
